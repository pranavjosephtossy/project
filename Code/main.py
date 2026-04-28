import json
import hashlib
import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

USE_CASE = "sports event related hate speech and abuse"

with open("example_raw_response.json", "r") as f:
    data = json.load(f)

posts = []
for child in data["data"]["children"]:
    if child["kind"] == "t3":
        d = child["data"]
        posts.append({
            "id": d.get("id"),
            "author": d.get("author"),
            "created_utc": d.get("created_utc"),
            "subreddit": d.get("subreddit"),
            "title": d.get("title"),
            "selftext": d.get("selftext"),
            "url": d.get("url"),
            "permalink": d.get("permalink"),
            "score": d.get("score"),
            "num_comments": d.get("num_comments"),
        })

print(f"{len(posts)} post(s) extracted\n")

relevant, grey_area, irrelevant = [], [], []

for post in posts:
    prompt = f"""
Analyse this Reddit post for: {USE_CASE}

Title: {post['title']}
Body: {post['selftext']}

Reply in raw JSON only:
{{"category": "relevant/irrelevant/grey_area", "severity": "low/medium/high/none - give ona scale of 1 - 10", "reasoning": "a senetnce describing the word used and whys its offenive"}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a digital forensics content analyser."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=200
    )

    result = json.loads(response.choices[0].message.content.strip().replace("```json","").replace("```",""))

    post["llm_category"] = result["category"]
    post["llm_severity"] = result["severity"]
    post["llm_reasoning"] = result["reasoning"]
    post["sha256_hash"] = hashlib.sha256(json.dumps(post, sort_keys=True).encode()).hexdigest()
    post["collected_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    print(f"[{result['category'].upper()}] {post['id']} | {result['severity']} | {result['reasoning']}")

    if result["category"] == "relevant": relevant.append(post)
    elif result["category"] == "grey_area": grey_area.append(post)
    else: irrelevant.append(post)

for fname, bucket in [("relevant.json", relevant), ("grey_area.json", grey_area), ("irrelevant.json", irrelevant)]:
    with open(fname, "w") as f:
        json.dump(bucket, f, indent=2)

print(f"\nRelevant: {len(relevant)} | Grey Area: {len(grey_area)} | Irrelevant: {len(irrelevant)}")
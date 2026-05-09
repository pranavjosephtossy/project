import json
import hashlib
import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

USE_CASE = "hate speech and abuse"

# load the YouTube data
with open("youtube_collection_with_comments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"{len(data)} video(s) loaded\n")

# every record goes into one list
all_records = []


def analyse_with_llm(content_type, text):
    prompt = f"""
Analyse this YouTube {content_type} for: {USE_CASE}

Content: {text}

Reply in raw JSON only:
{{"severity": "low/medium/high/none - give on a scale of 1 - 10", "reasoning": "a sentence describing why you assigned that severity"}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a digital forensics content analyser."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=50
    )

    result = json.loads(response.choices[0].message.content.strip().replace("```json", "").replace("```", ""))
    return result["severity"], result["reasoning"]


# loop through each video
for video in data:
    video_text = f"Title: {video.get('title')}\nDescription: {video.get('description')}"
    severity, reasoning = analyse_with_llm("video", video_text)

    video["llm_severity"] = severity
    video["llm_reasoning"] = reasoning
    video["sha256_hash"] = hashlib.sha256(json.dumps(video, sort_keys=True).encode()).hexdigest()
    video["collected_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    print(f"[VIDEO] {video.get('video_id')} | {severity} | {reasoning}")

    # loop through every comment under the video
    for comment in video.get("comments", []):
        severity, reasoning = analyse_with_llm("comment", comment.get("comment_text", ""))

        comment["llm_severity"] = severity
        comment["llm_reasoning"] = reasoning
        comment["sha256_hash"] = hashlib.sha256(json.dumps(comment, sort_keys=True).encode()).hexdigest()
        comment["collected_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        print(f"[COMMENT] {comment.get('comment_id')} | {severity} | {reasoning}")

    all_records.append(video)
    print()

# everything goes into one single JSON filep
with open("youtube_analysed.json", "w") as f:
    json.dump(all_records, f, indent=2)

print(f"\n{len(all_records)} video(s) analysed and saved to youtube_analysed.json")
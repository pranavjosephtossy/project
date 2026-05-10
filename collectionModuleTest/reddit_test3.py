import hashlib
import json
from datetime import datetime

# Fake Reddit-like data
fake_posts = [
    {
        "author": "user123",
        "title": "Suspicious activity reported during football event",
        "body": "Several fake ticket links were shared before the match.",
        "created_utc": 1713500000,
        "id": "abc001",
        "permalink": "/r/cybersecurity/comments/abc001/example_post_1/"
    },
    {
        "author": "throwaway99",
        "title": "Possible misinformation campaign in subreddit",
        "body": "Multiple accounts are posting the same misleading story.",
        "created_utc": 1713503600,
        "id": "abc002",
        "permalink": "/r/cybersecurity/comments/abc002/example_post_2/"
    },
    {
        "author": "investigatorX",
        "title": "Abusive comments increasing around sports event",
        "body": "Users are posting slurs and targeted harassment.",
        "created_utc": 1713507200,
        "id": "abc003",
        "permalink": "/r/cybersecurity/comments/abc003/example_post_3/"
    }
]

subreddit_name = "cybersecurity"
collected_data = []

for post in fake_posts:
    author = post["author"]
    title = post["title"]
    body = post["body"]
    timestamp = post["created_utc"]
    post_id = post["id"]
    permalink = "https://www.reddit.com" + post["permalink"]
    collected_at = datetime.utcnow().isoformat() + "Z"

    raw_data = str(timestamp) + author + title + body
    evidence_hash = hashlib.sha256(raw_data.encode("utf-8")).hexdigest()

    post_record = {
        "collected_at": collected_at,
        "subreddit": subreddit_name,
        "post_id": post_id,
        "author": author,
        "title": title,
        "body": body,
        "created_utc": timestamp,
        "permalink": permalink,
        "hash_sha256": evidence_hash
    }

    collected_data.append(post_record)

    print(f"--- NEW RECORD CAPTURED ---")
    print(f"Time: {timestamp}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Forensic SHA-256 Hash: {evidence_hash}")
    print("-" * 30)

with open("reddit_collection.json", "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4, ensure_ascii=False)

print("\nFake data successfully saved to reddit_collection.json")
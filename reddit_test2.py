import praw
import hashlib
import json
from datetime import datetime

# Connect script to Reddit
reddit = praw.Reddit(
    client_id="",  # will bpaste here
    client_secret="",  #will b paste here
    user_agent="windows:ForensicsThesis:v1.0 (by /u/YOUR_USERNAME)"
)

print("Successfully connected to Reddit API!")
print("Fetching preemptive data...\n")

# Connect to subreddit
subreddit_name = "cybersecurity"
subreddit = reddit.subreddit(subreddit_name)

# List to store collected posts
collected_data = []

# Fetch newest 5 posts
for post in subreddit.new(limit=5):
    author = str(post.author)
    title = post.title
    body = post.selftext
    timestamp = int(post.created_utc)
    post_id = post.id
    permalink = "https://www.reddit.com" + post.permalink
    collected_at = datetime.utcnow().isoformat() + "Z"

    # Create raw data for hashing
    raw_data = str(timestamp) + author + title + body
    evidence_hash = hashlib.sha256(raw_data.encode("utf-8")).hexdigest()

    # Store post as dictionary
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

    # Printing to console too just cos
    print(f"--- NEW RECORD CAPTURED ---")
    print(f"Time: {timestamp}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Forensic SHA-256 Hash: {evidence_hash}")
    print("-" * 30)

# Save to JSON file
with open("reddit_collection.json", "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4, ensure_ascii=False)

print("\nData successfully saved to reddit_collection.json")
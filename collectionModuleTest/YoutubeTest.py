import requests
import hashlib
import json
from datetime import datetime

# YouTube Data API v3 setup
API_KEY = "AIzaSyDQNBLpAiY9N_pZg4kBGZOtvj9UXmKvrtU"
SEARCH_QUERY = "cybersecurity"
MAX_RESULTS = 5

# Fetch data from YouTube API
url = "https://www.googleapis.com/youtube/v3/search"

#Set parameters for the API request
params = {
    "part": "snippet",
    "q": SEARCH_QUERY,
    "type": "video",
    "maxResults": MAX_RESULTS,
    "key": API_KEY
}

# Make the API request and parse the response
response = requests.get(url, params=params)
data = response.json()

# List to store collected video records
collected_data = []

# Process each video item in the response
for item in data.get("items", []):
    video_id = item["id"]["videoId"]
    snippet = item["snippet"]

# Extract relevant fields
    title = snippet["title"]
    description = snippet["description"]
    channel_title = snippet["channelTitle"]
    published_at = snippet["publishedAt"]
    collected_at = datetime.utcnow().isoformat() + "Z"
    video_url = f"https://www.youtube.com/watch?v={video_id}"

# Create raw data string for hashing
    raw_data = published_at + channel_title + title + description
    evidence_hash = hashlib.sha256(raw_data.encode("utf-8")).hexdigest()

# Create a record dictionary for the video
    record = {
        "collected_at": collected_at,
        "platform": "YouTube",
        "search_query": SEARCH_QUERY,
        "video_id": video_id,
        "channel_title": channel_title,
        "title": title,
        "description": description,
        "published_at": published_at,
        "video_url": video_url,
        "hash_sha256": evidence_hash
    }

# Append the record to the collected data list
    collected_data.append(record)

# Print the captured record to the console
    print("--- NEW VIDEO RECORD CAPTURED ---")
    print(f"Published: {published_at}")
    print(f"Channel: {channel_title}")
    print(f"Title: {title}")
    print(f"Hash: {evidence_hash}")
    print("-" * 30)

# Save the collected data to a JSON file
with open("youtube_collection.json", "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4, ensure_ascii=False)

# Final message indicating successful data saving
print("\nData successfully saved to youtube_collection.json")
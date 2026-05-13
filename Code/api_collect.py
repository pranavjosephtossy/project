import requests
import hashlib
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs
'''
SEARCH_QUERY = "slushynoobz"
MAX_RESULTS = 3          # number of videos to collect
MAX_COMMENTS = 5         # number of comments per video
'''
# YouTube Data API v3 setup again, but now with comments collection too
API_KEY = ""

def api_collect_module(video_link):
    parsed = urlparse(video_link)
    video_id= parse_qs(parsed.query).get("v",[None])[0]

    if video_id is None:
        print("YT link invalid!!")
        return None
    
    MAX_COMMENTS = 7         # number of comments per video
    # API endpoints for videos and getting comments
    video_url = "https://www.googleapis.com/youtube/v3/videos"
    comments_url = "https://www.googleapis.com/youtube/v3/commentThreads"

    # list to store collected video records with comments
    collected_data = []
    comment_list = []

    '''
    # step 1 searching for videos
    search_params = {
        "part": "snippet",
        "q": SEARCH_QUERY,
        "type": "video",
        "maxResults": MAX_RESULTS,
        "key": API_KEY
    }
    '''

    video_params = {
       "part": "snippet",
       "id": video_id,
       "key": API_KEY
    }

    # make the API request to get video
    video_resp= requests.get(video_url, params=video_params).json()

    # print message indicating start of data collection
    print("Fetching YouTube video and comments...\n")

    snippet = video_resp["items"][0]["snippet"]

    title = snippet["title"]
    description = snippet["description"]
    channel_title = snippet["channelTitle"]
    published_at = snippet["publishedAt"]
    collected_at = datetime.utcnow().isoformat() + "Z"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    # hashing the video metadata
    raw_video_data = published_at + channel_title + title + description
    video_hash = hashlib.sha256(raw_video_data.encode("utf-8")).hexdigest()


    # set parameters for the comments API request
    comment_params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": MAX_COMMENTS,
        "textFormat": "plainText",
        "key": API_KEY
    }

    # make the API request to get comments for the video
    comment_response = requests.get(comments_url, params=comment_params)
    comment_data = comment_response.json()

    # process each comment item in the response
    for comment_item in comment_data.get("items", []):
        top_comment = comment_item["snippet"]["topLevelComment"]["snippet"]

        # extract relevant fields for the comment
        comment_author = top_comment.get("authorDisplayName", "Unknown")
        comment_text = top_comment.get("textDisplay", "")
        comment_published_at = top_comment.get("publishedAt", "")
        comment_id = comment_item["snippet"]["topLevelComment"]["id"]

    # create raw data string for hashing the comment
        raw_comment_data = comment_published_at + comment_author + comment_text
        comment_hash = hashlib.sha256(raw_comment_data.encode("utf-8")).hexdigest()

    # create a record dictionary for the comment
        comment_record = {
            "comment_id": comment_id,
            "comment_author": comment_author,
            "comment_text": comment_text,
            "comment_published_at": comment_published_at,
            "comment_hash_sha256": comment_hash
        }
    # append the comment record to the comments list for this video
    comment_list.append(comment_record)

        # step 3 store video + comments together
    video_record = {
        "collected_at": collected_at,
        "platform": "YouTube",
        "video_id": video_id,
        "channel_title": channel_title,
        "title": title,
        "description": description,
        "published_at": published_at,
        "video_url": youtube_url,
        "video_hash_sha256": video_hash,
        "comments": comment_list
    }

    # append the video record (with comments) to the collected data list
    collected_data.append(video_record)

    # Print summary to terminal just for review purposes
    print("--- NEW VIDEO RECORD CAPTURED ---")
    print(f"Title: {title}")
    print(f"Channel: {channel_title}")
    print(f"Published: {published_at}")
    print(f"Video Hash: {video_hash}")
    print(f"Comments collected: {len(comment_list)}")
    print("-" * 40)

    # step 4 save to JSON
    output_file = f"youtube_vid_{video_id}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(collected_data, f, indent=4, ensure_ascii=False)
    print("\nData successfully collected and saved")

    return output_file
import praw #library to interact w Reddit API 
import time
import hashlib

# connects script to reddit
reddit = praw.Reddit(
    client_id="", #to be pasted 
    client_secret="",#tp be pasted 
    user_agent="windows:ForensicsThesis:v1.0 (by )" #reddit username here
)

#just for testing connection to reddit api, can be removed later
print("Successfully connected to Reddit API!")
print("Fetching preemptive data...\n")

# connects to r/ whatever you put in for example rn its r/cybersecyruty
subreddit = reddit.subreddit("cybersecurity")

# 3. getting the 5 recent posts
for post in subreddit.new(limit=5):
    
    # get the data need for the thesis and sort into author, title, body, timestamp
    author = str(post.author)
    title = post.title
    body = post.selftext
    timestamp = str(int(post.created_utc))
    
    # 4. FORENSIC HASHING (methodology!)
    raw_data = timestamp + author + title + body
    evidence_hash = hashlib.sha256(raw_data.encode('utf-8')).hexdigest()
    
    # Print the results to the screen
    print(f"--- NEW RECORD CAPTURED ---")
    print(f"Time: {timestamp}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Forensic SHA-256 Hash: {evidence_hash}")
    print("-" * 30)
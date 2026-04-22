import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

def sha256(value: str)-> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def evidence_storage(raw_json: dict, analysis_output: dict, storage_root="evidence_store"):

    raw_content= raw_json["content"]
    raw_username= raw_json["username"]
    analysis_content= analysis_output["content"]
    analysis_username= analysis_output["username"]

    print("Intrgrity of raw json:")
    if raw_json_hash != sha256(json.dumps(raw_json,sort_keys=True)):
        print("Hash mismatch!!!")
    else:
        print("Hash Matched!")
    print("Integrity between analysis module and collection/raw module json:")
    if sha256(raw_content)!= sha256(analysis_content):
        print("Hash mismatch, Content does not match!!! Possible LLM hallucination")
    elif sha256(raw_username)!= sha256(analysis_username):
        print("Hash mismatch, Username does not match!!! Possible alteration")
    
    content_hash= sha256(raw_content)
    username_hash= sha256(raw_username)

    storage_chain_entry = {
        "timestamp": utc_now(),
        "action": "stored",
        "performed_by":"forensic_storage_module"
    }

    forensic_package = {
        "raw_content": raw_json,
        "analysis_output": analysis_content,
        "hashes":{
            "initial_raw_json_hash": raw_json_hash,
            "content_hash": sha256(analysis_content),
            "username_hash": sha256(analysis_username)
            },
        "chain_of_custody": "ef3e"
        }
    

example_json ={
    "content": "This is an example",
    "username": "example_adbd",
    "subreddit": "cybersecurity",
    "timestamp": "2026-04-5"
}
analysis_json ={
    "content": "This is an example",
    "username": "example_adbdws",
    "subreddit": "cybersecurity",
    "timestamp": "2026-04-7"
}

raw_json_hash = sha256(json.dumps(example_json, sort_keys=True))

evidence_storage(example_json,analysis_json)
    

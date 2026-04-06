import json
import hashlib
import uuid
from datetime import datetime, timezone
from pathlib import Path

def sha256(value: str)-> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def evidence_storage(json_item: dict, analysis_output: dict, storage_root="evidence_store"):

    content= json_item["content"]
    username= json_item["username"]

    initial_hash= json_item["initial_hash"]
    current_hash= sha256(content)

    if current_hash != initial_hash:
        print("Hash mismatch, evidence altered!!!")
        return
    
    content_hash= sha256(content)
    username_hash= sha256(username)

    storage_chain_entry = {
        "timestamp": utc_now,
        "action": "stored",
        "performed_by":"forensic_storage_module"
    }

    forensic_package ={
        "evidence_id": str(uuid.uuid4()),
        "raw_content": json_item,
        "hashes":{
            "initial_hash": initial_hash,
            "content_hash": content_hash,
            "username_hash": username_hash
            }
        }
    

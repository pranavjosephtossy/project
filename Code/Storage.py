import json
import hashlib
from datetime import datetime, timezone
from chain_of_custody import add_chain_of_custody_entry
from pathlib import Path

def sha256(value: str)-> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def evidence_storage(raw_json, analysis_output, collection_log, analysis_log):

    analysis_content= analysis_output["content"]
    '''
    print("Intrgrity of raw json:")
    if raw_json_hash != sha256(json.dumps(raw_json,sort_keys=True)):
        print("Hash mismatch!!!")
    else:
        print("Hash Matched!")
    '''

    
    print("Integrity between analysis module and collection/raw module json:")
    if raw_json["comment_hash_sha256"]!= sha256(analysis_content):
        print("Hash mismatch, Content does not match!!! Possible LLM hallucination")

    content_hash= sha256(raw_content)

    storage_log = [add_chain_of_custody_entry("stored","forensic_storage_module")]
    
    final_chain= collection_log+analysis_log+storage_log
    
    forensic_package = {
        "raw_content": raw_json,
        "analysis_output": analysis_output,
        "hashes":{
            "initial_raw_json_hash": raw_json_hash,
            "content_hash": raw_json["comment_hash_sha256"]
            },
        "chain_of_custody": final_chain
        }
    
    return forensic_package


    


from datetime import *

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def add_chain_of_custody_entry(action: str, performed_by: str) -> dict:
    return {
        "timestamp": utc_now(),
        "action": action,
        "performed_by": performed_by
    }
from chain_of_custody import add_chain_of_custody_entry

def collect_item(raw_item):
    collection_log = [
        add_chain_of_custody_entry(action="collected", performed_by="collection_module")
    ]
    return raw_item, collection_log
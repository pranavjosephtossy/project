from Storage import evidence_storage

json_dump = [
    {
    "content": "This is an example",
    "username": "example_adbd",
    "subreddit": "cybersecurity",
    "timestamp": "2026-04-5"
    },
    {
    "content": "This is also an example"
    }
]
def run_main():
    for raw_item in json_dump:

        # calls collection and gets back raw_json and log item
        # calls analysis passes raw_json and gets analysis_json and log item
        # calls storage passes both jsons and logs
        evidence_storage()

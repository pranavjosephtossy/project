from Storage import evidence_storage
from analysis import *

def run_main():
        #calls collection module and gets back raw_json and log item
        collection()

        with open("youtube_collection_with_comments.json","r") as f:
              json_dump = json.load(f)

        for raw_item in json_dump:
            #i need a way to log each raw item has been collected
            raw_json, collection_log = collect_item(raw_item)

            #calls analysis passes raw_json and gets analysis_json and log item
            analysis_json, analysis_log = analysis(raw_json)
            
            # calls storage passes both jsons and logs
            evidence_storage(raw_json, analysis_json, collection_log, analysis_log)

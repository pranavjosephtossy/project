from Storage import evidence_storage
from analysis import *

def run_main():
        
      user_input=input("1 for synthetic,2 for preinstalled yt and 3 for custom")
      if user_input==1:
            print("Not implemented yet")

      elif user_input==2:
            with open("youtube_collection_with_comments.json","r") as f:
                  json_dump = json.load(f)
            
      elif user_input==3:
            user_input_yt_title=input("Enter yt link")
            #calls collection module and gets back raw_json and log item
            collection()
            with open("youtube_collection_with_comments.json","r") as f:
                  json_dump = json.load(f)

      else:
            print("Invalid input")
            
      for raw_item in json_dump:
            #i need a way to log each raw item has been collected
            raw_json, collection_log = collect_item(raw_item)

            #calls analysis passes raw_json and gets analysis_json and log item
            analysis_json, analysis_log = analysis(raw_json)
            
            # calls storage passes both jsons and logs
            forensic_package=evidence_storage(raw_json, analysis_json, collection_log, analysis_log)

            print("Forensic Package")
            print(json.dump(forensic_package, output_file, indent=4))
            output_file = f"forensic__package{raw_json['video_id']}.json"
            with open(output_file, "w", encoding="utf-8") as outfile:
                  json.dump(forensic_package, output_file, indent=4)
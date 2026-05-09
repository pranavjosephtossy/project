from Storage import evidence_storage
from main import analysis
import json
from collect_item import collect_item

def run_main():
        
      user_input=input("1 for synthetic,2 for preinstalled yt and 3 for custom")
      if user_input== "1":
            print("Not implemented yet")

      elif user_input=="2":
            with open("Offensive_content_reddit.json","r", encoding="utf-8") as f:
                  json_dump = json.load(f)
            
      elif user_input=="3":
            user_input_yt_title=input("Enter yt link")
            #calls collection module and gets back raw_json and log item
            collection()
            with open("youtube_collection_with_comments.json","r", encoding="utf-8") as f:
                  json_dump = json.load(f)

      else:
            print("Invalid input")

      for raw_item in json_dump:
            for comment in raw_item['comments']:

                  #i need a way to log each raw comment item has been collected
                  raw_json, collection_log = collect_item(comment)

                  #calls analysis passes raw_json_comment and gets analysis_json and log item
                  analysis_json, analysis_log = analysis(comment)
                  
                  # calls storage passes both jsons and logs
                  forensic_package=evidence_storage(comment, analysis_json, collection_log, analysis_log)

                  output_file = f"forensic__package{raw_item['video_id']}.json"
                  print(json.dumps(forensic_package, indent=4))   # dumps with an "s" returns a string
                  with open(output_file, "w", encoding="utf-8") as outfile:
                        json.dump(forensic_package, outfile, indent=4)   # outfile, not output_file
run_main()
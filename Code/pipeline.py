from Storage import evidence_storage
from main import analysis
import json
from collect_item import collect_item

def run_main():
        
      user_input=input("1 for synthetic,2 for preinstalled yt and 3 for custom")
      if user_input=="1":
            with open("positivetest.json","r",encoding="utf-8") as f:
                  json_dump = json.load(f)

      elif user_input=="2":
            with open("youtube_collection_with_comments.json","r",encoding="utf-8") as f:
                  json_dump = json.load(f)
            
      elif user_input=="3":
            user_input_yt_title=input("Enter yt link")
            #calls collection module and gets back raw_json and log item
            collection()
            with open("youtube_collection_with_comments.json","r",encoding="utf-8") as f:
                  json_dump = json.load(f)

      else:
            print("Invalid input")

      all_packages =[]

      for raw_item in json_dump:
            for comment in raw_item['comments']:

                  #i need a way to log each raw comment item has been collected
                  raw_json, collection_log = collect_item(comment)

                  #calls analysis passes raw_json_comment and gets analysis_json and log item
                  analysis_json, analysis_log = analysis(comment)
                  
                  # calls storage passes both jsons and logs
                  forensic_package=evidence_storage(comment, analysis_json, collection_log, analysis_log)

                  all_packages.append(forensic_package)
      
      print(json.dumps(all_packages, indent=4))
run_main()
from Storage import evidence_storage
from main import analysis
import json
from collect_item import collect_item

def run_main():
        
      print("1 for synthetic,2 for preinstalled yt and 3 for custom")
      user_input=input("Enter: ")
      print("")
      if user_input=="1":
            filename="positivetest.json"
            print("Will use synthetic dataset for analysis")

      elif user_input=="2":
            filename="youtube_collection_with_comments.json"
            print("Will use previously queried YouTube API JSON of Slushy Noobz for analysis")
                         
      elif user_input=="3":
            user_input_yt_title=input("Enter yt link")
            #calls collection module, passes in the yt link and gets back raw_json and log item
            #collection()
            #have not integreted this function yet
            #YoutubeTest2()
            
      else:
            print("Invalid input")
      
      with open(filename,"r",encoding="utf-8") as f:
            json_dump = json.load(f)
            
      #itterates through each video in json_dump if there are more than one video in json      
      for raw_item in json_dump:

            vidID=raw_item["video_id"]
            output_file=f"{vidID}_forensic_package_output.json"

            #forensic package for each video is appened to this array and then saved as json
            all_packages =[]

            #itterates through each comment
            for comment in raw_item['comments']:

                  #seperate and log each raw comment item has been collected, will return the comment untouched
                  raw_json, collection_log = collect_item(comment)

                  #calls analysis aand passes raw json comment and gets analysis_json and log item
                  analysis_json, analysis_log = analysis(comment)
                  
                  # calls storage passes both jsons and logs and gets the forensic package
                  forensic_package=evidence_storage(comment, analysis_json, collection_log, analysis_log)

                  all_packages.append(forensic_package)

            #saves the forensic package as .json file
            with open(output_file,"w",encoding="utf-8") as out:
                  json.dump(all_packages, out, indent=4)
            print(f"Saved forensic output in --> {output_file}")
run_main()
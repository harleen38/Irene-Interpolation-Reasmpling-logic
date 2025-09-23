import requests
import os



vehicle_ids = [860153738906566656]


Start_TS = str(int(1755887400000))
End_TS   = str(int(1758652199000))


for vehicle_id in vehicle_ids:
    
    
    # base_path is the ooutput path change this
    base_path = "/UPS_download_interpolation/Aug23_to_Sept_sample_file/"
    
    local_filename = base_path + str(vehicle_id) + "/" + str(vehicle_id) +  "_check_" +  Start_TS + "_" + End_TS + ".json"

    
    URL = 'https://old-data-downloader.intangles-aws-us-east-1.intangles.us/download/' + str(vehicle_id) +  "/" +Start_TS + "/" + End_TS 
    # URL =   'http://data-download.intangles.com:1883/download/' + str(vehicle_id) +  "/" + str(Start_TS) + "/" + str(End_TS) 

    r = requests.get(URL,stream=True)

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                print("Writing...................................")
                f.write(chunk) 
    
    print("*************************** vehicle-id *************", vehicle_id, "*********** download is completed *********************** ")   
    
           
            
            
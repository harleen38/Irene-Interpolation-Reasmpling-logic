- *** Following repo contains some basic scripts for performing download and interpolation of Irene data, I tried to name the scripts as per the intent they fulfill please feel free to rename them ***

- July_to_Aug23_data_download.py - is the script to download the data between July to Aug 23rd 2025 from the cloud (One sample file downloaded is present in July_to_Aug23_sample_file), further this json can also be converted to csv, its logic is present in July_to_Aug23_json_to_csv.ipynb


- Aug23_to_Sept_data_download.py is the script for getting the most recent data From Aug 23rd to Sept 2025 (Note since the data migration si still the work in progress) data dowanloded is between Sept 2nd to Sept 5tone sample file downloaded is present in Aug23_to_Sept_sample_file,   further this json can also be converted to csv, its logic is present in Aug23_to_sept_data_json_to_csv.ipynb

- The data downloaded between July to Aug 23 is the raw data (non-uniformly sanpled signal) with no interpolation performed - linear_interpolation_resampling_on_data.ipynb has the logic which performs the linear interpolation on this non-uniform data, kindly use the same logic and modify the diagnostic parameters as per your algorithm requirement

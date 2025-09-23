import requests
import json
import time
import os

BASE_URL = "https://apis.intangles-aws-us-east-1.intangles.us/idevice/logsV2"  # Replace with your API endpoint
PAGE_SIZE = 20000000

TYPE_MAPPING = {
    "StatusData": "status_data",
    "FaultData": "fault_data",
}


def generate_unique_filename(imei, log_type):
    timestamp = int(time.time() * 1000)
    return f"{imei}_{timestamp}.json"


def fetch_all_logs(imei, token, from_ts, until_ts, log_type=None):
    all_logs = []
    last_evaluated_key = None

    try:
        while True:
            params = {
                "psize": PAGE_SIZE,
                "token": token,
                "from": from_ts,
                "until": until_ts,
            }

            if log_type and log_type in TYPE_MAPPING:
                params["types"] = TYPE_MAPPING[log_type]

            if last_evaluated_key:
                params["last_t"] = last_evaluated_key

            url = f"{BASE_URL}/{imei}"
            print("this is the url: ", url)
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            

            logs = data.get("logs", [])

            if (
                last_evaluated_key is not None
                and data.get("last_evaluated_key", {}).get("t")
                and last_evaluated_key == data["last_evaluated_key"]["t"]
            ):
                last_evaluated_key = None
            else:
                last_evaluated_key = data.get("last_evaluated_key", {}).get("t")

            if logs and last_evaluated_key:
                for log in logs:
                    if "m" in log and log["m"]:
                        parsed_data = log["m"].strip()
                        all_logs.append(parsed_data)
                   

            if not last_evaluated_key:
                break

    except Exception as e:
        print(f"Error fetching logs for IMEI {imei}: {e}")

    return all_logs


def save_logs_to_file(imei, token, from_ts, until_ts, log_type=None):
    logs = fetch_all_logs(imei, token, from_ts, until_ts, log_type)
    if not logs:
        print("No logs found")
        return
    # this is the output path change this
    filename = "/UPS_download_interpolation/July_to_Aug23_sample_file/" + generate_unique_filename(imei, log_type or "logs")
    with open(filename, "w") as f:
        json.dump(logs, f, indent=2)
    print(f"Logs saved to {filename}")




imei_ls = ['b1CC7C'] # device-id has to be passed over here

count = 0
for imei in imei_ls:

    from_ts = 1751308200000
    until_ts = int(time.time() * 1000)
    log_type = "StatusData"

    token = "8hWSP7dGhr6a-mcVIDLPKKJdxKuyxXDjHa0AYta_MTnalCbF3nETamY6s-1TO0v1"
    
    save_logs_to_file(imei, token, from_ts, until_ts, log_type)
     
    
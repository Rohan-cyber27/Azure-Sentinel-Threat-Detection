import re
import requests
import csv

# Function to extract IP address from a line in the log
def extract_ip(line):
    match = re.search(r"Source Network Address:\s+([0-9.]+)", line)
    if match:
        return match.group(1)
    return None

# Function to get location information from an IP address using ip-api.com
def get_location(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        return {
            "IP Address": ip_address,
            "Country": data.get("country", "Unknown"),
            "Latitude": data.get("lat", "Unknown"),
            "Longitude": data.get("lon", "Unknown")
        }
    except Exception as e:
        return {"Error": str(e)}

# Main function to read the log file and process each line
def process_log_file(file_path, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ["IP Address", "Country", "Latitude", "Longitude"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with open(file_path, 'r') as file:
            for line in file:
                ip_address = extract_ip(line)
                if ip_address:
                    location_info = get_location(ip_address)
                    writer.writerow(location_info)

# Path to the log file
log_file_path = 'C:/Users/rohan/OneDrive/Desktop/python/file/rrr.csv'

# Path to the output CSV file
output_file_path = 'C:/Users/rohan/OneDrive/Desktop/python/file/output.csv'

# Process the log file and save the results to a new file
process_log_file(log_file_path, output_file_path)
print(f"Results saved to {output_file_path}")

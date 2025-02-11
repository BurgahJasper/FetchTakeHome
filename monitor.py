import requests
import yaml
import time
import sys
from collections import defaultdict
from urllib.parse import urlparse

def load_config(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def check_endpoint(endpoint):
    url = endpoint["url"]
    method = endpoint.get("method", "GET").upper()
    headers = endpoint.get("headers", {})
    body = endpoint.get("body", None)
    
    start_time = time.time()
    try:
        response = requests.request(method, url, headers=headers, json=body if body else None, timeout=5)
        latency = (time.time() - start_time) * 1000  # Convert to ms
        
        if 200 <= response.status_code < 300 and latency < 500:
            return True
    except requests.RequestException:
        pass
    
    return False

def main(file_path):
    config = load_config(file_path)
    domain_stats = defaultdict(lambda: {"up": 0, "total": 0})
    
    try:
        while True:
            for endpoint in config:
                domain = urlparse(endpoint["url"]).netloc
                is_up = check_endpoint(endpoint)
                
                domain_stats[domain]["total"] += 1
                if is_up:
                    domain_stats[domain]["up"] += 1
            
            for domain, stats in domain_stats.items():
                availability = round(100 * stats["up"] / stats["total"])
                print(f"{domain} has {availability}% availability percentage")
            
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monitor.py <config_file_path>")
        sys.exit(1)
    
    main(sys.argv[1])

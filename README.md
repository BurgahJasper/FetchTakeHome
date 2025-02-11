# HTTP Endpoint Monitor

This Python program is designed to monitor the health of HTTP endpoints defined in a YAML configuration file. It periodically checks each endpoint every 15 seconds and logs the availability percentage for each domain

## Prerequisites

Ensure Python is installed on your system. This script requires Python 3.6 or newer

## Installation

Before running the program, you need to install the required dependencies. The script uses the `requests` and `PyYAML` libraries, which may not be installed in your current Python environment

### Installing dependencies

Depending on your operating system, run the following command to install the necessary packages - 

OSX/Linux Python 2
```sh
sudo pip install requests pyyaml
```

OSX/Linux Python 3
```sh
sudo pip3 install requests pyyaml
```

Windows Without Python 3
```sh
pip install requests pyyaml
```

Windows With Python 3
```sh
pip3 install requests pyyaml
```

## Usage

Run the script with the path to your YAML configuration file as an argument:

```sh
python monitor.py <config_file_path>
```

### Example

```sh
python monitor.py endpoints.yaml
```

## Debugging

If there are doubts or you want to check the status, latency, or if the call is UP or DOWN, place this line of code at line 42 before the for loop

```sh
print(f"Checked {endpoint['name']} ({domain}) - Status: {status_code}, Latency: {latency:.2f} ms, {'UP' if is_up else 'DOWN'}")
```

## Configuration File Format

The input configuration file must be in YAML format, containing a list of HTTP endpoints with their properties. Example:

```yaml
- name: Fetch Index Page
  url: https://fetch.com/
  method: GET
  headers:
    user-agent: fetch-synthetic-monitor
- name: Fetch Careers Page
  url: https://fetch.com/careers
  method: GET
  headers:
    user-agent: fetch-synthetic-monitor
```

## Stopping the Program

To stop monitoring, press `CTRL + C` in the terminal.

import os
import platform
import argparse
import json
import requests

def do_ping_sweep(ip_addr, num_of_host):
    ip_parts = ip_addr.split(".")

    network_ip = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + "."
    scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)

    os_type = platform.system()

    if os_type == "Windows":
        response = os.popen(f"ping -n 1 {scanned_ip}")
    else:
        # os_type is "Darwin" or "Linux"
        response = os.popen(f"ping -c 1 {scanned_ip}")

    alive = "Destination Host Unreachable"

    for line in response.readlines():
        if line.upper().count("TTL"):
            alive = "Destination Host Accessible"
            break

    print(f"[#] Result of scanning: {scanned_ip} [#]\n{alive}", end = "\n\n")

def send_http_request(url, method, headers = None, payload = None):
    headers_dict = {}

    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method in ("GET", "POST"):
        if method == "GET":
            response = requests.get(url, headers = headers_dict, timeout = (3, 5))
        else:
            # method is "POST"
            response = requests.post(url, headers = headers_dict, data = payload, timeout = (3, 5))

        print(
            f"[#] Response status code: {response.status_code}\n"
            f"[#] Response headers: {json.dumps(dict(response.headers), indent = 4, sort_keys = True)}\n"
            f"[#] Response content:\n {response.text}"
        )

parser = argparse.ArgumentParser(description = "Network scanner")
parser.add_argument("task", choices = ["scan", "sendhttp"], help = "Network scan or send HTTP request")

# scan
parser.add_argument("-i", "--ip_address", type = str, default = "192.168.1.0", help = "IP address to scan")
parser.add_argument("-n", "--num_of_hosts", type = int, default = 1, help = "Number of hosts")

# sendhttp
parser.add_argument("-t", "--target", type = str, default = "https://google.com", help = "Where to send HTTP request")
parser.add_argument("-m", "--method", type = str, default = "GET", nargs = "*", help = "GET or POST method (if POST, fill payload after space)")
parser.add_argument("-hd", "--headers", type = str, nargs = "*", help = "Names:Values separated by space")

args = parser.parse_args()

if args.task == "scan":
    for host_num in range(args.num_of_hosts):
        do_ping_sweep(args.ip_address, host_num)
elif args.task == "sendhttp":
    send_http_request(args.target, args.method[0], args.headers, " ".join(args.method[1:]))

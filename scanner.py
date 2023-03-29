import os
import platform
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

def do_ping_sweep(ip_addr, num_of_hosts = 1):
    ip_parts = ip_addr.split(".")
    network_ip = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + "."

    scan_dict = {}

    for host_num in range(num_of_hosts):
        scanned_ip = network_ip + str(int(ip_parts[3]) + host_num)

        if platform.system() == "Windows":
            response = os.popen(f"ping -n 1 {scanned_ip}")
        else:
            # system is "Darwin" or "Linux"
            response = os.popen(f"ping -c 1 {scanned_ip}")

        alive = "Destination Host Unreachable"

        for line in response.readlines():
            if line.upper().count("TTL"):
                alive = "Destination Host Accessible"
                break

        print(f"[#] Result of scanning: {scanned_ip} [#]\n{alive}", end = "\n\n")
        scan_dict.update({scanned_ip : alive})

    return scan_dict

def send_http_request(url, method = "GET", headers = None, payload = None):
    headers_dict = {}

    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method in ("GET", "POST"):
        if method == "GET":
            result = requests.get(url, headers = headers_dict, timeout = (3, 5))
        else:
            # method is "POST"
            result = requests.post(url, headers = headers_dict, data = payload, timeout = (3, 5))

        print(
            f"[#] Response status code: {result.status_code}\n"
            f"[#] Response headers: {json.dumps(dict(result.headers), indent = 4, sort_keys = True)}\n"
            f"[#] Response content:\n {result.text}"
        )

        return {
            "Status" : result.status_code,
            "Headers" : result.headers,
            "Content" : result.text
        }

    return {}

class ProcessHandler(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/json")
        length = int(self.headers["Content-Length"])
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp

    def do_GET(self):
        temp = self.set_headers()
        payload = json.loads(temp)
        result = do_ping_sweep(payload["ip_address"], payload["num_of_hosts"])
        self.wfile.write(f"Result of scanning: {result}".encode())

    def do_POST(self):
        temp = self.set_headers()
        payload = json.loads(temp)
        response = send_http_request(payload["target"], payload["method"])
        self.wfile.write(f"HTTP response: {response}".encode())

httpd = HTTPServer(("0.0.0.0", 8081), ProcessHandler)
httpd.serve_forever()

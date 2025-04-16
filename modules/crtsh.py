import requests
import json

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=10)
        data = json.loads(res.text)
        subdomains = set()
        for cert in data:
            name = cert.get("name_value", "")
            if name and domain in name:
                for line in name.split("\n"):
                    if "*" not in line:
                        subdomains.add(line.strip())
        return sorted(subdomains)
    except Exception as e:
        return [f"[crt.sh error] {str(e)}"]

import os
import shodan

def get_shodan_data(_):
    api_key = os.getenv("SHODAN_API", "")
    if not api_key:
        return ["[Shodan] Missing SHODAN_API key"]

    api = shodan.Shodan(api_key)
    try:
        # Safe query that works on free tier
        results = api.search("port:80 country:UZ", limit=3)
        data = []
        for result in results["matches"]:
            ip = result.get("ip_str", "N/A")
            port = result.get("port", "N/A")
            org = result.get("org", "Unknown")
            data.append(f"{ip}:{port} – {org}")
        return data
    except Exception as e:
        return [f"[Shodan error] {str(e)}"]

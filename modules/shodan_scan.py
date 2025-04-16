import os
import shodan

def get_shodan_data(query):
    api_key = os.getenv("SHODAN_API", "")
    if not api_key:
        return ["[Shodan] SHODAN_API not set"]

    api = shodan.Shodan(api_key)
    try:
        results = api.search('org:"UNITEL"', limit=3)
        data = []
        for result in results['matches'][:3]:
            ip = result['ip_str']
            port = result.get('port', 'N/A')
            org = result.get('org', '')
            data.append(f"{ip}:{port} – {org}")
        return data
    except Exception as e:
        return [f"[Shodan error] {str(e)}"]

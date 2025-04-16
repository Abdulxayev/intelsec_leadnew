import requests

def get_cves(keywords=[]):
    url = "https://cve.circl.lu/api/last"
    try:
        res = requests.get(url, timeout=10).json()
        cve_list = []
        for cve in res[:30]:  # look at more in case of filtering
            if keywords:
                for kw in keywords:
                    if kw.lower() in str(cve).lower():
                        cve_list.append(f"{cve['id']} – {cve['summary'][:80]}")
                        break
            else:
                cve_list.append(f"{cve['id']} – {cve['summary'][:80]}")
        return cve_list
    except Exception as e:
        return [f"[CVE fetch error] {str(e)}"]

import subprocess

def get_subdomains(domain):
    try:
        result = subprocess.run(
            ["subfinder", "-silent", "-d", domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )
        subs = result.stdout.strip().split("\n")
        return list(filter(None, subs))[:20]  # limit to top 20
    except Exception as e:
        return [f"[subfinder error] {str(e)}"]

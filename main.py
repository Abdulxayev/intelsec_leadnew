import os
from telegram import Bot
from modules.crtsh import get_subdomains
#from modules.shodan_scan import get_shodan_data
from modules.cve import get_cves
#from modules.text_to_image import text_to_image

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

def build_report():
    subs = get_subdomains("beeline.uz")
   # shodan_info = get_shodan_data("beeline.uz")
    cves = get_cves()
    cve_block = "\n".join(cves[:10])



    report = f"🛡️ SecIntelBot Report\n📆 Date: Today\n\n"
    report += "1️⃣ Subdomains:\n" + "\n".join(subs[:5]) + "\n\n"
 #   report += "2️⃣ Shodan Exposures:\n" + "\n".join(shodan_info[:3]) + "\n\n"
    report += "3️⃣ Latest CVEs:\n```" + cve_block + "```\n\n"
    report += "✅ Auto-Posted by SecIntelBot"

    return report

def send_report():
    bot = Bot(token=bot_token)
    report = build_report()
    bot.send_message(chat_id=chat_id, text=report)

#    img = text_to_image(report)
#    with open(img, "rb") as photo:
 #       bot.send_photo(chat_id=chat_id, photo=photo)

if __name__ == "__main__":
    send_report()

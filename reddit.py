import requests
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Reddit Altin Yorum Botu)"
}

all_comments = []


POST_URLS = [
    "https://www.reddit.com/r/Yatirim/comments/1o1z2gz/%C5%9Fu_y%C3%BCkseli%C5%9Fte_alt%C4%B1n_almak_mant%C4%B1kl%C4%B1_m%C4%B1/",
    
   #ilgili post(yorrumları çekilecek)
]


def extract_comments(children):
    for item in children:
        if item.get("kind") != "t1":
            continue

        data = item["data"]
        all_comments.append({
            "author": data.get("author"),
            "comment": data.get("body"),
            "score": data.get("score"),
            "permalink": "https://www.reddit.com" + data.get("permalink", "")
        })

        replies = data.get("replies")
        if replies and isinstance(replies, dict):
            extract_comments(replies["data"]["children"])


for url in POST_URLS:
    json_url = url.rstrip("/") + "/.json"
    print(f"[+] Post indiriliyor: {json_url}")

    try:
        post_data = requests.get(json_url, headers=headers).json()
        comment_tree = post_data[1]["data"]["children"]
        extract_comments(comment_tree)
    except Exception as e:
        print(f"   Hata: {e}")

    time.sleep(1)

with open("reddit_yorumlari.json", "w", encoding="utf-8") as f:
    json.dump(all_comments, f, ensure_ascii=False, indent=4)

print(f"\nTOPLAM {len(all_comments)} YORUM KAYDEDİLDİ → reddit_yorumlari.json")

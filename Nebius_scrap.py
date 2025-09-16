import requests
from lxml import html
import json
import pandas as pd

def fetch_pricing_page(url: str) -> str:
    r = requests.get(url)
    r.raise_for_status()
    return r.content

def extract_json(content: bytes) -> dict:
    tree = html.fromstring(content)
    raw = tree.xpath('//script[@type="application/json"]/text()')[0]
    raw = raw.replace('\\u003cp\\u003e', '').replace('\\u003c/p\\u003e', '')
    return json.loads(raw)

def build_dataframe(data: dict) -> pd.DataFrame:
    rows = data['props']['pageProps']['pageContent']['blocks'][4]['table']['content'][1:]
    datalist = [{
        "Item": r[0],
        "vCPUs": r[1],
        "RAM(GB)": r[2],
        "Price per Hour": r[3]
    } for r in rows]
    return pd.DataFrame(datalist)

def main():
    url = "https://nebius.com/prices"
    content = fetch_pricing_page(url)
    json_data = extract_json(content)
    df = build_dataframe(json_data)
    df.to_excel("Nebius_Pricing.xlsx", index=False)

if __name__ == "__main__":
    main()

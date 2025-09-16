import requests
import pandas as pd

cookies = {
    'MUID': '2C2F66B4339B6C113A11758732006DE6',
    '_clck': 'n8jmts%7C2%7Cfuv%7C0%7C1923',
    '_uetvid': '01d865f013ab11f0afd63bae8807978e|plqgo3|1744029909055|4|1|bat.bing.com/p/insights/c/j',
    'MC1': 'GUID=98b2b425a1824d2681ee81a7e9833d7a&HASH=98b2&LV=202407&V=4&LU=1720158731123',
    'userInfo': '%7b%22guid%22%3a%2298b2b425a1824d2681ee81a7e9833d7a%22%7d',
    'ai_user': '+rzeHaqHMErfwG6CioggYP|2025-09-08T18:52:25.464Z',
    'MSFPC': 'GUID=98b2b425a1824d2681ee81a7e9833d7a&HASH=98b2&LV=202407&V=4&LU=1720158731123',
    'at_check': 'true',
    'mbox': 'session#359891a83cf34a5ca9e7ad70d8e81e51#1757359584|PC#359891a83cf34a5ca9e7ad70d8e81e51.41_0#1791537724',
    'ak_bmsc': '7FA33736E3CC67B69AEAFDD375C82AF1~000000000000000000000000000000~YAAQvP3UF1DN1EuZAQAAx/x1UR0iWAceuQbiokyb0dAKBnFfwyxTj1T9U+4VAVMg6o91EUV9cOM/cCUTmo4hF8X2V34e/rSd6LYvhytVW/eTULkhFsq9hGvbSbLHHDGSBzV2AMXHlQaLSaFi+/I6mWxI2I6ITGQDDINg4QZmCvEdiazbQP3s2mgVyVkCKkgG3YOzBxEMyWN3usev6QDMJc1fkWwT9RD2O0bO0Q2hEMpSy9gP1yklJQsDkqDyeGZWAjbGL1FIRQ6ol8hr8/FRJa9kab9qnDI0W24ROXM5XpfAXClFJn9dZdRmt0NL/LobVOZyk6GZSIUp+wbm5XDQYr/Mqvc7+eKbbNAt4s/dZkmz1ZqJKX/CXqIrMglRr46ZoWQyYoBOFITPaANvnoZCC5l3FiRBcoP28Pd8bgc=',
    'MSCC': 'NR',
    'MS0': 'c9bc2d3e16a6487baff6ad8eee6cf95d',
    'ai_session': 'pYQ/kqUeABkgEUIhF1VN6f|1758008311562|1758008865969',
    'bm_sv': '86B48DA09ADB789F733A185DDC3B5E27~YAAQvP3UF17y1EuZAQAAT+J+UR1LCela8L8YD+JLrAQQkV4in25fr4BP5Ze3onKOzMerwVzATl12mq4Ewe2FDfDiiGVe8LwSm0rXfxNj5r68qdxZsvuUQw5FfEeJ3cXWw399b0W5mk269iq/C2hnL06hnLjdhgN3rMFugNyDTzPpiTbz7c05eskPv4pblTqz59rcuI5QFqw2Tq8+RpuGJDqdmEdP42wn0rAecaljTwiJ5oirVMzYPVHUf8Tv3PZhfrcY~1',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Referer': 'https://azure.microsoft.com/en-us/pricing/details/virtual-machines/windows/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'X-Requested-With': 'FetchHttpRequest',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'MUID=2C2F66B4339B6C113A11758732006DE6; _clck=n8jmts%7C2%7Cfuv%7C0%7C1923; _uetvid=01d865f013ab11f0afd63bae8807978e|plqgo3|1744029909055|4|1|bat.bing.com/p/insights/c/j; MC1=GUID=98b2b425a1824d2681ee81a7e9833d7a&HASH=98b2&LV=202407&V=4&LU=1720158731123; userInfo=%7b%22guid%22%3a%2298b2b425a1824d2681ee81a7e9833d7a%22%7d; ai_user=+rzeHaqHMErfwG6CioggYP|2025-09-08T18:52:25.464Z; MSFPC=GUID=98b2b425a1824d2681ee81a7e9833d7a&HASH=98b2&LV=202407&V=4&LU=1720158731123; at_check=true; mbox=session#359891a83cf34a5ca9e7ad70d8e81e51#1757359584|PC#359891a83cf34a5ca9e7ad70d8e81e51.41_0#1791537724; ak_bmsc=7FA33736E3CC67B69AEAFDD375C82AF1~000000000000000000000000000000~YAAQvP3UF1DN1EuZAQAAx/x1UR0iWAceuQbiokyb0dAKBnFfwyxTj1T9U+4VAVMg6o91EUV9cOM/cCUTmo4hF8X2V34e/rSd6LYvhytVW/eTULkhFsq9hGvbSbLHHDGSBzV2AMXHlQaLSaFi+/I6mWxI2I6ITGQDDINg4QZmCvEdiazbQP3s2mgVyVkCKkgG3YOzBxEMyWN3usev6QDMJc1fkWwT9RD2O0bO0Q2hEMpSy9gP1yklJQsDkqDyeGZWAjbGL1FIRQ6ol8hr8/FRJa9kab9qnDI0W24ROXM5XpfAXClFJn9dZdRmt0NL/LobVOZyk6GZSIUp+wbm5XDQYr/Mqvc7+eKbbNAt4s/dZkmz1ZqJKX/CXqIrMglRr46ZoWQyYoBOFITPaANvnoZCC5l3FiRBcoP28Pd8bgc=; MSCC=NR; MS0=c9bc2d3e16a6487baff6ad8eee6cf95d; ai_session=pYQ/kqUeABkgEUIhF1VN6f|1758008311562|1758008865969; bm_sv=86B48DA09ADB789F733A185DDC3B5E27~YAAQvP3UF17y1EuZAQAAT+J+UR1LCela8L8YD+JLrAQQkV4in25fr4BP5Ze3onKOzMerwVzATl12mq4Ewe2FDfDiiGVe8LwSm0rXfxNj5r68qdxZsvuUQw5FfEeJ3cXWw399b0W5mk269iq/C2hnL06hnLjdhgN3rMFugNyDTzPpiTbz7c05eskPv4pblTqz59rcuI5QFqw2Tq8+RpuGJDqdmEdP42wn0rAecaljTwiJ5oirVMzYPVHUf8Tv3PZhfrcY~1',
}


def fetch_vm_data():

    params = {'culture': 'en-us', 'showLowPriorityOffers': 'false'}
    r = requests.get(
        'https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/details/windows/',
        params=params, cookies=cookies, headers=headers
    )
    return r.json()

def fetch_price_data():

    params = {'showLowPriorityOffers': 'false'}
    r = requests.get(
        'https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/windows/us-east/',
        params=params, cookies=cookies, headers=headers
    )
    return r.json()

def get_price(vm_name, price_json):
    return price_json.get(vm_name, {}).get('perhourhybridbenefit', 'NA')

def build_dataframe(vm_json, price_json):
    datalist = []
    for vm in vm_json['attributesByOffer'].keys():
        data = vm_json['attributesByOffer'][vm]
        datalist.append({
            "VM Name": data['instanceName'],
            "Series": data['series'],
            "Cores": data['cores'],
            "Category": data['category'],
            "RAM(GB)": data['ram'],
            "Tier": data['tier'],
            "Disk Size(GB)": data.get('diskSize', 'NA'),
            "Type": data['type'],
            "Price per Hour": get_price(vm, price_json),
        })
    return pd.DataFrame(datalist)

def main():
    vm_json = fetch_vm_data()
    price_json = fetch_price_data()
    df = build_dataframe(vm_json, price_json)
    df.to_excel('Azure_VM_Pricing.xlsx', index=False)

if __name__ == "__main__":
    main()

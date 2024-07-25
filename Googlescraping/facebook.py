import requests

cookies = {
    'datr': 'doiSZqEERPul36ZCbZTYqMIE',
    'dpr': '1.125',
    'ps_n': '1',
    'ps_l': '1',
    'wd': '786x780',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=doiSZqEERPul36ZCbZTYqMIE; dpr=1.125; ps_n=1; ps_l=1; wd=786x780',
    'origin': 'https://www.facebook.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=IN&q=%22typsybeauty.com%22&search_type=keyword_exact_phrase&media_type=all',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'AVq5nRIu868',
}

data = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': '2',
    '__hs': '19918.BP:DEFAULT.2.0..0.0',
    'dpr': '1',
    '__ccg': 'MODERATE',
    '__rev': '1014872399',
    '__s': 'cgpz8b:wr8jc4:j66jij',
    '__hsi': '7391424582286416414',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1Fx-ewSAxa68uxa0z8S2S2q0_EtxG4o3Bw5VCyU4a1Zg4K0KEswIwuo9oeUa8462mcw5Mx62G3i1ywa-2l0Fwqo31wp8kwyx2cwAxq1izXwrUcUjwVw9O7bK2S2W2K4EG1Mxu16wa-58G0iS2S3qazo11E2XU6-1FAwGw8O1pwr86C0nC1TwmU',
    '__csr': '',
    'lsd': 'AVq5nRIu868',
    'jazoest': '2865',
    '__spin_r': '1014872399',
    '__spin_b': 'trunk',
    '__spin_t': '1720950143',
    '__jssesw': '1',
}

response = requests.post(
    'https://www.facebook.com/ads/library/async/search_ads/?q=%22typsybeauty.com%22&v=f27b0f&session_id=f9aa19b4-6f2b-45d3-a675-4d96ecf65d02&count=30&active_status=all&ad_type=all&countries[0]=IN&media_type=all&search_type=keyword_exact_phrase',
    cookies=cookies,
    headers=headers,
    data=data,
)

import pdb;pdb.set_trace()

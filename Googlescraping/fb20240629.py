import requests

cookies = {
    'sb': 'LL0DZjE6P4wPROi6wVE5EkKm',
    'datr': 'LL0DZq5mQih5nbHX75G1AyE7',
    'c_user': '100002371207391',
    'ps_n': '1',
    'ps_l': '1',
    'dpr': '1.875',
    'xs': '42%3AVAXQGyjK73jhmg%3A2%3A1711521083%3A-1%3A5695%3A%3AAcUHUaUxOQ0Y4zfXpgI6H0u80vniGNUniHIh6i79SQ',
    'fr': '1Q9jzEKHytj78MQGA.AWVLsm41st0U7aADqeo-5ZnqYzA.Bmf5fB..AAA.0.0.Bmf5fB.AWWbwkjK7Ec',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1719638299727%2C%22v%22%3A1%7D',
    'wd': '552x468',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=LL0DZjE6P4wPROi6wVE5EkKm; datr=LL0DZq5mQih5nbHX75G1AyE7; c_user=100002371207391; ps_n=1; ps_l=1; dpr=1.875; xs=42%3AVAXQGyjK73jhmg%3A2%3A1711521083%3A-1%3A5695%3A%3AAcUHUaUxOQ0Y4zfXpgI6H0u80vniGNUniHIh6i79SQ; fr=1Q9jzEKHytj78MQGA.AWVLsm41st0U7aADqeo-5ZnqYzA.Bmf5fB..AAA.0.0.Bmf5fB.AWWbwkjK7Ec; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1719638299727%2C%22v%22%3A1%7D; wd=552x468',
    'origin': 'https://www.facebook.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=IN&q=%22typsybeauty.com%22&search_type=keyword_exact_phrase&media_type=all',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.114", "Google Chrome";v="126.0.6478.114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'gDPlOcwrfZW3DygQPBwe2u',
}

data = {
    '__aaid': '0',
    '__user': '100002371207391',
    '__a': '1',
    '__req': '2',
    '__hs': '19903.BP:DEFAULT.2.0..0.0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1014576526',
    '__s': 'xj42sy:3eyii6:fd5k7c',
    '__hsi': '7385794417871626180',
    '__dyn': '7xe6Eiw_K9zo5ObwKBAgc9o2exu13wqovzEdF8ixy7Eiw8O3K2q0_EtxG4o3Bw5VCyU4a1Zg4K0KEswIwuo9oeUa8462m0nS4oaEd86a0Rk2C0iK1Axi2a48O2i5E6aU6-3e4Ueo2sxOXwJwKwHxaaws8nwhE34yE1bobodEGdw46wbLwrU6Ci2G0z85C1Iwqo1uo7u1rw',
    '__csr': '',
    'fb_dtsg': 'NAcM_zbOjHjynRYBPXvC46gpSSgBWRpUKAZ8N0dDXMPY9OllxsbWMHQ:42:1711521083',
    'jazoest': '25483',
    'lsd': 'gDPlOcwrfZW3DygQPBwe2u',
    '__spin_r': '1014576526',
    '__spin_b': 'trunk',
    '__spin_t': '1719639268',
}

response = requests.post(
    'https://www.facebook.com/ads/library/async/search_ads/?q=%22typsybeauty.com%22&v=f27b0f&session_id=79b42aec-ab91-4ef9-95a9-61b3981031b9&count=30&active_status=all&ad_type=all&countries[0]=IN&media_type=all&search_type=keyword_exact_phrase',
    #cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
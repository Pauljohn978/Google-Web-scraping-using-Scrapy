import scrapy
from pathlib import Path
import json
import time
import logging

class QuotesSpider(scrapy.Spider):
    name = "facebook_spider"

    def __init__(self, productname, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.productName = productname
        self.path = r"D:\gradcommerce.com\Output ads"
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
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
        self.cookies = {
            'datr': 'doiSZqEERPul36ZCbZTYqMIE',
            'dpr': '1.125',
            'ps_n': '1',
            'ps_l': '1',
            'wd': '786x780',
        }
        self.data = {
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
        logging.info(f"Initialized spider with product name: {self.productName}")

    def start_requests(self):
        url = f'https://www.facebook.com/ads/library/async/search_ads/?q={self.productName}&v=f27b0f&session_id=f9aa19b4-6f2b-45d3-a675-4d96ecf65d02&count=100&active_status=all&ad_type=all&countries[0]=IN&media_type=all&search_type=keyword_exact_phrase'
        logging.info(f"Starting requests to {url}")
        yield scrapy.FormRequest(url, self.parse, headers=self.headers, formdata=self.data, method="POST", cookies=self.cookies, meta={"url": url, "productname": self.productName})

    def parse(self, response):
        logging.info(f"Parsing response from {response.url}")
        sel = scrapy.Selector(response)
        print(response)
        url = response.meta.get("url")
        productname = response.meta.get("productname")
        rawdata_response = "".join(sel.xpath('//text()').extract()).strip("for (;;);")
        json_response = json.loads(rawdata_response).get('payload', {})
        total_records = json_response.get("totalCount")
        logging.info(f"Total records: {total_records}")

        # Save the fetched data
        for raw_data in json_response['results']:
            for data in raw_data:
                logging.info(f"Processing adArchiveID: {data.get('adArchiveID')}")
                file_name_path = f"{self.path}\\{self.productName}_{data.get('adArchiveID')}.json"
                with open(file_name_path, 'w', encoding='utf-8') as save_file:
                    json.dump(data, save_file, indent=4)

        # Check if we need to continue paginating
        is_result_complete = json_response.get("isResultComplete", True)
        if not is_result_complete:
            forward_cursor = json_response.get("forwardCursor")
            collation_token = json_response.get("collationToken")
            if forward_cursor and collation_token:
                logging.info(f"forward_cursor={forward_cursor} -- collation_token={collation_token}")
                time.sleep(5)  # Delay to prevent rate limiting
                paginated_url = url
                if "forward_cursor" not in url:
                    paginated_url = f'{url}&forward_cursor={forward_cursor}&collation_token={collation_token}'
                else:
                    import re
                    paginated_url = re.sub(r"&forward_cursor=[^&]*", f"&forward_cursor={forward_cursor}", url)
                    paginated_url = re.sub(r"&collation_token=[^&]*", f"&collation_token={collation_token}", paginated_url)
                yield scrapy.FormRequest(paginated_url, self.parse, headers=self.headers, formdata=self.data, method="POST", cookies=self.cookies, meta={"url": url, "productname": self.productName})
# use  scrapy crawl facebook_spider -a productname="typsybeauty.com"
import urllib3
import certifi
http = urllib3.PoolManager(ca_certs=certifi.where())
resp = http.request(
     'POST',
     'https://app.i2crm.ru/api_v1/whatsapp/start?token=17db3bf8617cc5e99590e5a94fd1632a',
     body='',
     headers={'Content-Type': 'application/json',
                'Accept-Language': 'ru,en;q=0.9,en-US;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',})
print(resp.data)

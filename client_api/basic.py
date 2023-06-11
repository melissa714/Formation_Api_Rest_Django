import requests 

endpoint = "http://httpbin.org/anything"
response=requests.get(endpoint, data={'bonjour':'hello'})
print(response.text)

#HTTP RESQUEST --> HTML 
# REST API HTTP ---> JSON JAVASCRIPT OBJECT NOTATION 

{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-648643f0-3ca07e316daebfa74398fdcd'}, 'json': None, 'method': 'GET', 'origin': '160.120.204.150', 'url': 'http://httpbin.org/anything'}


{
  "args": {}, 

  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-6486442c-0daab7564cdd09fd3cc57336"
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "160.120.204.150", 
  "url": "http://httpbin.org/anything"
}
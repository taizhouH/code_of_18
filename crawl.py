import urllib.request
url = "http://www.bxquge.com/3_3619/10826.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
             (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read()
html = html.decode("utf-8")
print(html)
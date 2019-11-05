import urllib as url
import webbrowser as web
import time

url="https://gzkjxx.30edu.com.cn/Article/5d31e83e-1b88-44ad-b30c-f1c4a25a4910.shtml"

i=1
while i<30:
    web.open_new_tab(url)
    time.sleep(0.5)
    i=i+1

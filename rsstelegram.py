import feedparser
import datetime
import requests
import json
import time
import os.path
import urllib.parse

TELEGRAM_SENDMESSAGE_URL = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=%s&text=%s"
HTML_HREF = "<a href=\"%s\">%s</a>"
PARSE_MODE = ['Markdown', 'html']
CACHE_PATH = "cache"

KEY_CACHE_URLS = 'urls'
KEY_FEED_LINK = 'link'
KEY_FEED_TITLE = 'title'

class Rss2Telegram:

    def __init__(self, urls, token, channel, parse_mode = PARSE_MODE[1], cache_path = CACHE_PATH):
        self.urls = urls
        self.token = token
        self.channel = channel
        self.parse_mode = parse_mode
        self.cache_path = cache_path

    def parse_send_message(self, feeds):
        response_report = []
        cache = None
        if os.path.isfile(self.cache_path):
            cache_file = open(self.cache_path, "r")
            cache = json.loads(cache_file.read())
        else:
            cache = json.loads("{\"urls\" : []}")

        for feed in feeds:
            for entry in feed:
                if (entry[KEY_FEED_LINK] not in cache[KEY_CACHE_URLS]):
                    text = HTML_HREF%(entry[KEY_FEED_LINK],urllib.parse.quote(entry[KEY_FEED_TITLE]))
                    send_text = TELEGRAM_SENDMESSAGE_URL%(self.token, self.channel, self.parse_mode, text)
                    response = requests.get(send_text)
                    resp_json = response.json()
                    if (resp_json['ok'] is True):
                        cache[KEY_CACHE_URLS].append(entry['link'])
                    else:
                        #add url and title to error report
                        resp_json['urlFeed'] = entry[KEY_FEED_LINK]
                        resp_json['titleFeed'] = entry[KEY_FEED_TITLE]
                    response_report.append(resp_json)
                    time.sleep(1)

        cache_file = open(self.cache_path, "w")
        cache_file.write(json.dumps(cache))
        cache_file.close()
        return response_report

    def run_fetch(self):
        feeds = [feedparser.parse(url)['entries'] for url in self.urls]
        return self.parse_send_message(feeds)

#call
#run_fetch()
#from your python script

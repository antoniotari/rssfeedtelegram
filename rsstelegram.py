import feedparser
#import schedule
import requests
import json
import time

CD_FEED = 'https://canadiandimension.com/feeds/articles'
VICE_FEED = 'https://www.vice.com/en/rss?locale=en_ca'
VOX_FEED = 'https://www.vox.com/rss/index.xml'
CBC_FEED = 'https://www.cbc.ca/cmlink/rss-canada'
GW_FEED = 'https://www.guitarworld.com/feeds/all'
METAL_INJECTION_FEED = 'http://feeds.feedburner.com/metalinjection'

TELEGRAM_CHANNEL_MUSIC = '@musicguitarnews'
TELEGRAM_BOT_TOKEN_MUSIC = '1567491461:AAFa6sWr9KXnqJ_ufBabJVNyS7Rq1Z50UCA'
TELEGRAM_CHANNEL_NEWS = '@canadanewschannel'
TELEGRAM_BOT_TOKEN_NEWS = '1518827417:AAEhEI-Ux9gue0Y85ADqhF2DCfsbzxiUk0I'

PARSE_MODE = ['Markdown', 'html']

urls_music = [METAL_INJECTION_FEED, GW_FEED]
urls_news = [CD_FEED, VOX_FEED, CBC_FEED]

# grab the rss feeds
feeds_music = [feedparser.parse(url)['entries'] for url in urls_music]
feeds_news = [feedparser.parse(url)['entries'] for url in urls_news]

cache_file = open("cache","r") 
cache = json.loads(cache_file.read())
#print(cache)

def parse_send_message(feeds, token, channel, parse_mode):
    for feed in feeds:
        for entry in feed:
            if (entry['link'] not in cache['urls']):
                text = "<a href=\"%s\">%s</a>"%(entry['link'],entry['title'])
                send_text = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=%s&text=%s"%(token, channel, parse_mode, text)
                #print(send_text)
                response = requests.get(send_text)
                #response_json = json.loads(response.json())
                if (response.json()['ok'] is True):
                    cache['urls'].append(entry['link'])
                time.sleep(1)

parse_send_message(feeds_music, TELEGRAM_BOT_TOKEN_MUSIC, TELEGRAM_CHANNEL_MUSIC, PARSE_MODE[1])
parse_send_message(feeds_news, TELEGRAM_BOT_TOKEN_NEWS, TELEGRAM_CHANNEL_NEWS, PARSE_MODE[1])
 
cache_file = open("cache","w")
cache_file.write(json.dumps(cache))
cache_file.close()

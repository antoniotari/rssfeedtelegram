import feedparser
#import schedule
import datetime
import requests
import json
import time

CD_FEED = 'https://canadiandimension.com/feeds/articles'
VICE_FEED = 'https://www.vice.com/en/rss?locale=en_ca'
VOX_FEED = 'https://www.vox.com/rss/index.xml'
CBC_FEED = 'https://www.cbc.ca/cmlink/rss-canada'
GW_FEED = 'https://www.guitarworld.com/feeds/all'
METAL_INJECTION_FEED = 'http://feeds.feedburner.com/metalinjection'
PG_REVIEWS_FEED = "https://www.premierguitar.com/rss/2"
PG_RIG_FEED = "https://www.premierguitar.com/rss/5"
PG_LESSONS_FEED = 'https://www.premierguitar.com/rss/6'
PG_PROJECTS_FEED = 'https://www.premierguitar.com/rss/7'

TELEGRAM_CHANNEL_MUSIC = 'channel id here'
TELEGRAM_BOT_TOKEN_MUSIC = 'token here'
TELEGRAM_CHANNEL_NEWS = 'other channel id here'
TELEGRAM_BOT_TOKEN_NEWS = 'other token here'

PARSE_MODE = ['Markdown', 'html']

urls_music = [METAL_INJECTION_FEED, GW_FEED, PG_REVIEWS_FEED, PG_RIG_FEED, PG_LESSONS_FEED, PG_PROJECTS_FEED]
urls_news = [CD_FEED, VOX_FEED, CBC_FEED]

CACHE_PATH = "/home/antonio/feedFetcher/cache"

def parse_send_message(feeds, token, channel, parse_mode):
    cache_file = open(CACHE_PATH, "r")
    cache = json.loads(cache_file.read())
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
    cache_file = open(CACHE_PATH, "w")
    cache_file.write(json.dumps(cache))
    cache_file.close()

def runFetch():
    feeds_music = [feedparser.parse(url)['entries'] for url in urls_music]
    feeds_news = [feedparser.parse(url)['entries'] for url in urls_news]
    parse_send_message(feeds_music, TELEGRAM_BOT_TOKEN_MUSIC, TELEGRAM_CHANNEL_MUSIC, PARSE_MODE[1])
    #time.sleep(60)
    parse_send_message(feeds_news, TELEGRAM_BOT_TOKEN_NEWS, TELEGRAM_CHANNEL_NEWS, PARSE_MODE[1])
    #print('execution done')
    now = datetime.datetime.now()
    return str(now)

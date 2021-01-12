from rsstelegram import Rss2Telegram

CD_FEED = 'https://canadiandimension.com/feeds/articles'
VICE_FEED_CA = 'https://www.vice.com/en/rss?locale=en_ca'
VICE_FEED = 'https://www.vice.com/en/rss?locale=en_us'
VOX_FEED = 'https://www.vox.com/rss/index.xml'
CBC_FEED = 'https://www.cbc.ca/cmlink/rss-canada'
GW_FEED = 'https://www.guitarworld.com/feeds/all'
METAL_INJECTION_FEED = 'http://feeds.feedburner.com/metalinjection'
PG_REVIEWS_FEED = "https://www.premierguitar.com/rss/2"
PG_RIG_FEED = "https://www.premierguitar.com/rss/5"
PG_LESSONS_FEED = 'https://www.premierguitar.com/rss/6'
PG_PROJECTS_FEED = 'https://www.premierguitar.com/rss/7'
ALPHAECHOES_YOUTUBE_FEED = 'https://www.youtube.com/feeds/videos.xml?channel_id=UClpP4ZP3tYPaiWv4LnPqT5g'
ROCKFUJIYAMA_YOUTUBE_FEED = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCLmF8nkHDUap8ztsGnROWqg'
VICE_YOUTUBE_FEED = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCn8zNIfYAQNdrFRrr8oibKw'
VOX_YOUTUBE_FEED = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCLXo7UDZvByw2ixzpQCufnA'

TELEGRAM_CHANNEL_MUSIC = '@'
TELEGRAM_BOT_TOKEN_MUSIC = ':'
TELEGRAM_CHANNEL_NEWS = '@'
TELEGRAM_BOT_TOKEN_NEWS = ':-'
TELEGRAM_TEST_CHANNEL = '@'

urls_music = [METAL_INJECTION_FEED, GW_FEED, PG_REVIEWS_FEED, PG_RIG_FEED, PG_LESSONS_FEED, PG_PROJECTS_FEED, ALPHAECHOES_YOUTUBE_FEED, ROCKFUJIYAMA_YOUTUBE_FEED]
urls_news = [VICE_FEED, CD_FEED, VOX_FEED, CBC_FEED, VICE_FEED_CA, VOX_YOUTUBE_FEED, VICE_YOUTUBE_FEED]

CACHE_PATH = "/cache"

def runFetch():
    rssMusic = Rss2Telegram(urls_music, TELEGRAM_BOT_TOKEN_MUSIC, TELEGRAM_CHANNEL_MUSIC, cache_path = CACHE_PATH)
    rssNews = Rss2Telegram(urls_news, TELEGRAM_BOT_TOKEN_NEWS, TELEGRAM_CHANNEL_NEWS, cache_path = CACHE_PATH)
    report_music = rssMusic.run_fetch()
    report_news = rssNews.run_fetch()
    return report_music + report_news

'''
use this function for testing
'''
def runFetchTest():
    rssy = Rss2Telegram([VOX_YOUTUBE_FEED, VICE_YOUTUBE_FEED], TELEGRAM_BOT_TOKEN_NEWS, TELEGRAM_TEST_CHANNEL, cache_path = 'cache')
    report = rssy.run_fetch()
    return report

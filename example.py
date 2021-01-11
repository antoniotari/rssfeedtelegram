from feedfetch import Rss2Telegram

CD_FEED = 'https://canadiandimension.com/feeds/articles'
VICE_FEED_CA = 'https://www.vice.com/en/rss?locale=en_ca'
VICE_FEED = 'https://www.vice.com/en/rss?locale=en_us'
VOX_FEED = 'https://www.vox.com/rss/index.xml'
CBC_FEED = 'https://www.cbc.ca/cmlink/rss-canada'
GW_FEED = 'https://www.guitarworld.com/feeds/all'
METAL_INJECTION_FEED = 'http://feeds.feedburner.com/metalinjection'

TELEGRAM_CHANNEL_MUSIC = 'your channel id'
TELEGRAM_BOT_TOKEN_MUSIC = 'your token'
TELEGRAM_CHANNEL_NEWS = 'second channel id'
TELEGRAM_BOT_TOKEN_NEWS = 'second token'

urls_music = [METAL_INJECTION_FEED, GW_FEED]
urls_news = [VICE_FEED, CD_FEED, VOX_FEED, CBC_FEED, VICE_FEED_CA]

CACHE_PATH = "/home/antonio/rsstel_cache"

rssMusic = Rss2Telegram(urls_music, TELEGRAM_BOT_TOKEN_MUSIC, TELEGRAM_CHANNEL_MUSIC, cache_path = CACHE_PATH)
rssNews = Rss2Telegram(urls_news, TELEGRAM_BOT_TOKEN_NEWS, TELEGRAM_CHANNEL_NEWS, cache_path = CACHE_PATH)
report_music = rssMusic.run_fetch()
report_news = rssNews.run_fetch()
print (report_music + report_news)
    

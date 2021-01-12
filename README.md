files:
feedfetch.py - library file, contains the class with methods to fetch rss feed and send them to telegram
fetchloop.py - [temporary, replace with daemon] an infinite loop that will fetch rss feed at given intervals
fetchscript.py - a script to fetch rss feed and send it to telegram, must include it in your own script and call runFetch()
fetchscript-test.py - executes fetch and sends it to test telegram channel


# build a 'client' that will cache a URL

# first request: go out to the internet, get the web page
# second request: return from cache

# how to implement using a hash table aka a dictionary?
# - what are our keys? URL!
# - what are our values? web page data!

import urllib.request

cache = {}
url = 'https://www.google.com'
# given a url, check if it's in the cache

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.time_fetched = datetime.datetime.now().timestamp()



def fetch_web_page(url):
    stale_data = True
    if url in cache:
        time_now = datetime.datetime.now().timestamp()
        print('getting from cache')
        cache_entry = cache[url]
        
        if time_now - cache_entry.time_fetched < 10: 
            page = cache_entry.data
            stale_data = False

    elif stale_data:
        print('getting from the internet')
        # otherwise, send out a request to get the web page
        response = urllib.request.urlopen(url)
        data = response.read()
        response.close()

        # and put the result in our cache
        cache_entry = CacheEntry(data)
        cache[url] = cache_entry
        page = cache[url]
    
    return page

page = fetch_web_page(url)
print(page)

also_page = fetch_web_page(url)

# one issue: memory usage, lots of URLs will fill memory up 
## if the page isn't requested in a while, delete
## LRU cache (least recently used)
## use time to delete really old data

# what if the page changes?
## store time, and if data is stale, re-fetch
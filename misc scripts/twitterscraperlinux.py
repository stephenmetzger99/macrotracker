# author: Stephen Metzger
# purpose: takes a list of twitter users from .txt file and scrapes their
#          twitter accounts for recent tweets and stores them
#          in a dictionary, to then be dumped to a json file


import time
import json
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
# disables chrome window & runs in background
options.add_argument("headless")
#windows path:
#browser = webdriver.Chrome(options=options, executable_path="chromedriver.exe", )

#linux path:
browser = webdriver.Chrome(options=options, executable_path="/usr/lib/chromium-browser/chromedriver", )


NUM_OF_TWEETS_PER_USER = 2;

query = []
data = []
with open("twitterusers.txt") as twitter_username_file:
    for line in twitter_username_file:
        query = line
          
       
        base_url = u'https://twitter.com/'

        url = base_url + query
        browser.get(url)
        body = browser.find_element_by_tag_name('body')
        tweets = browser.find_elements_by_class_name('tweet-text')

        print("retrieved" , NUM_OF_TWEETS_PER_USER , "tweet(s) from @" + query)


        #iterate through a set number of tweets per user and append to a dictionary
        
        for i in range(NUM_OF_TWEETS_PER_USER):
            data.append(dict([("username", query),("tweet", tweets[i].text)]))
      
#close chrome driver and chromium windows    
browser.quit()

#write py dictionary data to tweet_data.json
with open("tweet_data.json", "w") as write_file:
    write_file.write("tweet_data =")
    json.dump(data, write_file, indent = 4)


datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

timestamp = datetime.datetime.now()


log_file = open("log.txt", "w")
log_file.write("Last twiter Update: %s" % timestamp)
print("Updated log file @ %s" % timestamp)
log_file.close()

#log_file.close()
twitter_username_file.close()






  
    

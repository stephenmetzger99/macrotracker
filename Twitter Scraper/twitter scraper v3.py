# author: Stephen Metzger
# purpose: takes a list of twitter users from .txt file and scrapes their
#          twitter accounts for recent tweets and stores them
#          in a dictionary, to then be dumped to a json file


import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("headless")
browser = webdriver.Chrome(options=options)

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

        #print("@" + query + " on Twitter: \"" + tweets[0].text + "\"")
        #print("@" + query + " on Twitter: \"" + tweets[1].text + "\"")

        #iterate through a set number of tweets per user and append to a dictionary
        
        for i in range(1):
            data.append(dict([("username", query),("tweet", tweets[i].text)]))
        #close chrome driver and chromium and file
       
        
#write dictionary data to tweet_data.json
with open("tweet_data.json", "w") as write_file:
    write_file.write("tweet_data =")
    json.dump(data, write_file, indent = 4)
        
        
twitter_username_file.close()
browser.quit()





  
    

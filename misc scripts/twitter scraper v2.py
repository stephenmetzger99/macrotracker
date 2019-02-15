import time
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys




browser = webdriver.Chrome()

base_url = u'https://twitter.com/'
query = u'elonmusk'
url = base_url + query

browser.get(url)
body = browser.find_element_by_tag_name('body')
tweets = browser.find_elements_by_class_name('tweet-text')

print("@" + query + " on Twitter: \"" + tweets[0].text + "\"")
print("@" + query + " on Twitter: \"" + tweets[1].text + "\"")

query = u'npr'
url = base_url + query

browser.get(url)
body = browser.find_element_by_tag_name('body')
tweets = browser.find_elements_by_class_name('tweet-text')

print("@" + query + " on Twitter: \"" + tweets[0].text + "\"")
print("@" + query + " on Twitter: \"" + tweets[1].text + "\"")

my_dict = {'user' : query, 'tweet' : tweets[0].text}
print (my_dict)
browser.quit()




  
    

import time
import json

from selenium import webdriver

with open("twitterusers.txt") as file:
    for line in file:
        query = line
    file.close()

          
browser = webdriver.Chrome()
base_url = u'https://twitter.com/'

url = base_url + query
browser.get(url)
body = browser.find_element_by_tag_name('body')
tweets = browser.find_elements_by_class_name('tweet-text')

print("@" + query + " on Twitter: \"" + tweets[0].text + "\"")
print("@" + query + " on Twitter: \"" + tweets[1].text + "\"")

#iterate through a set number of tweets per user

data = []
for i in range(3):
    data.append(dict([("username", query),("tweet", tweets[i].text)]))

    
#write to tweet_data.json
with open("tweet_data.json", "w") as write_file:
    write_file.write("tweet_data =")
    json.dump(data, write_file, indent = 4)
#close chrome driver and chromium    
browser.quit()






  
    

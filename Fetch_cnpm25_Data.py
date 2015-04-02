import datetime
import os
import time
import codecs
from bs4 import BeautifulSoup
import urllib2

def pro_city(input):
    city_name = input.text
    
    if len(city_name)== 7:
        city_name = 'WuHai'
        
    if len(city_name)>1:
        city_url = "http://www.cnpm25.com"+input["href"]

    try:
        city_response = urllib2.urlopen(city_url)
        city_soup = BeautifulSoup(city_response.read().decode("utf-8"))
        city_time = city_soup.find("div",{"class":"rt-share"})
            
    except urllib2.HTTPError,err:
        print 'Found an HTTP error! Will try again in 30 seconds.'
        time.sleep(30)
        pass

    except urllib2.URLError, err:
        print 'Found an URL error!Will try again in 30 seconds.'
        time.sleep(30)
        pass      
    return (city_name, city_time, city_soup)

#define a function to process each city
def writedatafile(inputname, inputtime, inputsoup):
    print 'printing files'
    strComma = u'\u002C'
    filename = inputname + ".csv"
    table = inputsoup.find("table")
    f = codecs.open(filename, "a+b", "utf-8")

    # get the time into format
    y = inputtime.text
    t = '/'.join([y[0:4], y[5:7],y[8:10] ]) + ' ' + y[12:14] + ':00'
    
    for row in table.findAll("tr"):
        global site
        global item
        site = row.findAll("td")
        if site:
            f.write(t + strComma)
            f.write(site[0].text+ strComma)
            f.write(site[1].text.replace('\r', '').replace('\n','') + strComma)
            f.write(site[3].text.replace('\r', '').replace('\n','') + strComma)
            f.write(site[4].text.replace('\r', '').replace('\n','') + strComma + u'\n')
    f.close()
        

# Main code
url = 'http://cnpm25.com'
r = urllib2.urlopen(url)
s = BeautifulSoup(r.read())
links = s.find_all("div",attrs={"class":"warp"})

time_dic = dict() # difine a empty dictionary to store time for each city

for x in links:
    link = x.findAll("a")
    for i in range(1,len(link)):
        city_name, city_time, city_soup = pro_city(link[i])
        writedatafile(city_name, city_time, city_soup)
        time_dic.update({city_name:city_time.get_text()})
        print city_name
        
count = 1
while count >0:
    print (time.strftime("%H:%M:%S"))
    print "Scanning the web..."
    for x in links:
        link = x.findAll("a")
        for i in range(1,len(link)):
            city_name, city_time, city_soup = pro_city(link[i])
            if city_name != '':
                if city_time.get_text() != time_dic[city_name]:
                    print "Found new time, updating files"
                    writedatafile(city_name, city_time, city_soup)
                    time.sleep(2)
                    time_dic.update({city_name:city_time.get_text()})
                else:
                    print "No new data"
                    
    print (time.strftime("%H:%M:%S"))
    print "Idling..."   

time.sleep(300) # web scrapping curtsy 	
    

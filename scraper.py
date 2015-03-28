import requests
import re
from progressbar import ETA, FileTransferSpeed, ProgressBar, Bar

class AqiSpider():
    
    def __init__(self):
        self.rootaddr = "http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?"
        self.city = ""
        self.startdate = ""
        self.enddate = ""
        self.page = 1
        self.pdate = re.compile(r'>(\d\d\d\d-\d\d-\d\d)')
        self.pcity = re.compile(r'>(.+)</td>[\r\n\t]*<.+>\d\d\d\d-')
        self.paqi = re.compile(r'-\d\d</td>[\t\n\r]*<.*>(\d*)<')

    def getContent(self):
        self.city = raw_input("City name: ")
        self.startdate = raw_input("Start date(in the format of 'yyyy-mm-dd'): ")
        self.enddate = raw_input("End date(in the format of 'yyyy-mm-dd'): ")
        r = requests.get(self.rootaddr+"city="+self.city+"&startdate="+
                         self.startdate+"&enddate="+self.enddate+"&page="+str(self.page))
        return r.text.encode('utf-8')

    def getRange():
        prange = re.compile(r'>(\d*)</font')
        return re.findall(prange, getContent())[1]

    def filterContent(self):
        datelist = re.findall(self.pdate, self.getContent())
        citylist = re.findall(self.pcity, self.getContent())
        aqilist = re.findall(self.paqi, self.getContent())

        return map(None, citylist, aqilist, datelist)

    def write_to_csv(self, filename):
        t = open(str(filename)+'.csv', 'a')
        for mapd in self.filterContent():
            t.write(','.join(mapd)+'\n')

myspider = AqiSpider()
pagecount = myspider.getRange()
widgets = [Bar(), ETA(), FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets)
for myspider.page in pbar(range(1, (pagecount+1))):
    myspider.write_to_csv('AQI')

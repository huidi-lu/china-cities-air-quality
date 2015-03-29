import re
import csv
import requests
from progressbar import Percentage, ETA, ProgressBar, Bar
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

def getSpace():
    ##r = requests.get(self.url_root).text
    ##cityname = re.findall(r'gstlp3">[\t\r\n]?\s*(.*)&nbsp', f)
    ##space = re.findall(r'"qdetail3\.aspx.*space=(\d*)" ',f)
    spacecodes = {}
    with open('spacedict.csv') as csvfile:
        f = csv.reader(csvfile)
        for item in f:
            spacecodes[item[1]]=item[0]
    return spacecodes

class MySpider():

    def __init__(self):
        
        ##self.url_root = 'http://www.ipe.org.cn/pollution/quality.aspx'
        self.url_getdetail = 'http://www.ipe.org.cn/pollution/getdetail.aspx?'
        self.spacecodes = getSpace()
        self.airinfo = []
            
    def getContent(self, code):
        self.airinfo = []
        years = map(lambda x:str(x), range(2004, 2014))
        for year in years:
            r = requests.get(self.url_getdetail+'space='+str(code)+'&type=airinfo&year='+year)
            if r.status_code != 500:
                content = r.text
                pm10 = re.findall(u'可吸入颗粒物浓度年日均值</td>[\t\r\n]?\s*<td>(.* )', content)
                so2 = re.findall(u'二氧化硫浓度年日均值</td>[\t\r\n]?\s*<td>(.* )', content)
                no2 = re.findall(u'二氧化氮浓度年日均值</td>[\t\r\n]?\s*<td>(.* )', content)
                co = re.findall(u'一氧化碳浓度年日均值</td>[\t\r\n]?\s*<td>(.* )', content)
                avg_dust = re.findall(u'城市平均降尘量</td>[\t\r\n]?\s*<td>(.*)<p>', content)
                rain_ph = re.findall(u'年均降水pH</td>[\t\r\n]?\s*<td>(.* )', content)
                acid_freq = re.findall(u'酸雨频率</td>[\t\r\n]?\s*<td>(.* )', content)
                o3 = re.findall(u'臭氧最大8小时年均值</td>[\t\r\n]?\s*<td>(.* )', content)
                pm25 = re.findall(u'细颗粒物浓度.*[\t\r\n]?\s*<td>(.*)mg', content)      
                self.airinfo += map(None, [year], pm10, so2, no2, co, avg_dust, rain_ph, acid_freq, o3, pm25)

    def output(self, code, filename = 'ipedata.csv'):
        self.getContent(code)
        outfile = open(filename, 'a')
        for i in range(len(self.airinfo)):
            outfile.write(self.spacecodes[str(code)]+','+','.join(self.airinfo[i])+'\n')

ipespider = MySpider()

widgets = [Bar(), Percentage(),' ', ETA()]
pbar = ProgressBar(widgets=widgets)
for spacecode in pbar(ipespider.spacecodes.keys()):
    ipespider.output(spacecode)
    time.sleep(10)

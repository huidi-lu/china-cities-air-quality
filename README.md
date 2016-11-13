## Air Quality Data of Major China Cities
Python version scrapers, inspired by [`@feelinglucky`](https://github.com/feelinglucky) and [`his project`](http://www.gracecode.com/aqi.html) of mainland china AQI database.<br><br>
`Official AQI` folder contains data crawled from MEP datacenter(http://datacenter.mep.gov.cn). The data is stored in the file `AQI.csv`, ranging from 2000-6-5 to 2015-3-27. There are three columns in it, namely `City`, `AQI`, `Date`(very easy to understand). If you wish to get this updated, please run the scraper and enter correct dates.<br>
`IPE Data` folder contains detailed data such as PM<sub>10</sub>, SO<sub>2</sub>, CO, average dust, in the file `ipedata.csv`. Original scraper is also included. If you wish to run this spider again(though I do not recommand so), please also download `spacedict.csv` to the same directory, as it translates the city name to its code used by the website. Personally I am very grateful for their work. If you also find the information useful, please consider donating to them! (link:[Support--IPE](http://www.ipe.org.cn/En/about/line.aspx))<br>
`US Ambassy Data` folder contains data from us ambassy in Beijing(2008-2014), Shanghai(2011-2014), Guangzhou(2011-2014), Shenyang(2013-2014) and Chengdu(2012-2014).<br>
`Fetch_cnpm25_Data.py` is a spider which crawls data from http://www.cnpm25.com/.<br>

###Data at a glance
PM25_199801_200012<br>
![PM25_199801_200012](https://raw.githubusercontent.com/Rudy1224/china-cities-air-quality/master/PM25_199801_200012.JPG)<br>

PM25_201001_201212<br>
![PM25_201001_201212](https://raw.githubusercontent.com/Rudy1224/china-cities-air-quality/master/PM25_201001_201212.JPG)<br>

Provincial-level correlation between China's 'Open Up and Reform' policy and air qulity change<br>
![scatter](https://raw.githubusercontent.com/Rudy1224/china-cities-air-quality/master/scatter - eng.png)

###Reference:
1. <b>[Air quality index - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Air_quality_index#Mainland_China)</b>
<p>China's Ministry of Environmental Protection (<a href="http://en.wikipedia.org/wiki/Ministry_of_Environmental_Protection_of_the_People%27s_Republic_of_China" title="Ministry of Environmental Protection of the People's Republic of China">MEP</a>) is responsible for measuring the level of air pollution in China. As of 1 January 2013, MEP monitors daily pollution level in 163 of its major cities. The API level is based on the level of 6 atmospheric pollutants, namely sulfur dioxide (SO<sub>2</sub>), nitrogen dioxide (NO<sub>2</sub>), suspended particulates smaller than 10 μm in <a href="http://en.wikipedia.org/wiki/Aerodynamic_diameter" title="Aerodynamic diameter" class="mw-redirect">aerodynamic diameter</a> (PM<sub>10</sub>), suspended particulates smaller than 2.5 μm in <a href="http://en.wikipedia.org/wiki/Aerodynamic_diameter" title="Aerodynamic diameter" class="mw-redirect">aerodynamic diameter</a> (PM<sub>2.5</sub>)， carbon monoxide (CO), and ozone (O<sub>3</sub>) measured at the monitoring stations throughout each city.</a></sup></p>
<p>  AQI Mechanics<br>
An individual score(IAQI) is assigned to the level of each pollutant and the final AQI is the highest of those 6 scores. The pollutants can be measured quite differently. PM<sub>2.5</sub>、PM<sub>10</sub> concentration are measured as average per 24h. SO<sub>2</sub>, NO<sub>2</sub>, O<sub>3</sub>, CO are measured as average per hour. The final API value is calculated per hour according to a formula published by the MEP.</a></sup></p>
<p>  AQI and Health Implications (HJ 663-2012)</p>

<table class="wikitable">
<tbody><tr>
<th style="text-align:center; width:100px;">AQI</th>
<th style="text-align:center; width:150px;">Air Pollution<br>
Level</th>
<th>Health Implications</th>
</tr>
<tr>
<td style="text-align:center;">0–50</td>
<td style="text-align:center;background-color:#00e400;color:#000">Excellent</td>
<td>No health implications.</td>
</tr>
<tr>
<td style="text-align:center;">51–100</td>
<td style="text-align:center;background-color:#ffff00;color:#000">Good</td>
<td>Few hypersensitive individuals should reduce outdoor exercise.</td>
</tr>
<tr>
<td style="text-align:center;">101–150</td>
<td style="text-align:center;background-color:#ff7e00;color:#fff">Lightly Polluted</td>
<td>Slight irritations may occur, individuals with breathing or heart problems should reduce outdoor exercise.</td>
</tr>
<tr>
<td style="text-align:center;">151–200</td>
<td style="text-align:center;background-color:#ff0000;color:#fff">Moderately Polluted</td>
<td>Slight irritations may occur, individuals with breathing or heart problems should reduce outdoor exercise.</td>
</tr>
<tr>
<td style="text-align:center;">201–300</td>
<td style="text-align:center;background-color:#99004c;color:#fff">Heavily Polluted</td>
<td>Healthy people will be noticeably affected. People with breathing or heart problems will experience reduced endurance in activities. These individuals and elders should remain indoors and restrict activities.</td>
</tr>
<tr>
<td style="text-align:center;">300+</td>
<td style="text-align:center;background-color:#7e0023;color:#fff">Severely Polluted</td>
<td>Healthy people will experience reduced endurance in activities. There may be strong irritations and symptoms and may trigger other illnesses. Elders and the sick should remain indoors and avoid exercise. Healthy individuals should avoid out door activities.</td>
</tr>
</tbody></table>

#####2. pH Value
A method of expressing differences in the acidity or alkalinity of a solution. A figure of 7 is regarded as neutral, figures below this indicate the decree of acidity and above alkalinity.

#####3. Particles
Particulate matter or PM (also called particle pollution) is the term for a mixture of solid particles and liquid droplets found in the air. Some particles, such as dust, dirt, soot, or smoke, are large or dark enough to be seen with the naked eye. Others are so small, they can only be detected using an electron microscope.  Particle pollution includes "inhalable coarse particles," with diameters larger than 2.5 micrometers and smaller than 10 micrometers and "fine particles," with diameters that are 2.5 micrometers and smaller. How small is 2.5 micrometers? Think about a single hair from your head. The average human hair is about 70 micrometers in diameter – making it 30 times larger than the largest fine particle.  These particles come in many sizes and shapes and can be made up of hundreds of different chemicals. Some particles, known as primary particles are emitted directly from a source, such as construction sites, unpaved roads, fields, smokestacks or fires. Others form in complicated reactions in the atmosphere of chemicals such as sulfur dioxides and nitrogen oxides that are emitted from power plants, industries and automobiles. These particles, known as secondary particles, make up most of the fine particle pollution in the country.<sub><i>Source: [United States Environmental Protection Agency](http://www.epa.gov/air/particlepollution/basic.html)</i></sub>

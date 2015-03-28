## Air Quality Index History of Major China Cities
Python version scraper, inspired by [`@feelinglucky`](https://github.com/feelinglucky) and [`his project`](http://www.gracecode.com/aqi.html) of mainland china AQI database.<br><br>
The data has already been crawled from MEP datacenter(http://datacenter.mep.gov.cn) and stored in the file `AQI.csv`, ranging from 2000-6-5 to 2015-3-27. There are three columns in it, namely `City`, `AQI`, `Date`(very easy to understand). If you wish to get this updated, please run the scraper and enter correct dates.<br>

###Reference:
[Air quality index - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Air_quality_index#Mainland_China)
<p>China's Ministry of Environmental Protection (<a href="http://en.wikipedia.org/wiki/Ministry_of_Environmental_Protection_of_the_People%27s_Republic_of_China" title="Ministry of Environmental Protection of the People's Republic of China">MEP</a>) is responsible for measuring the level of air pollution in China. As of 1 January 2013, MEP monitors daily pollution level in 163 of its major cities. The API level is based on the level of 6 atmospheric pollutants, namely sulfur dioxide (SO<sub>2</sub>), nitrogen dioxide (NO<sub>2</sub>), suspended particulates smaller than 10 μm in <a href="http://en.wikipedia.org/wiki/Aerodynamic_diameter" title="Aerodynamic diameter" class="mw-redirect">aerodynamic diameter</a> (PM<sub>10</sub>), suspended particulates smaller than 2.5 μm in <a href="http://en.wikipedia.org/wiki/Aerodynamic_diameter" title="Aerodynamic diameter" class="mw-redirect">aerodynamic diameter</a> (PM<sub>2.5</sub>)， carbon monoxide (CO), and ozone (O<sub>3</sub>) measured at the monitoring stations throughout each city.</a></sup></p>
<p><b>AQI Mechanics</b><br>
An individual score(IAQI) is assigned to the level of each pollutant and the final AQI is the highest of those 6 scores. The pollutants can be measured quite differently. PM<sub>2.5</sub>、PM<sub>10</sub> concentration are measured as average per 24h. SO<sub>2</sub>, NO<sub>2</sub>, O<sub>3</sub>, CO are measured as average per hour. The final API value is calculated per hour according to a formula published by the MEP.</a></sup></p>
<p><b>AQI and Health Implications (HJ 663-2012)</p>

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

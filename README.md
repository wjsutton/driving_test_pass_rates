<h1 style="font-weight:normal"> 
  Where to Pass the Great British Driving Test :car:
</h1>

[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/wjsutton/driving_test_pass_rates.svg)](https://github.com/wjsutton/driving_test_pass_rates/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/wjsutton/driving_test_pass_rates.svg)](https://github.com/wjsutton/driving_test_pass_rates/pulls) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

A data viz project explore driving test pass rates across the UK.

[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:

<!--/div-->

<!--
Quick Link 
-->

[Twitter]:https://twitter.com/WJSutton12
[LinkedIn]:https://www.linkedin.com/in/will-sutton-14711627/
[GitHub]:https://github.com/wjsutton
[Website]:https://wjsutton.github.io/

### :a: About

For many, passing their driving test enables them to travel across the country whenever they want to. The structure of the practical driving test remains the same across Great Britain but the amount of traffic, number of roundabouts, and potential hazards varies from place to place. 

Using data from the DVSA we can see that candidates could increase their chances of passing their practical driving test by carefully selecting their test centre. 

I've built a dataviz learner drivers to explore a map of Great Britain and the 300+ test centres to see the chances of passing the practical test, with historical data available as a hover over.   

### :broom: Data Clean Up

Two data sets are required for this viz:
- [Pass Rates by Test Centre](https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre)
- [Test Centre Locations](http://assets.dft.gov.uk/dvsa/find-your-nearest/practical.csv)

'Pass Rates by Test Centre' is downloaded as a .ods file, I've converted this to a Microsoft Excel file as it was planned to reshape the data with Python but the process is a one off and would have been more time consuming than manually reshaping this dataset. 

Below are the sets I took to reshape the data into [driving_tests_map.xlsx](data/driving_tests_map.xlsx)

1. Clean up yearly tabs for [Pass Rates by Test Centre](https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre), removing any blank columns, keeping only the total rows for each test centre, and adding the date range for the data.
2. Considate all the tabs into one tab 'Historical Data', so we have all the data in one place, columns should be:
Test Centre, Date, Male - Conducted, Male - Passes, Male - Pass rate (%), Female - Conducted, Female - Passes, Female - Pass rate (%), Total - Conducted, Total - Passes, Total - Pass rate (%)
3. For [Test Centre Locations](http://assets.dft.gov.uk/dvsa/find-your-nearest/practical.csv) add to the Excel file and reduce to test centre name, lat and long
4. Clean up test centre names in 'Historical Data', some names are also inconsistent between the locations.
5. Create three tabs, 1. A location lookup table 2. Pass rates by location for April 2020/2021 (looking up locations from the location lookup) 3. Historical pass rates by location
6. In Tableau size and check the test centre location squares, aiming to have square visable from a distance. 
7. For overlapping test centres create seperate zoomed in maps for cities, in other cases editing the lat and long data to nudge the square location so the data is clear (a rough location is fine for this viz)

### Visual Alphabet

For this viz I want to show 4 variables:
- the location of the test centres on a map of the UK (latitude and longitude) 
- how the driving tests pass rates differ from the national average
- whether men or women are more likely to pass their test at this test centre

Encoding 
- Using the location to place the test centres on the map, 
- I have created a sloped area chart to show the difficultly, i.e. an uphill slope indicates a relatively harder test. 
- To show gender I have coloured the red, blue and black, for female, male and no clear advantage. 

Detailing all of this information in the legend at the top of the map, with tooltips to help explain the data points so the users doesn't have to check the legend when viewing test centres in the South of England

<img src='https://github.com/wjsutton/driving_test_pass_rates/blob/main/Visual%20Alphabet.png?raw=true width="80%">

### 📈 Tableau Features


### 📈 See the Dashboard 

URL: [https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests](https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests)

<div style="overflow: hidden;margin: 0 10px 0 0">
<a href="https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests">
<img src='https://github.com/wjsutton/driving_test_pass_rates/blob/main/Driving%20Tests.png?raw=true width="80%">
</a>
</div>

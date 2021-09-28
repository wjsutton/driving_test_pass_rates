<h1 style="font-weight:normal"> 
  Where to Pass the Great British Driving Test :car:
</h1>

A data viz project exploring driving test pass rates across the UK.
<br>

[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/wjsutton/driving_test_pass_rates.svg)](https://github.com/wjsutton/driving_test_pass_rates/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/wjsutton/driving_test_pass_rates.svg)](https://github.com/wjsutton/driving_test_pass_rates/pulls) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:

<!--/div-->

<!--
Quick Link 
-->

[Twitter]:https://twitter.com/WJSutton12
[LinkedIn]:https://www.linkedin.com/in/will-sutton-14711627/
[GitHub]:https://github.com/wjsutton
[Website]:https://wjsutton.github.io/

<table border="0">
 <tr>
    <td><b>:rocket: PROJECT</b></td>
    <td><b>:link: LINK</b></td>
 </tr>
 <tr>
    <td>Personal Interest</td>
    <td><a href="https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests">Tableau Public</a></td>
 </tr>
 <tr>
    <td><b>:hammer_and_wrench: TOOLS</b></td>
    <td><b>:oil_drum: DATA</b></td>
 </tr>
 <tr>
    <td>Excel, <br>Tableau Public, <br>Mapbox Studio, <br>Figma</td>
    <td>DVSA driving test centre pass rates, <br>DVSA driving test centre locations<br><br><br></td>
 </tr>
 <tr>
    <td><b>:trophy: AWARDS</b></td>
    <td><b>:newspaper: CITATIONS</b></td>
 </tr>
 <tr>
    <td><a href="https://public.tableau.com/en-us/gallery/where-pass-great-british-driving-test?tab=viz-of-the-day&type=viz-of-the-day">Viz of the Day 2021-09-14</a><br><a href="https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests">50+ :star: on Tableau Public</a></td></td>
    <td><a href="https://www.tableau.com/community/blog/2021/9/datafam-roundup-september-6-10-2021">DataFam Roundup: Sept 6 - 10, 2021</a><br><br></td>
 </tr>
</table>

### :a: About

For many, passing their driving test enables them to travel across the country whenever they want to. The structure of the practical driving test remains the same across Great Britain but the amount of traffic, number of roundabouts, and potential hazards vary from place to place.

Using data from the DVSA, I have crafted this informative map of 300+ driving test centres pass rates across Great Britain. With the data provided candidates can see their chances of passing their practical driving test at nearby centres. 


<a href="https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests">
<img src='https://github.com/wjsutton/driving_test_pass_rates/blob/main/Driving%20Tests.png?raw=true' width="35%">
</a>

<!--a href="https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests">
<img align='right' src=https://github.com/wjsutton/driving_test_pass_rates/blob/main/screenshots/Collage.png?raw=true' width="35%">
</a-->



<h1 style="font-weight:normal"> 
:hammer: Building the Visualisation
</h1>


### :oil_drum: Data Sources
Two data sets are required for this viz:
- [Pass Rates by Test Centre](https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre)
- [Test Centre Locations](http://assets.dft.gov.uk/dvsa/find-your-nearest/practical.csv)

'Pass Rates by Test Centre' is downloaded as a .ods file, I've converted this to a Microsoft Excel file as it was planned to reshape the data with Python but the process is a one-off and would have been more time consuming than manually reshaping this dataset. 


### :broom: Data Clean Up

Below are the sets I took to reshape the data into [driving_tests_map.xlsx](data/driving_tests_map.xlsx)

1. Clean up yearly tabs for [Pass Rates by Test Centre](https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre), removing any blank columns, keeping only the total rows for each test centre, and adding the date range for the data.
2. Consolidate all the tabs into one tab 'Historical Data', so we have all the data in one place, columns should be:
Test Centre, Date, Male - Conducted, Male - Passes, Male - Pass rate (%), Female - Conducted, Female - Passes, Female - Pass rate (%), Total - Conducted, Total - Passes, Total - Pass rate (%)
3. For [Test Centre Locations](http://assets.dft.gov.uk/dvsa/find-your-nearest/practical.csv) add to the Excel file and reduce to test centre name, lat and long
4. Clean up test centre names in 'Historical Data', some names are also inconsistent between the locations.
5. Create three tabs, 1. A location lookup table 2. Pass rates by location for April 2020/2021 (looking up locations from the location lookup) 3. Historical pass rates by location
6. In Tableau size and check the test centre location squares, aiming to have square visible from a distance. 
7. For overlapping test centres, create separate zoomed-in maps for cities, in other cases editing the lat and long data to nudge the square location so the data is clear (a rough location is fine for this viz)


### :a: Visual Alphabet and Accessibility

For this viz I want to show 4 variables:
- the location of the test centres on a map of the UK (latitude and longitude) 
- how the driving tests pass rates differ from the national average
- whether men or women are more likely to pass their test at this test centre

Encoding 
- Using the location to place the test centres on the map, 
- I have created a sloped area chart to show the difficultly, i.e. an uphill slope indicates a relatively harder test. 
- To show gender I have coloured the red, blue and black, for female, male and no clear advantage. 

Detailing all of this information in the legend at the top of the map, with tooltips to help explain the data points so the users don't have to check the legend when viewing test centres in the South of England.

<p align="center">
  <img src='https://github.com/wjsutton/driving_test_pass_rates/blob/main/Visual%20Alphabet.png?raw=true' width="60%">
</p>

### :chart_with_upwards_trend: Charting in Tableau

Two charts types are used in this dashboard:
- the beeswarm plot
- the difficulty tiles (boxes)

#### :bee: Beeswarm plot

<img align="right" src='https://github.com/wjsutton/driving_test_pass_rates/blob/main/screenshots/beeswarm.png?raw=true' width="45%">


The beeswarm plot generally follows the tutorial from Ken Flerlage: [Creating a Basic Beeswarm Plot in Tableau](https://www.flerlagetwins.com/2020/11/beeswarm.html)

Notes for this specific build:
- Total pass rates are rounded and converted to integers `INT(ROUND([Total - Pass rate (%)],0))`
- A reference line for the national average was added and then rebuilt in Figma so the line didn't overlap the data points
- Adding a categorical colour palette caused calculation issues with the plot, I worked around these issues by using a custom sequential colour palette taking the values -1, 0, or 1 and adding the following to my Tableau preference.tps file between the `<preferences>` tags:

```
<color-palette name="Driving test" type="ordered-sequential" >
  <color>#7196ff</color>
  <color>#333333</color>
  <color>#f55343</color>
</color-palette>
```
Lastly, all text (notes, reference line, axis values, legend) were all created in Figma and layered underneath this plot, with the plot background set to None.


#### :ballot_box: Difficulty tiles (boxes)

The tiles are constructed using Tableau's new feature called map layers, essentially 4 separate components are drawn and layered on top of each other, they are:
- A background square (polygon) - a white background so the data stands out
- A slope chart (polygon) - how difficult the test is compared to the national average
- An angled car shape (shape) - so the car looks like it driving on the slope
- A blank foreground square (polygon) - giving ease of access to tooltips

In the dataset [driving_tests_map.xlsx](data/driving_tests_map.xlsx), I have created additional datapoints to build and path the polygons for the map layers.
In the tab `driving_tests_map` I added the following fields to build the polygon elements:
- [X, Y, Path] - draws the polygon shape
- [Element] - filters between the background polygon and slope polygon
- [Dataset] - filters for polygon data and the actual data set used for tooltips and calculations

The boxes are finished off by the tooltip detailing the test centre name, pass rates for overall and by gender, with a viz in tooltip sheet showing the historical trend for the test centre.

### :world_map: Mapbox

Mapbox studio is a great place to build custom-style maps for Tableau to give your work a unique look and feel. 

[Map Preview](https://api.mapbox.com/styles/v1/wjsutton/ckt7n3h8u12ty18phm8aioy94.html?title=view&access_token=pk.eyJ1Ijoid2pzdXR0b24iLCJhIjoiY2t0dWJiZTN0MDh1NTJvcDg3ZjRsODdvcyJ9.E-c5AaCDnUfhPCO2zLEyzA&zoomwheel=true&fresh=true#5.66/55.093/-2.23)

In [Mapbox studio](https://studio.mapbox.com/) > New Style > Under `Components`
- Change Base, Greenspace and Greenspace Label colour to #b6d1a3
- Change Roads to #f2eeee 
- Change Water to #e6f9f8

Note due to the number of maps on show (8) and being featured on VOTD means I exceeded the free tier API usage, so had to reset my API key and revert the maps to the standard free versions available with Tableau.

### :framed_picture: Figma Assets

I've used Figma to build:
- [Car icons](/car_icons)
- [Background](/figma)

#### :car: Car Icons

In Figma, I constructed sample slopes at angles from +45 to -45 incrementing by 5 degrees in 100x100px squares. I then positioned the car icon on the slope in the centre of the square. I then hid the slope, made the squares transparent and exported the car icons so they are all sized the same. 

Car Icon source from Freepik

#### :uk: Background

The background consists of the map of Great Britain, all text objects, and callouts for the additional maps.  

The process involves creating a background image in Figma with the same dimensions as the dashboard being made, tiling this image on the dashboard removing any padding and disabling the `fit to space` option. Assets in Tableau such as charts are then floated on top of the background, using the layout option you can  make these fit pixel perfect to your Figma background. From here there is a lot of back and forth with Tableau, exporting dashboard images, editing the background in Figma until you are happy with the result. 

Font used: Nobile

---

<div style="overflow: hidden;margin: 0 10px 0 0">
<a href="https://public.tableau.com/app/profile/wjsutton/viz/WheretoPasstheGreatBritishDrivingTest/DrivingTests">
<img src='https://github.com/wjsutton/driving_test_pass_rates/blob/main/Driving%20Tests.png?raw=true' width="100%">
</a>
</div>

<br>

Will Sutton, Sept 2021<br>
[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:

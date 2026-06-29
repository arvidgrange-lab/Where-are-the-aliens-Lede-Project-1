# Where are the aliens  -   Lede Project 1  -   Arvid Grange

## Project purpose - mapping UFO locations from the US Government

     The point of the project was to create a clear overview of where the UFO incidents declassified by the U.S government this spring have taken place, to insert the raw location data of these files into the broader popular debate surrounding UFOs, as well as to get a look at where these incidents are concentrated.

     Each location for a UFO incident is represented by a marker on the map. The size of that marker represents the number of incidents reported in that location.

## Findings
My findings were that the UFO-documents released to the public contain reports of UFO incidents from all over the world, collected since the middle of the previous century.

        Though they are spread out all over the world, the thickest concentrations are in the united states and the middle east.

        One surprising finding is that several of the reports are incidents that occured in space, reported by NASA astronauts.

## Data collection process
My data was scraped from the official UFO release website of the U.S department of war.
link: https://www.war.gov/UFO/limit/1000/?type=.pdf

All files have an "incident location" field attached to them. For many documents this field is N/A, however.

The lack of consistent incident locations, as well as different files pertaining to the same incidents, and the fact that I scraped only the pdf-files (since duplicates such as different angles with images and video create clutter), created some limitations to the accuracy of the project.

I can not claim to have mapped the locations of all the files released by the U.S government, but have instead created a map based on the incident locations published alongside the pdf documents released.

## Data analysis
My data analysis was quite simple since the project was focused on the mapping aspect. The biggest challenge was data cleaning.

Since all documents contain more sub-categories than just location, and since all these sub-categories have the same html-tab, I was unable to filter the scraping process to give me only locations.

With pandas I used .melt, str.replace, and regex to filter away all data that was not location names. The aim was to geocode these locations so I replaced locations such as "USSR" with "Russia". I also changed "Pacific Time Zone" to "Western United States" in order to not have two separate locations with such a big overlap.

Locations like "Moon" and "Low Earth Orbit" were also filtered away for the geocoding to work.

I created a new column to show how many times a particular location occured in the files released. Then I double-checked that spreadsheet and adjusted it manually by cross-referencing the duplicates with the DOW's website, looking inside files with the same location name to see if they are individual incidents or not.

## New skills and approaches
Scraping a website that uses single page application was challenging. I would get some data but not all, which, after some errors, taught me to quickly overview the data to see if it was correct.

The data cleaning was also challenging and my skills in regex grew substantially.

Doing so much work with CSS and Javascript in order to get the Mapbox globe map to be interactive also developed my understanding of those fields.


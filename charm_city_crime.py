#
# Data visualization of crime in Baltimore, MD
#
# Dane Fichter - 7/2/17

import gmplot
import requests

if __name__ == '__main__':

    # Gather data
    crime_base_2015 ='https://data.baltimorecity.gov/resource/4ih5-d5d5.json'
    crime_description = 'HOMICIDE'
    resp = requests.get(
        crime_base_2015 + '?' + 'description=' + crime_description,
        verify=False
    )
    homicides = resp.json()
    print "Length: " + str(len(homicides))

    # Plot the data
    lats = []
    lons = []
    gmap = gmplot.GoogleMapPlotter(39.322675, -76.631554, 14)
    for incident in homicides:
        address = incident['location_1']
        coords = address['coordinates']
        lon_address = coords[0]
        lat_address = coords[1]
        lats.append(lat_address)
        lons.append(lon_address)
    
    gmap.scatter(lats, lons, 'k', marker=True)
    gmap.draw("map.html")

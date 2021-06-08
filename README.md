# BikeDash

## Automation suggestions

```
git clone https://github.com/pe-st/garmin-connect-export
```

Download the activities with json descriptions and the corresponding gpx files
TODO: #1 Optimize this sequential download to be in parallel
```
python3 garmin-connect-export/gcexport.py --username **** --password ******** -c 10 -d './GarminDump' -s 'activities' -f json
python3 garmin-connect-export/gcexport.py --username **** --password ******** -c 10 -d './GarminDump' -s 'activities' -f gpx
```

TODO #2 Implement a watchdog to add new activities to the database


### Sources

https://towardsdatascience.com/build-interactive-gps-activity-maps-from-gpx-files-using-folium-cf9eebba1fe7
https://github.com/pe-st/garmin-connect-export

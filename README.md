# BikeDash

- [BikeDash](#bikedash)
  - [Initial Setup](#initial-setup)
  - [Docker Setup Steps](#docker-setup-steps)
    - [Execute the Garmin-Connect-Export module](#execute-the-garmin-connect-export-module)
  - [Sources](#sources)


## Initial Setup

```
git clone https://github.com/pe-st/garmin-connect-export
```

Download the activities with json descriptions and the corresponding gpx files

In order to "savely store" credentials and not accidentially commiting them the use of environment variables is the preffered solution.

```
export gce_user=blabla
export gce_pass=secret
```

call the following to download the most recent 10 activities in JSON as well as GPX format.
```
python3 garmin-connect-export/gcexport.py --username $gce_user --password $gce_pass -c 10 -d './GarminDump' -s 'NewActivities' -f json
python3 garmin-connect-export/gcexport.py --username $gce_user --password $gce_pass -c 10 -d './GarminDump' -s 'NewActivities' -f gpx
```
## Docker Setup Steps
```
docker build -t soriddler/bikedash .
docker run -d --name bikedash \
   -p 8890:5000 \
   -v /home/rnd/Projects/BikeDash/database:/usr/src/app/database \
   -v /etc/localtime:/etc/localtime:ro \
   --env-file config.env \
   soriddler/bikedash
```
### Execute the Garmin-Connect-Export module
```
docker exec -t boulderdash python3 /usr/src/app/garmin-connect-export/gcexport.py --username $gce_user --password $gce_pass -c 10 -d './GarminDump' -s 'NewActivities' -f json
docker exec -t boulderdash python3 /usr/src/app/garmin-connect-export/gcexport.py --username $gce_user --password $gce_pass -c 10 -d './GarminDump' -s 'NewActivities' -f gpx
```



TODO #2 Implement a watchdog to add new activities to the database

* for each newly downloaded **gpx** and **json** activities with gps data there will be a created and a modified event from the file system when the modification event is triggered the information will be passed to a queue module where the file will be processed and added to the database. Once processed the files will be moved and dequeued.



## Sources

* [Interactive map with step by step instructions; inspiration for this project](https://towardsdatascience.com/build-interactive-gps-activity-maps-from-gpx-files-using-folium-cf9eebba1fe7)
* [garmin connect export python module](https://github.com/pe-st/garmin-connect-export)

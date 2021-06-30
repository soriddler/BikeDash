import gpxpy
import pandas as pd

class dataProcessing():
    def process_gpx_to_df(file_name) -> pd.DataFrame:
        columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
        with open(file_name, 'r+') as f:
            gpx = gpxpy.parse(f)
            # restructure the data
            segment = gpx.tracks[0].segments[0]
            # Load the data into a Pandas dataframe (by way of a list)
            data = [[point.longitude, point.latitude,point.elevation,point.time, segment.get_speed(point_idx)] for point_idx, point in enumerate(segment.points)]
        # return the dataframe
        return pd.DataFrame(data, columns=columns)
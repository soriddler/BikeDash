import unittest
import os, sys

#Insert system variable to allow easy import of module
sys.path.insert(0, os.path.join(sys.path[0], '..', '..', '..', 'services', 'dataProcessing'))

from gpxDataPointCalculations import dataProcessing

class TestGPXDataProcessingNormalCase(unittest.TestCase):
    def setUp(self) -> None:
        self.absoluteDatasetPath = os.path.join(sys.path[1], '..', '..', 'datasets')
        return super().setUp()


    def test_normalFile(self):
        path = os.path.join(self.absoluteDatasetPath, 'cyclingActivity.gpx')
        data = dataProcessing.process_gpx_to_df(path)
        self.assertTrue(len(data['Longitude']) > 1)
        self.assertTrue(len(data['Latitude']) > 1)
        self.assertTrue(len(data['Altitude']) > 1)
        self.assertTrue(len(data['Time']) > 1)
        self.assertTrue(len(data['Speed']) > 1)

    def test_emptyFile(self):
        path = os.path.join(self.absoluteDatasetPath, 'emptyActivity.gpx')
        data = dataProcessing.process_gpx_to_df(path)
        self.assertTrue(data.empty)

    def test_NotExistingFile(self):
        path = os.path.join(self.absoluteDatasetPath, 'fileDoesNotExist.gpx')
        self.assertRaises(FileNotFoundError, dataProcessing.process_gpx_to_df, path)
        
if __name__ == '__main__':
    unittest.main()
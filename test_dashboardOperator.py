import unittest
from  dashboardOperator import process_file
import pandas as pd
import io


class TestDashboardOperatorMethods(unittest.TestCase):

# this function is testing a csv file
   def test_process_file_passing_csv(self):

        # setting up a mock csv
       mock_csv = io.StringIO("col1,col2,col3\n1,2,3\n4,5,6")
       mock_csv.name = 'mocked_file.csv'

       # this is what the expected answer is going to be
       expected_df =  pd.DataFrame({
           'col1': [1, 4],
           'col2': [2, 5],
           'col3': [3, 6]
       })
        # this is the actual answer
       actual_df = process_file(mock_csv)


        # this is comparing answer actual to the expected
       pd.testing.assert_frame_equal(actual_df, expected_df)

if __name__ == '__main__':
   unittest.main()
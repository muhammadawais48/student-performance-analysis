import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import pandas as pd
from src.analyze import analyze
class TestAnalysis(unittest.TestCase):
    def test_outputs(self):
        with TemporaryDirectory() as temp:
            summary=analyze(Path('data/students.csv'),Path(temp))
            self.assertEqual(summary['student_count'],200)
            self.assertTrue((Path(temp)/'score_distribution.png').exists())
            self.assertTrue((Path(temp)/'department_summary.csv').exists())
    def test_bad_data(self):
        with TemporaryDirectory() as temp:
            path=Path(temp)/'bad.csv';pd.DataFrame({'student_id':['1']}).to_csv(path,index=False)
            with self.assertRaises(ValueError): analyze(path,Path(temp)/'out')
if __name__=='__main__': unittest.main()

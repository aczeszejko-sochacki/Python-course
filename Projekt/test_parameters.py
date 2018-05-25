import unittest
from clasificate_iris import Target
import pandas as pd


class Tests(unittest.TestCase):

    def test_correct_parameters(self):  # params in a tuple
        all_data = pd.read_csv('iris.csv')

        data = all_data.drop('species', axis=1)
        data = data.drop('Unnamed: 0', axis=1)
        data = data.values
        target = all_data['species']
        target = target.values
        iris = Target(data, target)

        tests = [(('1', '2', '3.3', '4', '1'), True),
                 (('a', '2', '2', '1', '2'), False),
                 (('-1', '2', '2', '2', '2'), False)]

        for test in tests:
            sl, sw, pl, pw, n = test[0]
            result = test[1]
            self.assertEqual\
                (iris.clasificate_iris_to_test
                 (sl, sw, pl, pw, n), result)


if __name__ == "__main__":
    unittest.main()

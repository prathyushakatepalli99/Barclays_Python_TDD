import unittest


class TestHighestNumber(unittest.TestCase):
    def test_highest_num_finder(self):
        input_val = [8]
        cut = HighestNumber()  # cut - class/code under test
        expected_result = 8

        # Act
        actual_result = cut.highest(input_val)

        # #Assert
        self.assertEqual(expected_result, actual_result)

        if __name__ == '__main__':
            unittest.main()

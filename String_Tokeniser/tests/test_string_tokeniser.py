import unittest


class TestStringTokenizer(unittest.TestCase):
    def test_empty_string_result_empty_list(self):
        # AAA
        # Arrange
        input_val = ""
        cut = StringTokenizer()  # cut - class/code under test
        expected_result = []

        # Act
        actual_result = cut.tokenize(input_val)

        # #Assert
        self.assertEqual(expected_result, actual_result)

        if __name__ == '__main__':
            unittest.main()
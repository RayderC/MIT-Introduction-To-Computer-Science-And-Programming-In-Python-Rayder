from unittest import mock, TestCase
import unittest
from calc import calc

class TestMain(TestCase):
    @mock.patch('builtins.input', side_effect=['120000', '0.05', '500000', '0.03'])
    def test_main(self, mocked_input):
        result = calc()
        expectedResult = "Number of months: 142"
        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    unittest.main()

import unittest
import StringCalculator
from StringCalculator import StringCalculator

class Test_StringCalculatorTest(unittest.TestCase):

    def test_emptyString_returnsEmpty(self):
        stringCalculator = StringCalculator()
        numberResult = stringCalculator.Add("")
        self.assertEqual(0, numberResult)

    def test_hasPositiveNumbers_NumbersAreAdded(self):
        stringCalculator = StringCalculator()
        numberResult = stringCalculator.Add("7,9,8,4")
        self.assertEqual(28, numberResult)

    def test_NumbersSeparatedByNewLine_NumbersAreAdded(self):
        stringCalculator = StringCalculator()
        numberResult = stringCalculator.Add("7,9,8\n4")
        self.assertEqual(28, numberResult)

    def test_CustomDelimiterIncluded(self):
        stringCalculator = StringCalculator()
        numberResult = stringCalculator.Add("//;\n7;9;8;4")
        self.assertEqual(28, numberResult)

    def test_CustomDelimiterOfAnyLength(self):
        stringCalculator = StringCalculator()
        self.assertEqual(28, stringCalculator.Add("//****\n7****9****8****4"))

    def test_MultipleCustomDelimitersAccepted(self):
        stringCalculator = StringCalculator()
        self.assertEqual(28, stringCalculator.Add("//[%][**]\n7%9**8**4"))

    def test_NegativeNumber_ExceptionThrown(self):
        stringCalculator = StringCalculator()

        with self.assertRaises(ValueError):
            stringCalculator.Add("7,-9,8,4")

    def test_NumbersGreaterThanAThousandIgnored(self):
        stringCalculator = StringCalculator()
        self.assertEqual(28, stringCalculator.Add("//;\n7;9;8;4;1025"))

if __name__ == '__main__':
    unittest.main()

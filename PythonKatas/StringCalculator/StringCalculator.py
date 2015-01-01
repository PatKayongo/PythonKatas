import StringHelper

class StringCalculator(object):
    """String Calculator Kata which can be found here http://osherove.com/tdd-kata-1/"""

    def Add(self, numbers):
        numberList = self._getNumberListFromString(numbers)
        totalCount = 0
        negativeNumbers = []
        for number in numberList:

            if number < 0:
                negativeNumbers.append(number)
            elif number <= 1000:
                totalCount += number

        if len(negativeNumbers) > 0:
            raise ValueError('negatives not allowed - ' + ', '.join(str(x) for x in negativeNumbers))

        return totalCount

    def _getNumberListFromString(self, numberString):
        numberList = []
        delimiterList = [',', '\n']

        if numberString.startswith('//'):
            indexOfNewLine = numberString.index('\n')
            delimiterString = numberString[2:indexOfNewLine]
            
            if '[' in delimiterString:
                delimiterString = delimiterString[1:-1]
                customDelimiterList = delimiterString.split('][')
                delimiterList.extend(customDelimiterList)
            else:
                delimiterList.append(delimiterString)            
            numberString = numberString[(indexOfNewLine + 1):]

        self._addToNumberListFromStringList(numberList, numberString, delimiterList)
        return numberList;

    def _addToNumberListFromStringList(self, numberList, numberString, delimiterList):
        if len(delimiterList) == 0:
            return

        currentDelimiter = delimiterList[0]
        delimiterList.pop(0)
        stringList = numberString.split(currentDelimiter)
        for string in stringList:
            if StringHelper.is_numeric(string):
                numberList.append(int(string))
            else:
                self._addToNumberListFromStringList(numberList, string, delimiterList)
import math

class Solution(object):
    def generate(self, numRows):
        output = []

        for j in range(numRows):
            row = []
            for i in range(j + 1):
                row.append((math.factorial(j)) / (math.factorial(i) * math.factorial(j - i)))
            output.append(row)
        return output
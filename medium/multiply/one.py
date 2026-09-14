class Solution(object):
    def multiply(self, num1, num2):
        """
        The logic behind this is no need of conversion to int through any of the hashMapping or so,
        just following the elementary multiplication is the key idea.
        """
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                pos = i + j + 1
                result[pos] += product

                result[pos - 1] += result[pos] // 10
                result[pos] %= 10

        start = 0

        while start < len(result) and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))

class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiou"
        string_list = list(s)
        front = 0; back = len(s) - 1

        while front < back:
            while front < back and string_list[front].lower() not in vowels:
                front += 1

            while front < back and string_list[back].lower() not in vowels:
                back -= 1

            if front < back:
                string_list[front], string_list[back] = string_list[back], string_list[front]
                front += 1
                back -= 1

        return "".join(string_list)

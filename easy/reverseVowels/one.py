class Solution(object):
    def reverseVowels(self, s):
        """
        The logic is if both the pointers point towards the vowels then tuple swap them, else increase front/back
        depending on the case of vowels.
        """
        vowels = "aeiou"
        front = 0; back = len(s) - 1
        string_list = []

        for ch in s:
            string_list.append(ch)

        while front < back:
            if string_list[front].lower() in vowels and string_list[back].lower() in vowels:
                string_list[front], string_list[back] = string_list[back], string_list[front]
                front += 1
                back -= 1
            elif string_list[front].lower() in vowels and string_list[back].lower() not in vowels:
                back -= 1
            elif string_list[front].lower() not in vowels and string_list[back].lower() in vowels:
                front += 1
            else:
                front += 1
                back -= 1

        return ''.join(string_list)

def check_valid_parenthesis(testString):
    dictMap = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []

    for i in testString:
        if i in '({[':
            stack.append(i)
        elif i in dictMap:
            if not stack and stack[-1] != dictMap.get(i):
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0

print(check_valid_parenthesis('([{[]}])'))
print(check_valid_parenthesis('()[]'))
print(check_valid_parenthesis('('))
print(check_valid_parenthesis(''))
class Solution(object):
    def addBinary(self, a, b):
        result = []
        carry = 0
        
        # Pointers for both strings starting at the last character
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add bit from string 'a' if pointer is valid
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Add bit from string 'b' if pointer is valid
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The current bit to append is total % 2 (either 0 or 1)
            result.append(str(total % 2))
            
            # Update the carry for the next position (either 0 or 1)
            carry = total // 2
            
        # Since we added bits from right to left, reverse the result
        return "".join(reversed(result))

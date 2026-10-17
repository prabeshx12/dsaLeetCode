class Solution(object):
    def canWinNim(self, n):
        """
        The logic is to look for the pattern first;
        I can remove either of 1, 2 or 3 stones. If either of 1, 2 or 3 stones are there, I can remove them and win it.
        But what happens when I have 4 stones in my first go? Well, I can do whatever I want but I will leave my opponent
        with the winning position of either 3, 2 or 1. If I continue this then, I can notice that if I can force my opponent to 
        move the stones with the multiple of 4, I can win it. So every time I start with the multiple of 4, I lose.
        So, the number of stones shouldn't be the multiple of 4 for me to win provided we both play the game optimally.
        """
        return n % 4 != 0

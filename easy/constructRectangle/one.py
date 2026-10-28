class Solution(object):
    def constructRectangle(self, area):
        """
        The logic is to look for the pairs of (L, W) that is equal to the area and only listing out the L and W
        pair where L is greater than W. Then we check for the minimum (L - W) pair in the possibleList and then
        return that pair of [L, W]
        """
        i = 1
        possList = []

        while i * i <= area:
            if area % i == 0:
                if i >= area // i:
                    possList.append([i, area // i])
                else:
                    possList.append([area // i, i])
            
            i += 1
        
        min = possList[0][0] - possList[0][1]

        for pair in possList:
            if pair[0] - pair[1] < min:
                min = pair
            
        return pair

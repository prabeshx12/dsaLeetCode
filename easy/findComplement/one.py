class Solution(object):
    def findComplement(self, num):
        """
        The logic is to first convert the number into its binary form list from backward i.e. if 4 is 100 then in
        the list it will be [0, 0, 1] then we will complement the bits using the XOR with each element in the list
        with 1, getting result such as [1, 1, 0] for this example of 4. Then, we convert that list bits into the
        binary back using 2 ** count multiplication with the face values of bits.
        """
        bin_lst = []

        while num != 0:
            bin_lst.append(num % 2)
            num //= 2
        
        cmp_bin_lst = [x ^ 1 for x in bin_lst]
        cmp_dec = 0
        count = 0

        for bit in cmp_bin_lst:
            cmp_dec += bit * 2 ** count
            count += 1
        
        return cmp_dec

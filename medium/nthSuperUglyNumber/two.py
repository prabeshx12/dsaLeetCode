class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        The logic is to generate super ugly numbers using dynamic programming. We maintain pointers 
        for each prime to generate the next possible super ugly number. In each iteration, we select the 
        smallest candidate and update the pointers that produced it to avoid duplicates. This is more optimal 
        for bigger n because it generates only super ugly numbers instead of checking every integer starting
        from 2.
        """
        if n == 1:
            return 1

        sup_ugly = [1]
        k = len(primes)
        idx = [0] * k
        vals = list(primes)

        while len(sup_ugly) < n:
            num = min(vals)
            sup_ugly.append(num)

            for j in range(k):
                if vals[j] == num:
                    idx[j] += 1
                    vals[j] = sup_ugly[idx[j]] * primes[j]

        return sup_ugly[-1]

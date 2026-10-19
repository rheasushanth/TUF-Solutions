class Solution:
    def primeTillN(self, n):
        #your code goes here
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p*p <= n:
            if is_prime[p]:
                for j in range(p*p,n+1,p):
                    is_prime[j] = False
            p+=1
        return [i for i in range(2,n+1) if is_prime[i]]
            




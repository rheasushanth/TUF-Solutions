class Solution:
    def search(self, pat, txt):
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []
        
        B = 256
        MOD = 1_000_000_007
        high = pow(B, m-1, MOD)

        phash = thash = 0
        for i in range(m):
            phash = (phash * B + ord(pat[i])) % MOD
            thash = (thash * B + ord(txt[i]))% MOD
        result = []
        for i in range(n-m+1):
            if phash == thash and txt[i:i+m] == pat:
                result.append(i)

            if i < n-m:
                thash = ((thash - ord(txt[i])*high)*B + ord(txt[i+m])) % MOD
            
        return result
     
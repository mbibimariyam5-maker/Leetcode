class Solution(object):
    def frequencySort(self, s):
        
        hash = {}
        for ch in s:
            if ch in hash:
                hash[ch] += 1
            else:
                hash[ch] = 1
        m =  sorted(hash, key=lambda ch: hash[ch], reverse=True)
        ans = ""
        for ch in m:
            ans += ch * hash[ch]

        return ans
       
        
       

        
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {')' : '(','}':'{',']':'['}
        for ch in s:
            if ch not in d:
                st.append(ch)
            else:
                if not st:
                    return False
                top = st.pop()
                if d[ch]!=top:
                    return False
        return not st        
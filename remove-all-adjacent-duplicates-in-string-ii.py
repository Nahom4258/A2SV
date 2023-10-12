class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []

        for ch in s:
            if st:
                top_ch, count = st[-1]
                if top_ch == ch and count+1 == k:
                    for _ in range(k-1):
                        st.pop()
                    continue
                if top_ch == ch:
                    st.append((ch, count+1))
                else:
                    st.append((ch, 1))
            else:
                st.append((ch, 1))

        return ''.join([x[0] for x in st])
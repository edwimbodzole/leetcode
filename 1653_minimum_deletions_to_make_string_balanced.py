class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)

        b_left = 0
        a_right = s.count("a")

        best = min(N, b_left + a_right)
        for i in range(N):
            #moving the line from before s[i] to after s[i]
            if s[i] == 'a':
                a_right -= 1
            else:
                #if s[i] == 'b'
                b_left += 1

            best = min(best, b_left + a_right)

        return best

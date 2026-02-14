class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        champagne = [poured]

        for row in range(1, query_row + 1):
            new_champagne = [0.0] * (row + 1)

            for glass in range(len(champagne)):
                overflow = max(0, champagne[glass] - 1.)

                #left side
                new_champagne[glass] += overflow / 2.
                new_champagne[glass + 1] += overflow / 2.

            champagne = new_champagne

        return min(1.0, champagne[query_glass])

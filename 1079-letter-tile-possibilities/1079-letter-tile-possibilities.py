class Solution(object):
    def numTilePossibilities(self, tiles):
        c = [0]
        used = [False] * len(tiles)
        def permutations(newStr):
            for i in range(len(tiles)):
                if used[i]:
                    continue
                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                c[0] += 1
                permutations(newStr + tiles[i])
                used[i] = False
        tiles = sorted(tiles)
        permutations("")
        return c[0]
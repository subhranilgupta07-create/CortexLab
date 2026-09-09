class Solution(object):
    def bestHand(self, ranks, suits):
        c = 0
        for i in range (len(suits) - 1):
            if (suits[i] != suits[i + 1]):
                c = 1
        if (c == 0):
            return "Flush"   
        k = 0
        r = sorted(ranks)
        for i in range (len(r) - 1):
            if (r[i] == r[i + 1]):
                k += 1
            else:
                k = 0
            if (k == 2):
                return "Three of a Kind"       
        for i in range (len(r) - 1):
            if (r[i] == r[i + 1]):
                return "Pair"    
        return "High Card"            
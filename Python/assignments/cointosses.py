import random
def cointoss():
    heads = 0
    tails = 0
    for flip in range(1,2001):
        result = random.random()
        if round(result) == 1:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a {} ...Got {} head(s) so far and {}tail(s) so far".format(flip,"heads",heads, tails)
        else:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a {} ...Got {} head(s) so far and {}tail(s) so far".format(flip, "tails", heads, tails)

print(cointoss())

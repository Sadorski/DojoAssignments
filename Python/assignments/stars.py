def draw_stars(l):
    for val in l:
        if type(val) == str:
            print val[0]*len(val)
        else:
            print val*'*'

print draw_stars([3, "steve", "ray" , 5 , 6])

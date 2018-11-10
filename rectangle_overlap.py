def rectangle_overlap(rec1, rec2):
    [x1, y1, x2, y2] = rec1
    [w1, v1, w2, v2] = rec2
    if x1 >= w2 or y1 >= v2 or y2 <= v1 or x2 <= w1:
        return False
    else:
        return True

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]

print(rectangle_overlap(rec1, rec2))

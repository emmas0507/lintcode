# mock_hanoi_tower
# N: reprensents the number of plate
# start: the index of the start tower of all the plates, first tower is 0
# end: the inde of the end tower of all the plates, second tower is 1 and third tower is 2

def mock_hanoi_tower(N, start, end):
    if N == 0:
        return None
    if N == 1:
        print('move plate from {} to {}'.format(start, end))
        return None
    else:
        other = [x for x in [0, 1, 2] if x not in [start, end]][0]
        mock_hanoi_tower(N-1, start, other)
        mock_hanoi_tower(1, start, end)
        mock_hanoi_tower(N-1, other, end)
        return None

N = 3
mock_hanoi_tower(N, start=0, end=2)



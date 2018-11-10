def meeting_rooms(interval_list):
    min = 0
    max = 100000
    for interval in interval_list:
        if interval[0] > min:
            min = interval[0]
        if interval[1] < max:
            max = interval[1]
        if max < min:
            return False
    return True

interval_list = [[0,30],[5,10],[15,20]]
print(meeting_rooms(interval_list))

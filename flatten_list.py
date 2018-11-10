# list contains element of list, flatten list

def flatten_list(alist):
    flattened_list = []
    queue_list = []
    while len(alist) > 0:
        # put the next element in queue_list
        queue_list = queue_list + [alist[0]]
        alist = alist[1:]
        print('alist is')
        print(alist)
        while len(queue_list) > 0:
            process_element = queue_list[-1]
            print('process_element is')
            print(process_element)
            queue_list = queue_list[:-1]
            print('queue list is')
            print(queue_list)
            if type(process_element) == int:
                flattened_list = flattened_list + [process_element]
                pass
            elif len(process_element) == 0:
                pass
            else:
                queue_list = queue_list + process_element[1:] + process_element[0:1]
    return flattened_list

alist = [1, 2, [1, 2]]
result_list = flatten_list(alist)
print(result_list)

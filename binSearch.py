from math import floor
import mergeSort
import random
import time

def binarySearch(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = floor((low + high)/2)
        random_ISBN = A[mid][0]
        if random_ISBN == key:
            return mid
        elif key < random_ISBN:
            high = mid - 1
        else:
            low = mid + 1
    return -1


#run merge sort
sort_list = mergeSort.main(verbose=False)

#initialize running time
total_running_time = 0

#randomly select ISBN & search for it
for i in range(len(sort_list)):
    choose_book_record = random.choice(sort_list)
    select_ISBN = choose_book_record[0]
    
    #run binary search
    start_period = time.time() #get start time
    search_key = binarySearch(sort_list, select_ISBN)
    end_period = time.time() #get end time

    #compute running time
    run_time = (end_period - start_period) * 1000 
    total_running_time += run_time

print(f"{len(sort_list)}, {total_running_time:.0f}")


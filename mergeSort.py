from math import floor
import pandas as pd
import time


def merge_sort(A, p, r):
    if p < r:
        q = floor((p + r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return {'arr': A, 'size': len(A)}

def merge(A, p, q, r):
    nL = q - p + 1
    nR = r - q
    L = [0] * nL
    R = [0] * nR

    for i in range(0, len(L)):
        L[i] = A[p + i]
    for j in range(0, len(R)):
        R[j] = A[q + j + 1]
    i = 0
    j = 0
    k = p

    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1
   
def main (verbose=True):
    #get file path from user
    file_path = input('Input the file path of the data to be sorted:' )

    #read file into dataframe
    df = pd.read_csv(file_path, header=None)

    #convert to list
    arr = df.values.tolist()
    #save list items into new list
    new_list = []
    for item in arr:
        new_list.append(item)
    #get start time
    start_period = time.time()
    #call sort function 
    sorted_list = merge_sort(new_list, 0, len(new_list)-1)
    #get stop time
    end_period = time.time()
    #execution time in milliseconds
    run_time = (end_period - start_period) * 1000
    
    if verbose:
        print(f"{sorted_list['size']},{ run_time:.0f}")
    return sorted_list['arr']

if __name__ == "__main__":
    main()



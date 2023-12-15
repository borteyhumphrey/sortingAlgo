import pandas as pd
import time
import random
import argparse
import inspect

parser = argparse.ArgumentParser(description='Perform linear search on a list of fictitious book records')

parser.add_argument('file',type=str)

args = parser.parse_args()

'''
A Python program that uses the linear search algorithm to find randomly selected ISBN from a list of fictitious book records. The program returns the randomly selected ISBN and it's position in the list, and the size (of the list), and time taken to search for ISBNs
Author: Humphrey B. Borketey, borteyhumphrey@gmail.com
'''

#linear seach algorithm
def linear_search(arr, key):
    """Take a list of fictitious books `arr` and search for an ISBN `key` using Linear Search.

    Args:
        arr (list): The list of books.
        key (int): The ISBN to search for.

    Returns:
        list
    
    ValueError:
        Raises
            If ISBN `key` not found.
    """
    for i in range(len(arr)):
        if arr[i][0] == key:
            return i
    return -1


def main ():
    #get file path from user
    file_path = args.file

    #read file into dataframe
    df = pd.read_csv(file_path, header=None)

    #convert to list
    arr = df.values.tolist()
    #save list items into new list
    new_list = []
    for item in arr:
        new_list.append(item)
    
    #initialize runnning time
    total_run_time = 0

    #random ISBN selection
    for arr in range(len(new_list)):
        choose_book_record = random.choice(new_list)
        select_ISBN = choose_book_record[0]

        start_time = time.time() #get start time
        search = linear_search(new_list, select_ISBN) #search randomly selected ISBN
        end_time = time.time() #get end time

        #compute running time
        running_time = (end_time - start_time) * 1000
        total_run_time += running_time

        #print ISBN and position in list
        print(f"{select_ISBN} found at index {search}")
    
    print()

    #print size of list and runtime
    print(f"Data size: {len(new_list)}, Run time: {total_run_time:.0f}ms")

if __name__ == "__main__":
    main()


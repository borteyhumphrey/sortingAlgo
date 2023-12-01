import pandas as pd
import time
import random
import argparse

parser = argparse.ArgumentParser(description='Perform linear search on a list of fictitious book records')

parser.add_argument('file',type=str)

args = parser.parse_args()

'''
A Python program that uses the linear search algorithm to find randomly selected ISBN from a list of fictitious book records. The program returns the randomly selected ISBN and it's position in the list, and the size (of the list), and time taken to search for ISBNs
Author: Humphrey B. Borketey, borteyhumphrey@gmail.com
'''

#linear seach algorithm
def linearSearch(arr, key):
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
        search = linearSearch(new_list, select_ISBN) #search randomly selected ISBN
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


import math
import string

#binary search 
#searches sorted sequence for value toFind
#if found returns the index
#if not found returns -1
def binarysearch(seq , toFind):
    if not type(seq) in (tuple, list):
        return -1

    min = 0
    max = len(seq) -1
    guess = 0
    while max >= min:
        guess = (min + max) // 2;
        if seq[guess] == toFind:
            return guess
        elif seq[guess] < toFind:
            min = guess + 1
        else:
            max = guess -1
    
    return -1
    

def main():
    print("index: " + str(binarysearch([0,1,2,3,4,5,6,7,8,9], 4)))
    l = []
    l.extend(range(0 , 1000));
    print("index: " + str( binarysearch(l,  1001)))
    print("index: " + str(binarysearch( (0,1,2,3,4,5,6,7,8,9), 2)))
    print("index: " + str(binarysearch('A', 4)))
    print("index: " + str(binarysearch("ABCDEFG", 'E')))

if __name__ == '__main__':
    main()
""" This is a sudoku solver written  by Backtracking DFS algorithm. """

""" Try to fill the cells with one possibility, then if it breaks the rule, we will backtracking it to find the possible solution. When all solutions are found, we end the algorithm and print board out. """

import fileinput
import time


def make_board(a):
    """ This is used to make a sudoku board from a 2D list"""
    for row in range(9):
        s = '\t'
        for column in range(9):
            s = s + str(a[row][column])
            if (column+1) % 3 == 0:
                s = s + ' '
        print(s)
        if (row+1) % 3 == 0:
            print('')
    if column + 1 == 3 or column+1 == 6: #Make a '|' every 3 numbers and every 6 numbers in every row and col
        print(" | ")
        if row+1 == 3 or row+1 == 6:
            print(" | ")
        print()
    print()



def try_cell_possibility(a, row, column):
    """ Test the cell with the row number and the column number, and return back a list of numbers can be filled in this cell. """
    tried = [0]*10
    tried[0] = 1
    rowBlock = row // 3
    colBlock = column // 3


    for b in range(9):   #Test in each col and row
        tried[a[b][column]] = 1;
        tried[a[row][b]] = 1;


    for b in range(3):  #Test in every 3x3 sqaure box
        for c in range(3):
            tried[a[b+rowBlock*3][c+colBlock*3]] = 1
    return tried

def tryFillFirst(a):
    """ Try to solve the puzzle the first time by iterating through every cell, by checking each cell, get the possible numbers in the cell. If only one exists, fill in, do this until it stops."""

    #Set the needStop as a counter, so it determines if the algorithm needs to be stopped
    needStop = False

    while not needStop:
        needStop = True
        for row in range(9):  #Go through the puzzle and get the possible numbers in every cell
            for col in range(9):
                tried = try_cell_possibility(a, row, col)
                if tried.count(0) != 1:  #If the possible numbers is not equal to 0, we need to continue, if equal to 1 we can fill it in the cell, but in most cases, this is not going to happen
                    continue
                for b in range(1, 10):   #If there is only one possibility in the cell and the cell is empty, we can fill it in with the only number available.
                    if a[row][col] == 0 and tried[b] == 0:
                        a[row][col] = b
                        needStop = False
                        break

def BTDFSSlover(a, row, column, i):
    """ Recursively try to use DFS to get all the possible solutions for each cell, then use backtracking to eliminate the invalid possibilities, which is the pruning process."""

    if column == 9:
        row = row + 1
        column = 0

    if row == 8 and column == 8 :
        tried = try_cell_possibility(a, row, column)
        if 0 in tried:
            a[row][column] = tried[0]
            i[0] = i[0] + 1
        return True

    if a[row][column] == 0:
        tried = try_cell_possibility(a, row, column)
        for m in range(1, 10):
            if tried[m] == 0:
                a[row][column] = m
                if BTDFSSlover(a, row, column + 1, i):
                    i[0] = i[0] + 1
                    return True


        a[row][column] = 0
        return False

    return BTDFSSlover(a, row, column + 1, i)

def main():

    data_file = input('Please select a test file: (e.g.  easySudokus.txt or hardSudokus.txt): ')


    total_test = int(input('Please input a number to identify how many tests you want to process: '))
    
    #data_file = 'fileName.txt'
    puzzleNum = 0
    a = []
    t = ""
    i = [0]
    startTime = time.time()
    
    
    #for l in fileinput.input():
    with open(data_file) as f:
	
        for l in f.readlines()[0:total_test]:
            
            
            l = ' '.join(l.split())
            t = t + l
            
            while len(t) > 0:
                ll = []
                
                while len(ll) < 9:
                    if t[0].isdigit():
                        ll.append(int(t[0]))
                    t = t[1:]
            
                a.append(ll)
                
                if len(a) == 9:
                    puzzleNum = puzzleNum + 1
                    print("Puzzle Number {:d}".format(puzzleNum))
                    print("Original: ")
                    make_board(a)
                    
                    for l in a:
                        if 0 in l:
                            insideTime = time.time()
                            BTDFSSlover(a, 0, 0, i)
                            break
                
                    print("Solution: ")
                    make_board(a)
                    
                    print("="*53)
                    a = []
            
            print("Used {:.10f} seconds to solve total of {} puzzles".format(time.time() - startTime, puzzleNum))
            print("Used {:.10f} seconds to solve this puzzle".format(time.time() - insideTime))
            print("%d nodes generated in total"%i[0])
            print("="*53)
    f.close()

if __name__ == "__main__":
    main()



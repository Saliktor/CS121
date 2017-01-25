'''
Created on Jan 17, 2017

@author: Sal
'''
import re, sys, os
from time import clock

def setTokenize(f_name : str) -> {str}:
    
    #isascii = lambda s: len(s) == len(s.encode()) #Simple lambda function to test if a string is in all ascii characters
    
    tokens = set()
    
    with open(f_name, 'r') as f: #Handles opening and closing of file once finished
        for line in f:
            tokens.update([token.lower() for token in re.split('[^a-zA-Z0-9]', line) if token])
            
    return tokens

def printSetIntersection(token_set1: {str}, token_set2: {str}) -> None:
    token_set = set.intersection(token_set1, token_set2)
    for token in token_set:
        print(token)
    print("Matched Token Count:", len(token_set))

    
def checkPassedArguments() -> bool:
    if len(sys.argv) < 3: #No additional arguments were passed
        return False
    return True

def getFilesFromCommand() -> [str]:
    if not checkPassedArguments():
        print("Need to pass two files with execution of script")
        sys.exit()
    
    f_name1 = sys.argv[1]
    f_name2 = sys.argv[2]
    
    if not os.path.isfile(f_name1):
        print("File", f_name1, "does not exist")
        sys.exit()
        
    if not os.path.isfile(f_name2):
        print(f_name2, "does not exist")
        sys.exit()
        
    return [f_name1, f_name2]

def main():
    f_names = getFilesFromCommand()
    
    token_set1 = setTokenize(f_names[0])
    token_set2 = setTokenize(f_names[1])
    printSetIntersection(token_set1, token_set2)


if __name__ == '__main__':
    start = clock()
    
    main()
    
    end = clock()
    print("Total Execution Time:", end-start, "sec")
    


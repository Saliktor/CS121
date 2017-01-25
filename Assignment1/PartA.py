'''
Created on Jan 17, 2017

@author: Sal
'''
import re, sys, os
from time import clock

def tokenize(f_name : str) -> [str]:

    #isascii = lambda s: len(s) == len(s.encode()) #Simple lambda function to test if a string is in all ascii characters
    
    tokens = []
    
    with open(f_name, 'r') as f: #Handles opening and closing of file once finished
        for line in f:
            tokens += [token.lower() for token in re.split('[^a-zA-Z0-9]', line) if token]
            
    return tokens

def computeWordFrequencies(tokens: [str]) -> {str:int}:
    token_map = {}
    
    for token in tokens:
        if token in token_map:
            token_map[token] += 1
        else:
            token_map[token] = 1
    
    return token_map

def printTokens(token_map: {str:int}) -> None:
    sorted_map = sorted(token_map.items(), key = lambda x: x[1], reverse = True)
    for token, count in sorted_map:
        print(token,":",count)

    
def checkPassedArguments() -> bool:
    if len(sys.argv) == 1: #No additional arguments were passed
        return False
    return True

def getFileFromCommand() -> str:
    if not checkPassedArguments():
        print("No file was passed in with execution of script")
        sys.exit()
    
    f_name = sys.argv[1]
    
    if not os.path.isfile(f_name):
        print("File", f_name, "does not exist")
        sys.exit()
        
    return f_name
    
def main() -> None:    
    f_name = getFileFromCommand()
    tokens = tokenize(f_name)
    token_map = computeWordFrequencies(tokens)
    printTokens(token_map)

if __name__ == '__main__':
    start = clock()
    
    main()
    
    end = clock()
    print("Total Execution Time:", end-start, "sec")
    

        

    

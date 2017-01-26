'''
Created on Jan 17, 2017

@author: Sal
'''
import re, sys, os
from time import clock


#Takes file name and will return map containing all tokens within file with frequency value
def tokenize(f_name : str) -> {str:int}:

    #isascii = lambda s: len(s) == len(s.encode()) #Simple lambda function to test if a string is in all ascii characters
    
    tokens = []
    tokens_map = {}
    
    with open(f_name, 'r') as f: #Handles opening and closing of file once finished
        for line in f:
            tokens += [token.lower() for token in re.split('[^a-zA-Z0-9]', line) if token]
            if len(tokens) > 10000: #If list contains more than 10000 elements then we dump into map to avoid memory issues
                tokens_map = computeWordFrequencies(tokens, tokens_map)
                tokens.clear()

    return computeWordFrequencies(tokens, tokens_map) #One last dump of token list into map

#Takes in list of tokens and applies to passed in map by adding to already existing key or creating new one
def computeWordFrequencies(tokens: [str], token_map: {str: int}) -> {str:int}:
    for token in tokens:
        if token in token_map:
            token_map[token] += 1
        else:
            token_map[token] = 1
    
    return token_map

#Prints out each token in map and its frequency value
def printTokens(token_map: {str:int}) -> None:
    sorted_map = sorted(token_map.items(), key = lambda x: x[1], reverse = True)
    for token, count in sorted_map:
        print(token,":",count)


#Checks to proper amount of arguments are passed through command line
def checkPassedArguments() -> bool:
    if len(sys.argv) == 1: #No additional arguments were passed
        return False
    return True

#Checks to ensure file was passed from command line and that it exist
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
    token_map = tokenize(f_name)
    printTokens(token_map)

if __name__ == '__main__':
    start = clock()
    
    main()
    
    end = clock()
    print("Total Execution Time:", end-start, "sec")
    

        

    

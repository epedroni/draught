import os
import re

def prompt(directory):
    
    fileList = list()
    index = 0
    
    if os.path.isdir(directory):
        for root, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                fileList.append([root, filename])
                print("\t", index, ":", filename)
                index += 1
        print("\t q : quit")
        print("Choose one or more files: ", end="")
        
        rawInput = input().strip()
        # check that input consists of integers and spaces only
        if re.search("[^0-9 ]", rawInput) == None:
            selectedFiles = set(re.split(" +", rawInput))
            for selection in selectedFiles:
                index = int(selection)
                if index < len(fileList):
                    yield fileList[index]
                else:
                    print(selection + " does not correspond to a file, skipping...")
        elif rawInput == "q":
            return
        else:
            raise Exception(rawInput + " is not a valid input")  
    else:
        raise Exception(path + " is invalid")


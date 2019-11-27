import os
import fnmatch

testdir1 = 'D:/Google_Drive/1.Work' 

# 判斷patterns
def is_file_match(filename, patterns):
    for i in patterns:
        if fnmatch.fnmatch(filename, i):
            return True
        return False 

def find_specific_files(path, patterns=['*'], exclude_dir=[]):
    for path, dirnames, filenames in os.walk(path):
        print(dirnames)

if __name__ == "__main__":
    find_specific_files(testdir1)
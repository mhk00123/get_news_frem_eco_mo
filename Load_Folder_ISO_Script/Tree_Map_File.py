import os
import os.path

rootdir = 'C:/Users/leotam/CPTTM/IST - 文件/Projects'
testdir = 'C:/Users/leotam/Desktop/Sample File'

def get_path(path, dirName):
    new_path = path  + '/' + dirName
    return new_path

def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        flag = os.path.isdir(get_path(path, item))
        if(flag):
            # print(item)
            print("|    "  * depth + "+--" + item)
            f.write("|    "  * depth + "+--" + item + '\n')
            
        if(('.docx' in item) or ('.pdf' in item)):
            print("|    "  * depth + "+--" + item)
            f.write("|    "  * depth + "+--" + item + '\n')
        flag = False
        newitem = path +'/'+ item
        if os.path.isdir(newitem):
            dfs_showdir(newitem, depth +1)
        
        f.write('\n')

if __name__ == '__main__':
    f = open("Tree_Map_File.txt", "w+", encoding="utf-8")
    dfs_showdir(rootdir , 0)
    f.close()

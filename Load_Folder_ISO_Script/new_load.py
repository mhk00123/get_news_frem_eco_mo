import os
import os.path

#1.  一層目錄掃瞄
def search_layer1(path):
    for root, dirs, files in os.walk(path):
        return dirs

#2.  二層目錄掃瞄
def search_layer2(path):
    for root, dirs, files in os.walk(path):
        return files

#3.  各目錄文件
#3.1 new Path
def get_new_path(path, dirName):
    new_path = path  + '/' + dirName
    return new_path

rootdir = 'C:/Users/leotam/CPTTM/IST - 文件/Projects'


taget_str1 = 'proposal'
taget_str2 = 'report'

flag = True

tempFile = []

if __name__ == '__main__':
    #1
    layer_one_dir = search_layer1(rootdir)
    f = open("New.txt", 'w+')
    #2
    for d in layer_one_dir:

        new_path = get_new_path(rootdir, d)
        tempFile = search_layer2(new_path)

        for i in tempFile:
            s = i.lower()
           
           
        if(flag):
            print(d)
            f.write(d + '\n')

        # clean
        flag = True
        tempFile = []
    
    f.close()
    

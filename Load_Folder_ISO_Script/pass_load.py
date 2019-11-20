import os
import os.path

#1.  一層目錄掃瞄
def search_layer(path):
    for root, dirs, files in os.walk(path):
        return dirs

#2.  二層目錄掃瞄
def search_files(path):
    for root, dirs, files in os.walk(path):
        return files

#3.  各目錄文件
#3.1 new Path
def get_new_path(path, dirName):
    new_path = path  + '/' + dirName
    return new_path

rootdir = 'C:/Users/leotam/CPTTM/IST - 文件/Projects/Past Projects 已完成'

taget_str1 = 'proposal'
taget_str2 = 'report'

flag = True

tempFile  = []
tempFile2 = []
tempFile3 = []

if __name__ == '__main__':
    f = open("Old.txt", 'w+')

    tempFile = search_layer(rootdir)
    for i in tempFile:
        new_path = get_new_path(rootdir,i)
        if(os.path.isdir(new_path)):
            tempFile2 = search_layer(new_path)
            for j in tempFile2:
                new_path2 = get_new_path(new_path, j)
                if(os.path.isdir(new_path2)):
                    tempFile3 = search_layer(new_path2)
                    for k in tempFile3:
                        s = i.lower()
                        if(s.find(taget_str1)>=0):
                            flag = False
                    if(flag):
                        print(i + " " + j)
                        f.write(i + " " + j +"\n")

            #clean            
            flag = True
            tempFile3 = []
        tempFile2 = []
    f.close()
import os 

testdir1 = 'D:/Google_Drive/1.Work/' 
temp = ''


def list_files(startpath): 
    flag = 0
    temp3 = ''
    for root, dirs, files in os.walk(startpath):
        if(flag!=0):
            # print(root)
            # 把path換成空白，由於path帶'/'，換成空白後統計後方'\'數，用作判斷層數
            temp  = root.replace(startpath, '')
            temp2 = temp.split('\\')[0]
            if(temp3 != temp2):
                print()
                temp3 = temp2

            level = temp.count(os.sep)
            # print(root.replace(startpath, ''))
            if(level > 2):
                continue
            indent = '|' + '*' * 2 * (level+1) + '+ '
            print('{}{}/'.format(indent, os.path.basename(root))) 
            subindent =  '|'+' ' * 2 * (level+1) + '|' + '--' * (level)
            for f in files:
                if(('.docx' in f) or ('.pdf' in f)):
                    print('{}{}'.format(subindent, f))
        flag = 1

if __name__ == "__main__":
    list_files(testdir1)
from PyPDF2 import PdfFileReader
import os
from time import sleep 
from subprocess import call
from banner import banner


print('[+]- Processing PDF Files')
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
    
    #print(info)
    return info

if __name__ == '__main__':
    banner()
    arr = os.listdir('pdf/')
    print('[+]- Extracting Users From PDF')
    users=[]
    for file in arr:
        path = 'pdf/'+file
        file = get_info(path)
        users.append(file)

    usernames=[]
    print('[+]- Formating Users')
    for file in users:
        tmList=[]
        tmpFile = str(file)
        tmpFile = tmpFile[0:-2]
        tmList.append(tmpFile.split(' '))
        usernames.append(tmList[0][1][1:])

    print('[+]- Removing Duplicated Users')
    setUsers = set(usernames)
    finalUsers = list(setUsers)    
    print('[+]- Writing Users To File')    
    with open('endUsers.txt', 'w') as f:
        f.writelines("%s\n" % user for user in finalUsers)
    totUsersFound = len(finalUsers)

    f.close()
    choice = input('Wish to view the file? [y/n]: ')
    if choice == 'y' or choice == 'Y':
        if os.name == 'nt': #checks if user is using windows OS
            script ="type endUsers.txt"
        else:
            script = "cat endUsers.txt"
        
        print('[+]- enUsers FILE\n=================')
        call(script, shell=True)
    print('[+]- Total Users Found: ', totUsersFound)
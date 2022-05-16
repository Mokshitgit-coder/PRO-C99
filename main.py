from stat import ST_CTIME
import time
import os
import shutil
def main ():
    path="/Users/Mokshit/Desktop/Python"
    days= 180
    seconds= time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folders,folders,files in os.walk(path):
            if seconds >= os.stat(root_folders).st_ctime:
                shutil.rmtree(root_folders)
            else:
                for folder in folders:
                    folder_path= os.path.join(root_folders,folder)
                    if seconds >= os.stat(folder_path).st_ctime:
                        shutil.rmtree(folder_path)
                for file in files:
                    file_path= os.path.join(root_folders,file)
                    if seconds>= os.stat(file_path).st_ctime:
                        os.remove(file_path)
    else:
        print ("PATH DOES NOT EXIST")
main()
            
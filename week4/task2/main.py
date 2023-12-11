import os
import time
'''
functions
    list_files
    created_or_modified -st_mtime- -st_ctime-
    append_time_stamp
    create_folder
    move_files
'''
def list_files():
    files=[]
    for a_file in os.scandir():
        if a_file.is_file():
            files.append(a_file.name)

    return files

def created_or_modified_24(my_file):
    my_path=os. getcwd()+'/'+my_file
    crtd=os.stat(my_path).st_ctime
    mdfd=os.stat(my_path).st_mtime
    now=time.time()

    crtd_hr=(now-crtd)/3600
    mdfd_hr=(now-mdfd)/3600
    print(str(now)+' '+str(crtd)+' '+str(crtd_hr)+' '+ my_file)

    if crtd_hr<=24 or mdfd_hr<=24:
        return True
    return False

def append_time_stamp(my_file):
    file = open(my_file, "a")
    file.write(str(time.time())+'\n')
    file.close()

def create_folder():
    import os
    path = "last_24hours"
    if os.path.isdir(path):
        print("The folder already exists")
    else:
        os.mkdir(path)


def move_files():
    cwd = os.getcwd()
    create_folder()
    files=list_files()
    for file in files:
        if created_or_modified_24(file) and file != 'main.py':
            append_time_stamp(file)
            src = os.path.join(cwd, file)
            dst = os.path.join(cwd, "last_24hours", file)
            os.rename(src, dst)

move_files()

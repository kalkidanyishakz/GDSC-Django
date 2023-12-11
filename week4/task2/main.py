import os
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

created_or_modified_24('main.py')
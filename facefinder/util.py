import os

'''
Generator of all files with a certain file ending in a path
'''
def next_file(path, ending):
    for fi in os.listdir(path):
        abs_path = '%s/%s' % (path, fi)
        if os.path.isdir(abs_path):
            for gen_fi in next_file(abs_path, ending):
                yield gen_fi
        elif fi.endswith(ending):
            yield abs_path 

def file_name_from_path(path):
    arr = path.split('/')
    return arr[len(arr)-1]

def file_and_dir_name_from_path(path):
    arr = path.split('/')
    file_name = arr[len(arr)-1]
    dir_name = arr[len(arr)-2]
    return [file_name, dir_name]

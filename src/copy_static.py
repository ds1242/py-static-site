import os
import shutil

def create_file_path(path, output_list):
    path_list = []
    if not os.path.exists(path):
        raise Exception('not a valid path')
    
    if os.path.isfile(path):
        output_list.append(path)
    else:
        path_list = os.listdir(path=path)

    for current_path in path_list:
        curr_path = os.path.join(path, current_path)
        if os.path.isfile(curr_path):
            output_list.append(curr_path)
        else:
            create_file_path(curr_path, output_list)
    return output_list


def copy_files(path_list, destination):
    if not os.path.exists(destination):
        raise Exception('destination path does not exist')

    if len(path_list) == 0:
        raise Exception('no source available')
    
    for path in path_list:
        shutil.copy(path, destination, )


def trim_path_list(path_list, start_path):
    trimmed_list = []
    for path in path_list:
        trimmed_list.append(path[len(start_path):])
    return trimmed_list

    
    
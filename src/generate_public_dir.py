import os
import shutil

def recursive_move(src, dst):
    if not(os.path.exists(dst)):
        os.mkdir(dst)
    for entry in os.listdir(src):
        print(entry)
        if os.path.isfile(os.path.join(src, entry)):
            shutil.copy(os.path.join(src, entry), dst)

        else:
            recursive_move(os.path.join(src, entry), os.path.join(dst, entry))



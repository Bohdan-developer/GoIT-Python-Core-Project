#Shows which files are older than X and removes them if uncommented
import os, time

def file_age(x_days: int):
    path = "."
    now = time.time()

    try:
        for filename in os.listdir(path):
            filestamp = os.stat(os.path.join(path, filename)).st_mtime
            filecompare = now - x_days * 86400
            if  filestamp < filecompare:
                print(filename)
                #if os.path.isfile(f):
                #os.remove(os.path.join(path, f))
    except:
        print("Cannot convert input to integer")
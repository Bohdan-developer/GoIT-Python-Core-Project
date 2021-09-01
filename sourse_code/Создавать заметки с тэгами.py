#File with Note and Tags create
import time


def Create_new_note():

    randomData = ("\n\n") #file filling
    t,s = str(time.time()).split('.')
    filename = t+".txt" #Name would be similar to 1630063227.txt
    print ("writing to", filename) #Display in console
    try:
        with open(filename, "a") as file:
            file.write(randomData)
            file.close()
    except IOError:
        print("File not accessible")

    Tag_update(filename)
    Note_update(filename)
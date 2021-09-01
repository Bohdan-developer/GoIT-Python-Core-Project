#Search for a Note
import os


def Note_Search(note: str):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    flist = []

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for filename in files:
        try:
            with open(os.path.join(__location__, filename), encoding='utf-8') as currentFile:
                text = currentFile.readlines()
                if (note.lower() in text[1].lower()): #Note we're looking for in the second line, lowercase
                    flist.append(filename[:-4])
        except:
            print(f"{filename} contains less than 2 strings or cannot be opened")

    result = Counter(flist)
    print("Matches in Files:")
    for key, value in result.items():
        print(f'{value} : {key}')
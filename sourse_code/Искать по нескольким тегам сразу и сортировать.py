#Search for up to 6 tags and sort by frequency
import os
from collections import Counter


def Tag_Search_Helper(tag: str, flist: list, filename: str, text: str):
    if tag != '%%%%%%%%%%' and (tag.lower() in text[0].lower()): #Tag we're looking for in the first line, lowercase
        flist.append(filename[:-4])
    return flist

def Tag_Search(tag: str, tag1 : str = '%%%%%%%%%%', tag2 : str = '%%%%%%%%%%', tag3 : str = '%%%%%%%%%%', tag4: str = '%%%%%%%%%%', tag5 : str = '%%%%%%%%%%'):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    flist=[]

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for filename in files:
        try:
            with open(os.path.join(__location__, filename), encoding='utf-8') as currentFile:
                text = currentFile.readlines()
                flist = Tag_Search_Helper(tag, flist, filename, text)
                flist = Tag_Search_Helper(tag1, flist, filename, text)
                flist = Tag_Search_Helper(tag2, flist, filename, text)
                flist = Tag_Search_Helper(tag3, flist, filename, text)
                flist = Tag_Search_Helper(tag4, flist, filename, text)
                flist = Tag_Search_Helper(tag5, flist, filename, text)

        except:
            print(f"{filename} contains less than 2 strings or cannot be opened")

    result = Counter(flist)
    print("Matches in Files:")
    for key, value in result.items():
        print(f'{value} : {key}')
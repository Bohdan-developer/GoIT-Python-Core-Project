from pathlib import Path
import os
import shutil
import sys


def normalize(filename):

    Table={'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd',
    'Е': 'E', 'е': 'e', 'Ё': 'Io', 'ё': 'io', 'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i',
    'Й': 'J', 'й': 'j', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't',
    'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh', 'Ц': 'Ts', 'ц': 'ts', 'Ч': 'Ch', 'ч': 'ch',
    'Ш': 'Sh', 'ш': 'sh','Щ': 'Shch', 'щ': 'shch', 'Ь': "'", 'ь': "'", 'Ы': 'Y', 'ы': 'y', 'Ъ': "", 'ъ': "",
    'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia', 'Ї': 'Ji', 'ї': 'ji', 'І': 'I', 'і': 'i',
    'Ґ': 'G', 'ґ': 'g'}
    Restricted = ('#', '<', '$', '+', '%', '>', '!', '`', '&', '*', "'", '|', '{', '?', '"', '=', '}', '/', ':', '\\', '@')
    latin = ''
    
    for char in filename:
        transchar = ''
        if char in Table:
            transchar = Table[char]
        elif char in Restricted:
            continue
        else:
            transchar = char
        latin += transchar
    return latin


def create_new_folders(path):

    Imgdir = path/'Images'
    Docdir = path/'Documents'
    Audir = path/'Audio'
    Vidir = path/'Video'
    Arcdir = path/'Archives'
    Othdir = path/'Other'

    if not os.path.exists(Imgdir):
        os.mkdir(Imgdir)
    if not os.path.exists(Docdir):
        os.mkdir(Docdir)
    if not os.path.exists(Audir):
        os.mkdir(Audir)
    if not os.path.exists(Vidir):
        os.mkdir(Vidir)
    if not os.path.exists(Arcdir):
        os.mkdir(Arcdir)
    if not os.path.exists(Othdir):
        os.mkdir(Othdir)

    return (Imgdir, Docdir, Audir, Vidir, Arcdir, Othdir)


def file_normalization(path):

    normalized_filename = normalize(path.stem) #Не обработает двойные расширения .tar.gz
    return normalized_filename


def sorting_files(path, new_folders):

    Imgdir, Docdir, Audir, Vidir, Arcdir, Othdir = new_folders
    normalized_name = file_normalization(path)

    if path.suffix in ('.jpeg', '.png', '.jpg', '.svg'): path.replace(Imgdir / (normalized_name + path.suffix))
    elif path.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'): path.replace(Docdir / (normalized_name + path.suffix))
    elif path.suffix in ('.mp3', '.ogg', '.wav', '.amr'): path.replace(Audir / (normalized_name + path.suffix))
    elif path.suffix in ('.avi', '.mp4', '.mov', '.mkv'): path.replace(Vidir / (normalized_name + path.suffix))
    elif path.suffix in ('.zip', '.gz', '.tar'):
        shutil.unpack_archive(path, (Arcdir / normalized_name))
        os.remove(path)
    elif path.is_file(): path.replace(Othdir / (normalized_name + path.suffix))


def folder_processing(path, new_folders):

    if path.is_dir() and path not in new_folders:
        for fullpath in path.iterdir():
            folder_processing(fullpath, new_folders)
        if not os.listdir(path):
            path.rmdir()
    else:
        sorting_files(path, new_folders)


def main():

    path = sys.argv[1]
    #path = (r'C:\Users\vlady\Desktop\testfolder')
    path = Path(path)

    if path.exists():
        new_folders = create_new_folders(path)
        folder_processing(path, new_folders)
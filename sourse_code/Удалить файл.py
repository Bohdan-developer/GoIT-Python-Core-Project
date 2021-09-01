#Delete Notes completely (with a file)
def remove_file(filename):
    path = os.getcwd()
    if os.path.isfile(filename):
        os.remove(os.path.join(path, filename))
        print(f'{filename} deleted')
		
		
#Or
filename = input("Enter FileName: ")
choice = input(f"You're going to delete {filename}. Confirm? (Y/N)")
	if choice in ('Y','y'):
		if os.path.exists(filename):
			os.remove(filename)
			print(f"File {filename} successfully removed")
		else:
			print("The file does not exist")
	else:
	print("I will keep it to myself then")

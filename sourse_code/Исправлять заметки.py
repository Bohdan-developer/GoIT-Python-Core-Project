#Note update
def Note_update(file_to_open: str):
    #file_to_open = 'data.txt' #filename input.

    try:
        with open(file_to_open, 'r') as file:
            data = file.readlines()
            file.close()
        
        print('Current note is:')
        print(data[1][:-1])
        note = input("Update a note: ") + '\n' #note input
        data[1] = note
        print(f'Note updated to: {note}')

        with open(file_to_open, 'w') as file:
            file.writelines(data)
            file.close()

    except IOError:
        print("File not accessible")
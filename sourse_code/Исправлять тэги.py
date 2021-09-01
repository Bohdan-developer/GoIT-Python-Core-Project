#Tag update
def Tag_update(file_to_open: str):
    #file_to_open = 'data.txt' #filename input.

    try:
        with open(file_to_open, 'r') as file:
            data = file.readlines()
            file.close()
        
        print('Current tags are:')
        print(data[0][:-1])
        tags = input("Write tags: ") + '\n' #tags input
        data[0] = tags
        print(f'Tags updated to: {tags}')

        with open(file_to_open, 'w') as file:
            file.writelines(data)
            file.close()

    except IOError:
        print("File not accessible")
import os


folder_path = './static/Certificates'
output_file = './static/File_list.txt'

if os.path.exists('./static/File_list.txt'):
    os.remove('./static/File_list.txt')


# Get a list of all filenames in the folder
filenames = os.listdir(folder_path)

with open(output_file, 'w') as file:
    for filename in filenames:
        file.write(filename + '\n')

print(f'List of filenames has been saved to {output_file}')

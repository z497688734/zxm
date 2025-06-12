import os
def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            newFileName = file_name
            fileName = os.path.join(root, file_name)
            if file_name.endswith('.ibd'):
                print(f"文件: ", fileName)
                command = "python3 main.py "+ fileName +" --ddl --sql > " + newFileName + ".sql"
                os.system(command)

directory_path = "./data/gcb3"
if __name__ == '__main__':
    traverse_directory(directory_path)
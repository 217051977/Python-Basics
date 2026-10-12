from DownloadFiles import download

file_name = "Example1.txt"
download(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt",
    file_name
)

def read_file():
    file = open(file_name, "r")
    print(file)
    print(file.name)
    print(file.mode)
    print("\nReading file content")
    file_content = file.read()
    print(file_content)
    print(type(file_content))
    print("\nClose file")
    file.close()

def better_way_to_read_a_file():
    print("\nBetter way to read a file")
    with open(file_name, "r") as file:
        file_content = file.read()
        print(file_content)
    file.close()

def read_a_file_but_just_the_first_4_chars():
    print("\nRead just the first 4 chars of the file")
    with open(file_name, "r") as file:
        file_content = file.read(4)
        print(file_content)
    file.close()

def read_first_file_line():
    print("\nRead first line of the file")
    with open(file_name, "r") as file:
        file_content = file.readline()
        print(file_content)
    file.close()

def read_all_file_lines_with_interation():
    print("\nRead all lines of the file using an interation")
    with open(file_name, "r") as file:
        i = 0
        for line in file:
            print("Iteration", str(i), ": ", line)
            i = i + 1
    file.close()

def read_all_file_lines_as_list():
    print("\nRead all lines of the file")
    with open(file_name, "r") as file:
        file_content = file.readlines()
        print(type(file_content))
        print(file_content)
    file.close()

read_file()
better_way_to_read_a_file()
read_a_file_but_just_the_first_4_chars()
read_first_file_line()
read_all_file_lines_with_interation()
read_all_file_lines_as_list()
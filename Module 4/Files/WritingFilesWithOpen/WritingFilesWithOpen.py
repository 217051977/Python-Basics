def get_file_name(i):
    return f"Example{i}.txt"

def create_file_content_line(i = 1):
    file_content = ""
    if i > 1:
        file_content += "\n"
    file_content += f"This is line {i}"
    return file_content

def read_file_line(i):
    with open(get_file_name(i), "r") as file:
        print(file.readlines())
    file.close()

def write_file():
    with open(get_file_name(1), "w") as file:
        file.write(create_file_content_line())
    file.close()

def write_file_with_multiple_lines():
    print("\nWrite file with multiple lines")
    with open(get_file_name(2), "w") as file:
        file.write(create_file_content_line())
        file.write(create_file_content_line(2))
    file.close()

def write_file_with_a_list_content(l):
    print("\nWrite file with list content")
    with open(get_file_name(3), "w") as file:
        for item in l:
            print(item)
            file.write(item)
    file.close()

def write_file_and_then_overwrite_it():
    print("\nWrite file and then overwrite it:")
    print("Write file")
    with open(get_file_name(4), "w") as file:
        file.write(create_file_content_line())
    file.close()
    read_file_line(4)
    print("Overwrite file")
    with open(get_file_name(4), "w") as file:
        file.write(create_file_content_line(4))
    file.close()
    read_file_line(4)

def write_file_and_then_append_to_it():
    print("\nWrite file and then append to it:")
    print("Write file")
    with open(get_file_name(5), "w") as file:
        file.write(create_file_content_line())
    file.close()
    read_file_line(5)
    print("Append to file")
    with open(get_file_name(5), "a") as file:
        file.write(create_file_content_line(4))
    file.close()
    read_file_line(5)

def write_file_and_then_read_it():
    print("\nWrite file and then read it:")
    print("Write file")
    with open(get_file_name(6), "w+") as file:
        file.write(create_file_content_line())
        print("Reset pointer")
        print(f"{file.tell()} -> {file.seek(0,0)} ({file.tell()})")
        print("Read file")
        print(file.readlines())
    file.close()

def copy_file():
    print("\nCopy file:")
    print("Write file")
    with open(get_file_name(7), "w") as file:
        file.write(create_file_content_line(7))
    file.close()
    print("Copy file")
    with open(get_file_name(7), "r") as file:
        with open(get_file_name(8), "w") as copied_file:
            for line in file:
                copied_file.write(line)
        copied_file.close()
    file.close()

write_file()
write_file_with_multiple_lines()
write_file_with_a_list_content([create_file_content_line(), create_file_content_line(2), create_file_content_line(3)])
write_file_and_then_overwrite_it()
write_file_and_then_append_to_it()
write_file_and_then_read_it()
copy_file()
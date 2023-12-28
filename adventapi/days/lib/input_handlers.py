def read_file(input_file):
    with open(input_file, "r") as file:
        return file.read()

def read_lines(input_file):
    with open(input_file, "r") as file:
        return file.readlines()

def split_content(file_content):
    return file_content.split('\n')


def double_split_content(file_content):
    return file_content.split('\n\n')

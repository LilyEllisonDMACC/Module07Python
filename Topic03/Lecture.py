import os as os

#write to a file before read from a file
def write_numbers_to_file():
    f = open('testscores.txt', 'w')
    for x in range(0,22):
        f.write(str(x) + "\n")
    f.close()


#read
def read_file_lines():
    list_int = []
    with open('testscores.txt', 'r') as file:
        for line in file:
            line = line.strip()
            try:
                line = int(line)
                list_int.append(line)
            except:
                print("Failed to convert for: " + str(line))
    return  list_int

def square_list(a_list):
    final_list = []
    for item in a_list:
        final_list.append(item**2)
    return final_list

def overwrite_numbers_to_file(a_list):
    f = open('testscores.txt', 'w')
    for x in a_list:
        f.write(str(x) + "\n")
    f.close()

if __name__ == "__main__":
    #write_numbers_to_file()
    a_list = read_file_lines()
    print(a_list)
    a_square_list = square_list(a_list)
    print(a_square_list)
    overwrite_numbers_to_file(a_square_list)

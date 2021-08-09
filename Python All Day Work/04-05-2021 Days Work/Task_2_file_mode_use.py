# file mode handling

# for opening file:
# Function: open(param1, param2, param3)

# param1: file name
# param2: access mode
# param3: Buffering

# file opening and read

open_file = open('test.txt')
file_read = open_file.read()
print('Read a file',file_read)
open_file.close()


# file write

write_file = open('test_1.txt', mode='w+' )
write_file.write('I am learing python programming')
write_file.seek(0)
print(write_file.read())
write_file.close()

# write_new_file = open('test_2.txt', 'w')
# write_new_file.write('line number one !')
# print("write test_2::"write_new_file.read())
# write_new_file.close()

# file Append

append_file = open("test_2.txt", 'a')
append_file.write("\n Hello python append methods")
print(append_file)
append_file.close()


# Using with

with open('test.txt', mode='r') as f:
    file_data = f.read()
    print(file_data)

# using readline

with open("test.txt", 'r') as f:
    lines = f.readlines()
    print(lines)
    print('\n', lines[1])
    
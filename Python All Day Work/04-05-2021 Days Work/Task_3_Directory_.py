import os

# dir_1 = os.getcwd()
# print('directory  : ',dir_1)

# dir_2 = os.getcwdb()
# print(dir_2)



# current Directory
directory = os.getcwd()
print("current Dir : ", directory)


# # changing dircetory
# os.chdir('E:\\Computer all Subject Study\\Python\\Python Crouse')
# print('Current dir after change : ', os.getcwd())

# list dir files and folders

print("current directory : ", os.getcwd())

dir_info = os.listdir()
print("dir info: ", dir_info)


# creating a new directory

os.mkdir('Make_a_new_folder')
print(os.listdir('Make_a_new_folder'))

#rename a dir or file

# os.rename('Make_a_new_folder', 'change_name_folder')
# print(os.listdir())

os.remove('test.txt')
print(os.listdir())

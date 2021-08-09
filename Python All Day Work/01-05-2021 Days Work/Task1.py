# python program to Check vowel to consonant

input_Charecter = input('Enter a character: ')
Input = input_Charecter.lower()# use lower function


if (Input == 'a' or Input == 'e' or Input =='i' or Input == 'o' or Input == 'u'):
    #(Input == 'A' or Input == 'E' or Input == 'I' or Input == 'O' or Input == 'U') use capital letter
    print(Input, "is a Vowel")
else:
    print(Input, "is a Consonant")
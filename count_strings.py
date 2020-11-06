#3. Count the number of strings where the string length is 2 or more and the first and
#last character are the same from a given list of strings.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
#Accept a list of comma-separated strings
#Iterate through list, and check length >= 2
#Compare first and last character & increment counter if equal
input_str = input("Please enter a string: ")
str_list = [x for x in input_str.split(',') if x.strip()]
counter = 0
for element in range(0, len(str_list)):
    if(len(str_list[element]) >= 2):
        str = str_list[element] #initializing a new string equal to the current list item
        if(str[0] ==  str[len(str) - 1]):
            counter += 1
print(counter)
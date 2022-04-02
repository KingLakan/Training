# with open("../dummy.txt", 'w') as file_object:
#    file_object.write("hello\n")
with open("../dummy.txt", 'a') as file_object:
    file_object.write("röv\n")
    file_object.write("röv\n")
    file_object.write("röv\n")
print("append")

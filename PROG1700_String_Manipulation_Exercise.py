#Declare list of names
names = ("Mike", "Harper", "Tike", "Carter", "Porter", "Parker")
#Adding ::-1 at the end of the code will make whatever is written out be written backwards
for name in names[::-1]:
    print(name[::-1])

my_name = "Nicholas" # my_name actually stores [N, i, c, h, o, l, a, s]
print(my_name[0])
print(my_name[1])
print(my_name[2])
print(my_name[3])
print(my_name[4])
print(my_name[5])
print(my_name[6])
print(my_name[7])

print(len(my_name))
#Get the last letter of my_name
print(my_name[len(my_name) - 1])

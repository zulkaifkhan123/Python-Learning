"""
dictonary and sets practice questions

WAP to enter three subjects marks and store them in a dictoanry
Start with an empty dictonary and addd one by one . Use subject name as
key and marks as value

"""

computer = int(input("Enter Computer Subject Marks ! "));
phy = int(input("Enter physics Subject Marks ! "));
math = int(input("Enter maths Subject Marks ! "));

Subjects = {}
Subjects.update({"Computer" : computer})
Subjects.update({"physics" : phy})
Subjects.update({"maths" : math})

print(Subjects);

"""
WAP figure out to store 9 and 9.0 in a set separatly

"""

new_set = {9 ,"9.0"};
print(new_set) # will store both 
# here if i didn't change the type of 9.0 to string the set will delete it automatically
# and will just store 9
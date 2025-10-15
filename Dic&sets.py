"""

A dictionary is a collection of key-value pairs where
 each key is unique and used to access its value.
It is mutable (changeable) and stores data in the form of a map.

A set is a collection of unique and unordered elements.
It does not allow duplicate values and is mainly used for
mathematical operations like union and intersection.
sets are also mutable.

"""

# Dictionary Example


student_info = {
    "name" : "Zulkaif_Ahmad" ,
    "Subjects" : {
        "comp" : 100 ,
        "Math" : 98 ,
        "Phy" : 88.5 
    } ,
    "is_graduated" : False ,
    "courses" : ["python" , "javascript" , "c++"],
    "Skills" : ("html" , "css" , "js" , "react" , "next" , "github")
}

# student_info["courses"][0] = "C" # this is how to change something in dictonary
# print("count of skills : ",len(student_info["Skills"]))

# print("Student info : " , student_info);
# print("Student Courses : " , student_info["courses"]);
# print("\nStudent subjects : " , student_info["Subjects"])
# print("\nStudent Skills : ", student_info["Skills"])



# Methods of Dictonary : 

print(list(student_info.keys()),"\n"); # type casting 
print(student_info.values(),"\n"); # give all the values 
print(student_info.items(),"\n"); # give all ,  key : values  , in the form of tuples
print(student_info.get("is_graduated"),"\n"); 
# getting specific value and if not exists then it won't give you error instead print NONE


new_dic = {"city" : "Peshawar"}
student_info.update(new_dic)
print("updated dictionary : " ,student_info )



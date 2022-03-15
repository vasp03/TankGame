avskärare = "----------------------------------------------------------------------------"



# print(avskärare)
# print("While:")
# i = 1
# #Medans i är mindre eller lika med 6, printar den i och adderar 1 på i
# while i <= 6:
#     print(i)
#     i += 1



# print(avskärare)
# print("function:")
# #Nedan är en funktion
# def f(x):
#     return 2*x+1
# #printar ut vad funktionen jag kallar på: f()
# print(f(1))



# print(avskärare)
# print("break:")
# i = 1
# #Medans i är mindre eller lika med 6, printar den i och adderar 1 på i
# while i <= 6:
#     print(i)
#     if(i==4):
#         print("break")
#         break
#     i += 1



# print(avskärare)
# print("Import function:")
# from test_module import person1, pog
# print(person1["age"], "is very", pog())



# print(avskärare)
# print("Arrays:")
# list1 = ["banan","äpple","pog"]
# print(list1[1])



# print(avskärare)
# print("Import a module")
# import test_module as testModule
# print(testModule.pog())



print(avskärare)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def aFunc(*c):
        print("Person -", p1.name,p1.age,c)

p1=Person(input("Name: "), input("Age: "))
Person.aFunc("Get rekt")


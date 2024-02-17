#-----------------INSTANCE ATTRIBUTES-------------
# class Athlete:

#     #Constructor / Initializer
#     def __init__(self, jno, name, position):
#         self.jno = jno              #Jersey Number
#         self.name = name            #Player Name
#         self.position = position    #Playing Position


#-----------------CLASS ATTRIBUTES-------------
# class Athlete:
    
#     event = 'Men\'s Volleyball'     #Class Attribute

#     #Constructor / Initializer
#     def __init__(self, jno, name, position):
#         self.jno = jno              #Jersey Number
#         self.name = name            #Player Name
#         self.position = position    #Playing Position


#-----------------INSTANTIATING OBJECTS-------------
# class Athlete:
#     event = 'Men\'s Volleyball'     #Class Attribute

#   #Constructor / Initializer
#     def __init__(self, jno, name, position):
#         self.jno = jno              #Jersey Number
#         self.name = name            #Player Name
#         self.position = position    #Playing Position

# #Instantiation
# ash = Athlete(4, 'Ashly Duke', 'S')
# jose = Athlete(9, 'Jose Malvin', 'MB1')

# #Accessing Instance Attributes
# print(f'''{ash.name} is an {ash.position}.
# His jersey number is {ash.jno}.''')
# print(f'''{jose.name} is an {jose.position}.
# He is the team captain with jersey number {jose.jno}.''')

# #Accessing Class Attribute
# if ash.event == 'Men\'s Volleyball':
#     print(f'{ash.name} is a {ash.event} Player.')




#-----------------INSTANCE METHODS-------------
# def functionName(self, parameter_list: type) -> returnType:
#     pass



# class Athlete:

#     event = 'Men\'s Volleyball'     #Class Attribute
#     #Constructor / Initializer
#     def __init__(self, jno: int, name: str, position: str) -> None:
#         self.jno = jno              #Jersey Number
#         self.name = name            #Player Name
#         self.position = position    #Playing Position

#     def description(self) -> str:
#         return f'Jersey no. {self.jno}, {self.name}!'

#     def serve(self, sType: str) -> str:
#         return f'{self.name} uses {sType} serve!'
    
#     # Class implementation
# ash = Athlete(4, 'Ashly Duke', 'S')

# print(ash.description())
# print(ash.serve('float'))


#-----------------PYTHON OBJECT INHERITANCE-------------
# class Athlete:

#     event = 'Men\'s Volleyball'     #Class Attribute

#     #Constructor / Initializer
#     def __init__(self, jno: int, name: str, position: str) -> None:
#         self.jno = jno              #Jersey Number
#         self.name = name            #Player Name
#         self.position = position    #Playing Position

#     def description(self) -> str:
#         return f'Jersey no. {self.jno}, {self.name}!'

#     def serve(self, sType: str) -> str:
#         return f'{self.name} uses {sType} serve!'
  
# class MiddleBlocker1(Athlete):
#     def __init__(self, jno: int, name: str) -> None:
#         self.jno = jno
#         self.name = name
#         self.position = 'MB1'
    
#     def block(self) -> str:
#         return f'{self.name} blocks the hit!'
    
# class Setter(Athlete):
#     def __init__(self, jno: int, name: str) -> None:
#         super().__init__(jno,name,'Setter')
    
#     def serve(self) -> str:
#         return f'{self.name} jump serves!'
    

# # Class implementation
# ash = Setter(4, 'Ashly Duke')
# jose = MiddleBlocker1(9,'Jose Malvin')

# print(ash.description()) # Inherited from the parent class
# print(jose.description()) # Inherited from the parent class
# print(jose.block()) # Owned by the child class MiddleBlocker1
# #print(jose.serve('jump’)) # Inherited from the parent class
# print(ash.serve()) # Overridden from the parent class




#-----------------KEEPING THINGS PRIVATE-------------
# class Athlete:

#    event = 'Men\'s Volleyball'

#    #Constructor / Initializer
#    def __init__(self, jno: int, name: str, position: str) -> None:
#        self.jno = jno
#        self.__name = name # __name is private
#        self.position = position

#    def description(self) -> str:
#        return f'Jersey no. {self.jno}, {self.__name}!'

#    def serve(self, sType: str) -> str:
#        return f'{self.__name} uses {sType} serve!'

#    # Accessor for the private attribute __name
#    def getName(self) -> str:
#        return self.__name

#    # Mutator for the private attribute __name
#    def setName(self,name: str) -> None:
#        self.__name = name

# class OutsideHitter1(Athlete):

#     def description(self) -> str:
#         s = f'Hi! I am {self.getName()}! '
#         s+= f'I am an {self.position}.'
#         return s

# # Class implementation
# chris = OutsideHitter1(7, 'Chris', 'OH1')
# chris.setName('Chris Jimenez')
# print(chris.description())

# # ash = Athlete(4,'Ashly Duke','Setter')

# # print(ash.description())


# x = 5

# print("{} is {}.".format("weh", "dinga"))

# x= "power"
# y= "puff"

# print(f"{x} and {y}!")

# print("My", "name", "is", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*\n")

# a = 20
# b = 3
# res = a + b / b + b * 4
# print(res)

# a = 20
# b = 3
# res = a + b / b + b * 5
# res//=5
# print(res)

# x = 100
# y = 50
# print(x and y)

# x = 6
# y = 2
# print(x ** y)
# print(x // y)

# list1 = [10, 20, 30, 40, 50]
# y = len(list1) -1
# while y >= 0:
#     print






    






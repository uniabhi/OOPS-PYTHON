from OOPS_Proj import chatbook

lst = [1,2,3]
my_str = "mlps playlist"
my_int = 123

# print(type(lst))
# print(type(my_str))
# print(type(my_int))

# print(lst.index(1))

from OOPS_Proj import chatbook
user1 = chatbook()
print(user1.id)


lst1 = [1,2,3]

# print(len(lst1))

# user1.signup()
# print(user1._chatbook__name)

# print(user1.get_name())
# user1.set_name("Harish")
# print(user1.get_name())


# Using static method directly from class rather than object

# Using static method directly from class rather than obj
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

user4 = chatbook()
print(user4.id)
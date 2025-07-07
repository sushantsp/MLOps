from OOPs_Project import Blogger

## Accessing the encapsuled variable or attribute
# user1 = Blogger()
# print(user1._Blogger__name)


## Getter and Setters
# print(user1.get_name())

# user1.set_name("Sushant")
# print(user1.get_name())

# Using static method directly from class rather than obj
Blogger.set_id(10)


user1 = Blogger()
print(user1.id)

user2 = Blogger()
print(user2.id)

user3 = Blogger()
print(user3.id)

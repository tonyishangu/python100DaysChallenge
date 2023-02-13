# CREATING A CLASS
# SYNTAX OF A CLASS
#   class Car:
#   name using pascal case

class User:

    def __init__ (self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User('001', 'tony')
print(user_1.id)
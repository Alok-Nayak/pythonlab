class User():
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        print("New user being created...")
        pass

user_1 = User("001", "alok")
print(user_1.id, user_1.name, user_1.follower)
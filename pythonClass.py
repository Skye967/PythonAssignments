# declare a class and give it name User
class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login
    def login(self):
        self.logged = True
        print( self.name + " is logged in.")
        return self
    
    def logout(self):
        self.logged = False
        print( self.name + " is not logged in")
        return self
    # print name and email of the calling instance
    def show(self):
        print( "My name is {}. You can email me at {}".format(self.name, self.email))
        return self
#now create an instance of the class
new_user = User("Anna","anna@anna.com")
print( new_user.email)
new_user.login()
new_user.show()
new_user.logout()

class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    

    def menu(self):
        user_input = input("""Welcome to the chatbook !! Can you tell me how would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to message a Friend
                           5. Press any other key to exit !!""")
        
        if user_input == "1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


    def signup(Self):
        email = input("Enter your email Here: ")
        pwd = input("Enter your password Here: ")
        Self.username = email
        Self.password = pwd
        print("You have successfully signedup")
        print("\n")
        Self.menu()

    
    def signin(self):
        if self.username =='' and self.password == '':
            print("Please signup first by pressing option 1 from the menu !!")
        else:
            uname = input("Enter your email/username Here: ")
            pwd = input("Enter your password Here: ")
            if self.username==uname and self.password==pwd:
                print("You have signedin successfully !!")
                self.loggedin= True
            else:
                print("Please enter correct credentials !!")
        
        print("\n")
        self.menu()

obj1 = chatbook()


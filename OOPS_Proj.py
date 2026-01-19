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
                           5. Press any other key to exit 
                           -> """)
        
        if user_input == "1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_mssg()
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

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your post content here -> ")
            print(f"Desired content -> {txt} for Blog has been posted")
        else:
            print("Please signedin first to Blog post...")
        print("\n")
        self.menu()

    def send_mssg(self):
        if self.loggedin== True:
            txt = input("Enter your message content here -> ")
            frnd = input("Whom to send this message? -> ")
            print(f"Your message has been sent to your friend -> {frnd}")
        else:
            print("You need to sign in first to type and send something..")
        print("\n")
        self.menu()


# user1 = chatbook()


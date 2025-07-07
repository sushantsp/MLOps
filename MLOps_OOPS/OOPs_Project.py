class Blogger:

    # class attribute and available to all the object. in this case not because of encaps. __
    __user_id = 1

    def __init__(self):
        self.id = Blogger.__user_id
        Blogger.__user_id +=1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()


    @staticmethod
    def set_id(val):
        Blogger.__user_id = val

    @staticmethod
    def get_id():
        return Blogger.__user_id

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
        
    def menu(self):

        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


    def signup(self):

        email = input("enter your email here -> ")
        pwd = input("setup your password here -> ")      
        self.username = email
        self.password = pwd

        print("You have signed up successfully !!\n")

        self.menu()


    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first by pressing 1 in the menu.")

        else:
            uname = input("Please enter your username : ")
            pwd = input("Please enter your password : ")
            if self.username==uname and self.password==pwd:
                print("YOu have successfullt logged in !!\n")

                self.loggedin = True
            else:
                print("Please input correct credentials..\n")
        self.menu()

        
    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

# user = Blogger()
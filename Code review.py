class User:
    def __init__(self, username, displayName, state, friends):
        self.username = username
        self.displayName = displayName
        self.state = state
        self.friends = friends

    def __str__(self):
        f = ""
        for i in range(0, len(self.friends)):
            f += "Friend" + str(i+1) + ": " + self.friends[i] + ", "
        return f"UserName: {self.username}, DisplayName: {self.displayName}, State: {self.state}, " + f

u1 = User("goldenlover1", "Jane Doe", "CA", ["petpal4ever", "whiskerwatcher"])
u2 = User("whiskerwatcher", "John Doe", "NY", ["goldenlover1"])
u3 = User("petpal4ever", "Great Name", "WV", ["goldenlover1"])

# print(u1)
# print(u2)
# print(u3)

##########################################################################################################
class Posts:
    def __init__(self,postId,userName,viewType):
        self.postId = postId
        self.userName = userName
        self.viewType = viewType

    def __str__(self):
        return f"postId: {self.postId}, userName: {self.userName}, viewType: {self.viewType}"

p1 = Posts("post1112","goldenlover1","friend")
p2 = Posts("post2123 ","whiskerwatcher","friend ")
p3 = Posts("post3298 ","petpal4ever "," public")

#3print(p1.postId)
# print(p2)
# print(p3)


print('Options')
print('1. Load input data.')
print('2. Check visibility.')
print('3. Retrieve posts.')
print('4. Search users by location:')
print('5. Exit:')

option = input('Select an option: ')

if option == '1':
    print('Loading Data ...')

elif option == '2':
    postId = input('Enter post Id number: ')
    postsUserId = input('Enter a user id: ')
    print('Checking Posts Visibility ...')
    
    if postId == 'post1112' or postId =='post2123':
        if postsUserId == 'goldenlover1' or postsUserId == 'whiskerwatcher':
            print('Access Permitted')
    else:
        print('Access Denied')

elif option == '3':
    userName = input('Enter Username to get posts: ')
    if userName == "goldenlover1":
        print('Acess denied post Private')
    elif userName == 'whisker watcher':
        print('Acess denied post Private')
    elif userName == 'petpal4ever':
        print(p3.postId)

elif option == '4':
    state = input('Enter 2 letters to find user from certain state: ')
    print('Searching For location ...')
    if state == 'ca' or state == 'CA':
        print(u1.displayName)
    elif state == 'ny' or state == 'NY':
        print(u2.displayName)
    elif state == 'wv' or state == 'WV':
        print(u3.displayName)

elif option == '5':
    print('Exiting the system...')

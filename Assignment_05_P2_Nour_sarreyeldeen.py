class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
        self.graph = {}

    def add_user(self, username):
        if username in self.users:
            print("User already exists. Please choose another username.")
        else:
            self.users[username] = True
            self.graph[username] = []

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            del self.graph[username]
            for user, friends in self.graph.items():
                if username in friends:
                    friends.remove(username)
            print(f"User {username} removed.")
        else:
            print("User not found.")

    def send_friend_request(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            if user2 not in self.graph[user1]:
                self.graph[user1].append(user2)
                self.graph[user2].append(user1)
                print(f"Friend request sent from {user1} to {user2}.")
            else:
                print(f"{user1} is already friends with {user2}.")
        else:
            print("One or both users not found.")

    def remove_friend(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            if user2 in self.graph[user1]:
                self.graph[user1].remove(user2)
                self.graph[user2].remove(user1)
                print(f"{user1} and {user2} are no longer friends.")
            else:
                print(f"{user1} and {user2} are not friends.")
        else:
            print("One or both users not found.")

    def view_friends(self, username):
        if username in self.users:
            friends = self.graph[username]
            print(f" Your Friends : {', '.join(friends)}")
        else:
            print("User not found.")

    def view_users(self):
        print("Users on the platform:")
        for user in self.users:
            print(user)

def main():
    social_media = SocialMediaPlatform()

    while True:
        print("-" * 40)
        print("1. Add a user to the platform")
        print("2. Remove a user from the platform")
        print("3. Send a friend request to another user")
        print("4. Remove a friend from your list")
        print("5. View your list of friends")
        print("6. View the list of users on the platform")
        print("7. Exit")
        print("-" * 40)

        choice = int(input("Enter a choice: "))

        if choice == 1:
            username = input("Enter username: ")
            social_media.add_user(username)

        elif choice == 2:
            username = input("Enter username to remove: ")
            social_media.remove_user(username)

        elif choice == 3:
            user1 = input("Enter your username: ")
            user2 = input("Enter friend's username: ")
            social_media.send_friend_request(user1, user2)

        elif choice == 4:
            user1 = input("Enter your username: ")
            user2 = input("Enter friend's username: ")
            social_media.remove_friend(user1, user2)

        elif choice == 5:
            username = input("Enter your username: ")
            social_media.view_friends(username)

        elif choice == 6:
            social_media.view_users()

        elif choice == 7:
            break

if __name__ == "__main__":
    main()

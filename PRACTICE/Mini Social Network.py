import json

class NotfoundError(Exception):
    pass

class MiniSocialNetwork:
    users = []
    with open("general.txt", "w") as general:
        pass

class user:
    def __init__(self, name):
        self.name = name
        if self.name not in MiniSocialNetwork.users:
            MiniSocialNetwork.users.append(self.name)
        self.follower_list = []
        self.follower_count = 0
        self.user_feed = []
        self.user_profile = {
            "Name": self.name,
            "Follower count": self.follower_count,
            "Follower list": self.follower_list,
            "Feed": self.user_feed
        }

    def show_user_profile(self):
        self.update_profile()
        with open(f"{self.name} profile.json", "w") as file:
            json.dump(self.user_profile, file, indent=4)
        with open(f"{self.name} profile.json", "r") as file:
            print(file.read())

    def follow(self, follower_name: str):
        try:
            if follower_name not in MiniSocialNetwork.users:
                raise NotfoundError(f"{follower_name} not in network")
            if follower_name not in self.follower_list:
                self.follower_list.append(follower_name)
                self.follower_count += 1
                print(f"You are now following {follower_name}")
            else:
                print(f"You already follow {follower_name}")
        except (NotfoundError, TypeError) as e:
            print("User not found:", e)

    def display_user_feed(self):
        self.user_feed = []
        with open("general.txt", "r") as general:
            for person in general:
                line = json.loads(person)
                if list(line.keys())[0] in self.follower_list:
                    self.user_feed.append(line)
        feed = self.user_feed if len(self.user_feed) < 10 else self.user_feed[-10:]
        with open(f"{self.name} profile.json", "r") as file:
            data = json.load(file)
        data["Feed"] = feed
        with open(f"{self.name} profile.json", "w") as file:
            json.dump(data, file, indent=4)
        print(feed)

    def display_user_profile(self):
        print(self.user_profile)

    def post(self, message):
        user_message = {self.name: message}
        with open("general.txt", "a") as general:
            json.dump(user_message, general)
            general.write("\n")
        print(f"You have posted: {user_message}")

    def update_profile(self):
        self.user_profile["Follower count"] = self.follower_count
        self.user_profile["Follower list"] = self.follower_list
        self.user_profile["Feed"] = self.user_feed



# Assuming your classes are defined and imported above

# Create some users in the network
alice = user("Alice")
bob = user("Bob")
charlie = user("Charlie")

# Alice follows Bob and Charlie
alice.follow("Bob")
alice.follow("Charlie")

# Bob posts a message
bob.post("Hello, this is Bob!")

# Charlie posts a message
charlie.post("Hey! Charlie here.")


# Alice views her profile
alice.show_user_profile()

alice.display_user_feed()
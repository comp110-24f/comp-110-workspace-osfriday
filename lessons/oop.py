"""Learning Object-Oriented Programming."""

# OOP (Object-Oriented Programming)
# objects in the real world are things perceived, used, or interacted with
#   can be physical: chair is a type of furniture, human = mammal fork = utensil
#   can be abstract: happiness = emotion,learning = experience
#   every object has a type, internal data representation, set of procedures
#   for interaction with the object

# Class
# Modeling an Instagram profile with a class


# declaring a new data type! Doesn't already exists (class = classification)
class Profile:  # capital first letter (important)
    username: str  # declaring things that make up the class; called attibutes
    bio: str
    followers: int
    private: bool

    # initializing attributes(with default values)
    def __init__(self):  # this looks like a fn but is a METHOD
        self.username = "usr9"
        self.bio = ""
        self.followers = 0  # default values
        self.following = 0
        self.private = False


my_prof: Profile = Profile()  # construct a NEW profile/object

# My private functions for validating

from datetime import datetime
from PIL import Image

def _password_good(password):

    if len(password) < 8:
        return False
    
    lowercase = False
    uppercase = False
    number = False
    special_char = False
    
    for char in password:

        if char.islower():
            lowercase = True

        if char.isupper():
            uppercase = True

        if char.isnumeric():
            number = True

        if char in ["!", "@", "#", "$", "%", "^", "&", "*", "~", 
                    "`", "(", ")", "-", "_", "+", "=", "|", "{", "}",
                      "[", "]", ",", ":", ";", "<", ">", ".", "?", "/", "\\", "\'", "\""]:
            special_char = True

    if lowercase and uppercase and number and special_char:
        return True
        
    return False


def _confirm_password(password, confirm):
    if password != confirm:
        return False
    else:
        return True
    

def _valid_pic(pic):

    try:
        Image.open(pic)
    except Exception as e:
        return False
    
    return True

# Not a validating function but it is a private helper function.
def _bird_color(name):

    name = name.title()

    red_birds = ["Red-Tailed Hawk", "Cardinal", "Rose-Breasted Grosbeak", "Red-Bellied Woodpecker"]
    orange_birds = ["American Robin", "Red-Shouldered Hawk", "Carolina Wren"]
    blue_birds = ["Eastern Bluebird", "Blue Jay", "Great-Blue Heron"]
    yellow_birds = ["American Goldfinch", "Ruby-Crowned Kinglet"]
    brown_birds = ["Cooper's Hawk", "House Sparrow", "Barred Owl", "Eastern-Screech Owl", "Barn Owl",
                   "Great-Horned Owl", "Mourning Dove", "Brown Pelican", "Canada Goose",
                   "Savannah Sparrow"]
    
    if name in red_birds:
        return "#9e160d"
    elif name in orange_birds:
        return "#f76319"
    elif name in blue_birds:
        return "#1d62e0"
    elif name in yellow_birds:
        return "#e3c902"
    elif name in brown_birds:
        return "#4a3714"
    else:
        return "#050300" #black

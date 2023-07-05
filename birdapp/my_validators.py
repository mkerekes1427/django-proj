# My private functions for validating



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
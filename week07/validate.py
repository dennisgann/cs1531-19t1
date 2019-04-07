# User-defined exceptions
# Raised when the user-name field is invalid
class UserInputError(Exception):
    pass

#business logic
def validate_user_name(username):
	if len(username) < 1 or len(username) > 25 or username.find(' ') != -1:
		raise UserInputError("invalid username")
    # validation successful, do something with the user-name, e.g., add to database
	return True

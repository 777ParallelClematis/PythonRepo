class User:
    """
    Base Class for creating users
    """

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
    def show_id(self) -> None:
        """Prints the user_id"""
        print(self.user_id)

def main() -> None:
    # user: User = User(1) # this shows the docstring lines above
    bob: User = User(0)
    anna: User = User(1)

    database: set[User] = {bob, anna}

    if user_exists(bob, database):
        print('User exists in databsae')
    else:
        print('User does not exist in database')

    print(User.__doc__) # returns documentation on this
    print(user_exists.__doc__) #returns documentation on this



def user_exists(user: User, database: set[User]) -> bool:
    #called 'sphinx' markup, triple-quote then enter
    """
    Checks if a user is inside a database
    :param user: The user to check for
    :param database: the database to check inside
    :return: boolean
    """
    return user in database

if __name__ == '__main__':
    main()


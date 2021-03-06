class Client():
    def __init__(self, user_id, username, balance, message):
        self.__username = username
        self.__balance = balance
        self.__user_id = user_id
        self.__message = message

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__user_id

    def get_message(self):
        return self.__message

    def set_message(self, new_message):
        self.__message = new_message

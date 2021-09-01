   def check_birthday(user_birthday):
        try:
            if datetime.strptime(user_birthday, '%d.%m.%Y'):
                return user_birthday
        except ValueError:
            raise ValueError

    def check_email(user_email):
        try:
            if user_email == (re.search(r'[a-zA-Z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}', user_email)).group():
                return user_email
            raise AttributeError
        except AttributeError:
            raise AttributeError

    def check_name(user_name):

        with open('data/data-file.txt', 'r') as file:
            users = file.readlines()
        try:
            if not any(re.split('\| ', user)[0].strip().casefold() == user_name.casefold() for user in users):
                return user_name
            raise ValueError
        except AttributeError:
            raise AttributeError

    def check_phone_number(user_phone_number):
        try:
            if user_phone_number == (re.search(r'\+?\d?\d?\d?\d{2}\d{7}', user_phone_number)).group():
                return user_phone_number
            raise AttributeError
        except AttributeError:
            raise AttributeError
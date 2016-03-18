from abc import ABCMeta, abstractmethod


class BaseField(metaclass=ABCMeta):

    def is_valid(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class TextInput(BaseField):

    def is_valid(self):
        return True

    def __str__(self):
        return "<input />"


class PasswordInput(BaseField):

    def is_valid(self):
    	return True

    def __str__(self):
        return "<input />"


class Form:
	def __init__(self):
		objects = Form.__subclasses__()
		fields = []
		for i in range(0, len(objects)):
			for attr in objects[i].__dict__:
				if not callable(attr) and '__' not in attr:
					fields.append(attr)
		print(fields)

class LoginForm(Form):
	name = TextInput()
	pwd = PasswordInput()




def main():
	f = LoginForm()
	

if __name__ == '__main__':
	main()
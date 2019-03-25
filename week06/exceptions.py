'''
What is the difference between an exception and a software bug?

EXCEPTION:
- error that happens during execution of a program
- causes program to terminate abruptly
- due to unavoidable circumstances such as;
    - providing wrong input
    - file to be read not found
- can be anticipated by programmers --> handling mechanisms (gracefully)

FAULT/BUG:
- erroneous software element of a system / un-intended behaviour
- can cause system failure
- arises due to programming error :(
- incorrect results or peforming poorly
- prevented through thorough testing

'''

# Mechanism to handle exceptions
# In python; Object instance of Exception class handled by try/except mechanism

# If not handled, normal flow is disrupted and error msg shown in the form of stack-trace
# def divide(a,b):
# 	return a/b

# Python’s try/except exception-handling mechanism
def divide(a,b):
	try:
		return a/b
    # catch ZeroDivisionError exception as error
	except ZeroDivisionError as error:
		print("error: {0}". format(error))
	else:
		print("division successful")


print(divide(3,0))


# User-defined exceptions to signal application error
class Car:
    def __init__(self, name, model, rego):
        self._name = name
        self._model = model
        self._rego = rego

    def __str__(self):
        return f"Car <{self._name}, {self._model}, {self._rego}>"

# User defined exception
class IllegalSpeed(Exception):
    def __init__(self, car, speed, msg=None):
        if msg is None:
	        msg = "An error occurred with car %s" % car
        super().__init__()
        self._msg = msg
        self._speed = speed
        self._car = car
    
    def __str__(self):
        return self._msg
    
    @property
    def speed(self):
        return self._speed

def drive_car(car, speed):
    try:
        if speed > 100:
            # throw/raise the exception
            raise IllegalSpeed(car, speed, "%s caught for driving at speed %d" % (car, speed))
    # catch it as error
    except IllegalSpeed as error:
        print(error)
        if error.speed >= 120:
           call_000()

def call_000():
    print("calling 000")

my_car = Car("mercedes","glc coupe","xyz133")
drive_car(my_car,180)

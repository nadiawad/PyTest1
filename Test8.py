class Parent:
    def __init__(self, last_name, eye_colour):
        print "Parent Init Called"
        self.last_name = last_name
        self.eye_colour = eye_colour

    def show_info(self):
        print "Last Name: "+self.last_name
        print "Eye Colour: "+self.eye_colour

class Child(Parent):
    def __init__(self, last_name, eye_colour, number_of_toys):
        print "Child Init Called"
        Parent.__init__(self, last_name,eye_colour)
        self.number_of_toys = number_of_toys

    def show_info(self):
        Parent.show_info(self)
        print "Number of toys: "+ str(self.number_of_toys)

x = Parent("Awad", "brown")
#print x.last_name
x.show_info()

y = Child("Awad", "hazel", 4)
#print y.number_of_toys
#print y.last_name
y.show_info()
from turtle import Turtle

class LievreTortue:
    def __init__(self, lievre_instance):
        self.tortue = Turtle()
        self.lievre = lievre_instance
    def forward(self, distance):
        self.tortue.forward(distance)
        self.lievre.aller_vers(self.tortue.xcor(), self.tortue.ycor())
    def left(self, angle):
        self.tortue.left(angle)
        self.lievre.aller_vers(self.tortue.xcor(), self.tortue.ycor())
    def right(self, angle):
        self.tortue.right(angle)
        self.lievre.aller_vers(self.tortue.xcor(), self.tortue.ycor())

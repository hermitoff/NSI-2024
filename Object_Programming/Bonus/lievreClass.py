import turtle
import math

class Lievre:
    def __init__(self):
        self.turtle = turtle.Turtle()
    
    def aller_vers(self, cible_x, cible_y):
        position_x, position_y = self.turtle.position()
        angle = math.degrees(math.atan2(cible_y - position_y, cible_x - position_x))
        distance = math.sqrt((cible_x - position_x) ** 2 + (cible_y - position_y) ** 2)
        
        # Limiter l'angle à 20 degrés maximum
        angle_limit = 20
        angle_difference = angle - self.turtle.heading()
        if angle_difference > angle_limit:
            self.turtle.left(angle_limit)
        elif angle_difference < -angle_limit:
            self.turtle.right(angle_limit)
        else:
            self.turtle.setheading(angle)
        
        # Limiter la distance à 20 pas maximum
        step_limit = 20
        steps = min(distance, step_limit)
        self.turtle.forward(steps)
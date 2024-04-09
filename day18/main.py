import random
import turtle as t

tim = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# # Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# CHALLENGE: draw from triangle to decangle.
# figure_drawing = 1
# num_sides = 3
# index_color_list = 0
# color_list = ["aquamarine4", "azure4", "BlueViolet", "brown4", "CadetBlue", "chartreuse4", "chocolate4", "goldenrod4",
#               "HotPink", "LightSeaGreen", "LawnGreen"]


#
# while figure_drawing < 11:
#     angle_sides = 360 / num_sides
#     # Draw a Triangle
#     tim.pencolor(color_list[index_color_list])
#
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle_sides)
#
#     figure_drawing += 1
#     num_sides += 1
#     index_color_list += 1
#


# # Other solution
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(color_list))
#     draw_shape(shape_side_n)


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# # CHALLENGE: Random walk with random color
# directions = [0, 90, 180, 270]
tim.pensize(3)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# Window stay
screen = t.Screen()
screen.exitonclick()

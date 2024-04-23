from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The head of the snake.

    def create_snake(self):
        """Create the snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a segment to the snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake with a new segment"""
        self.add_segment(self.segments[-1].position())  # adding from the last segment

    def move(self):
        """Move the snake forwards"""
        # (start, stop, step) -> backwards of the segments
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # move second to last segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Move the snake up"""
        if self.head.heading() != DOWN:
            # 270 to prevent the snake to move to the opposite direction.
            self.head.setheading(UP)

    def down(self):
        """Move the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

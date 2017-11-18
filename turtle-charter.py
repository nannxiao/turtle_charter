import turtle

def count_observations(fname):
    '''this function count the number of observations in a file
    it takes one parameter: file name, then returns the observations number
    '''
    myfile = open(fname)
    count_l = int(sum(1 for line in myfile) / 3)
    return count_l

def get_max_value(fname, feature):
    '''this function takes 2 parameters: file name and feature name
    it turns the file content to a string list, and uses a for loop to get the maximum value of one feature
    then returns the maximum value
    '''
    myfile = open(fname)
    lst = myfile.readlines()
    for i,s in enumerate(lst):
        lst[i] = s.strip()
    max_array = -10
    count = int(len(lst)/3)
    feature_l = int(feature.split(' ')[1])
    for i in range(0, count):
        max_array = max(int(lst[i*3+feature_l]), max_array)
    return max_array

def draw_x_axis(turtle):
    '''this function takes a turtle as parameter
    then let the turtle draw the x-axis which has a length of 700 pixels
    '''
    turtle.forward(700)
    turtle.left(180)
    turtle.forward(700)
    turtle.right(180)

def draw_y_axis(turtle):
    '''this function takes another turtle as parameter
    then let the turtle draw the y-axis which has a length of 400 pixels
    '''
    turtle.left(90)
    turtle.forward(400)

def draw_y_tick_mark(turtle, fname):
    '''this function takes a turtle and a file name as parameters
    then lets the turtle draw the y-axis tick marks using the calculated height
    '''
    # beacause when we draw the bar chart of 2 features we want to keep the tick marks in one same scale,
    # we can take the max value of feature 1 as the maximum value in tick marks
    val = get_max_value(fname, 'feature 1')
    height = 400 / val
    dist = val / 10
    turtle.left(90)
    for i in range(0, 10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(25)
        turtle.pendown()
        turtle.write(round(val-i*dist, 1), align = 'left', font = font)
        turtle.penup()
        turtle.left(180)
        turtle.forward(35)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(height * dist)
        turtle.right(90)

def draw_rectangle(turtle, width, height, color):
    '''this function takes 4 arguments: turtle, width, height and color
    it draws a single rectangle of the assigned width, height and color
    '''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

def draw_bars(turtle, fname, color):
    '''this function takes 3 arguments: turtle, file name and color,
    it draws the bar chart of 2 features, and takes the scale of first feature,
    in the for loop, it calls draw_rectangle function twice at each time,
    in order to draw bars of both features.
    '''
    myfile = open(fname)
    lst = myfile.readlines()
    for i,s in enumerate(lst):
        lst[i] = s.strip()
    count = int(len(lst)/3)
    width = 700 / count - 10
    # takes the scale of the first feature by using the max value of first feature
    max_l = get_max_value(fname, 'feature 1')
    for i in range(0, count):
        turtle.forward(10)
        height_1 = int(lst[i*3+1])*(400/max_l)
        height_2 = int(lst[i*3+2])*(400/max_l)
        draw_rectangle(turtle, width/2, height_1, choose_color(i, color))
        draw_rectangle(turtle, width/2, height_2, choose_color(i+6, color))
        draw_x_axis_label(turtle, width, lst, i)

def draw_x_axis_label(turtle, width, lst, i):
    '''this function takes 4 arguments: turtle, width of a bar, value list, and 'i' in the for loop
    it writes the x axis label under each bar
    '''
    turtle.penup()
    turtle.right(180)
    turtle.forward(width/2)
    turtle.left(90)
    turtle.forward(25)
    turtle.pendown()
    turtle.write(lst[i*3], align = 'center', font = font)
    turtle.penup()
    turtle.right(180)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(width/2)
    turtle.pendown()

def choose_color(index, color):
    '''this function takes 2 arguments: index and color
    index decides which specific color to use for a bar, and color tells which theme user wants to use
    '''
    color_1 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f']
    color_2 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928']
    if color == 'light':
        return color_1[index%12]
    else: 
        return color_2[index%12]

# Main function:
if __name__ == '__main__':
    fname = input('Enter the file path to visualize: (data/huskies2016.txt)')
    feature = input('Enter the feature you want to analyze:(feature 1/feature 2)')
    color = input('Enter the color palette you want:(light/dark)')

# Retrieve the number of observations and the maximum value of the wanted feature
    count_l = count_observations(fname)
    max_l = get_max_value(fname, feature)
    print('There are', count_l, 'observations in this file.')
    print('The maximum value of', feature, 'is', max_l, '.')

# Create a new screen 800 by 500 pixels
    turtle.setup(800, 500)
    wn = turtle.Screen()

# Set graph title by splitting the file name
    title = fname.split('/')[1].split('.')[0]
    wn.title(title)

# Move the origin of the coordinate system to the left bottom corner of the chart
    wn.reset()
    turtle.setworldcoordinates(-50, -50, 750, 450)

# Create two turtles, and make them move faster
    tur_x = turtle.Turtle()
    tur_y = turtle.Turtle()
    tur_x.speed(0)
    tur_y.speed(0)

# Set the font template for later use
    font = ('Arial', 14, 'normal')

# Draw the bar chart
    draw_x_axis(tur_x)
    draw_y_axis(tur_y)
    draw_y_tick_mark(tur_y, fname)
    draw_bars(tur_x, fname, color)

# Control the window's open time
    turtle.mainloop()

# +
import matplotlib.pyplot as plt #import libraries
import numpy as np

def deriv(f, base): 
    # estimate the derivative of the function f at base_point using the symmetric approx
    return ((f(base+10**(-5)) - f(base))) / (10**(-5))

def gradient_descent(f, learning_rate, initial_point):
    x_coords = []  # This list is where you will store the x_n's
    y_coords = []  # This list is where you will store the y_n's
    x_coords.append(initial_point)  # set the first x coordinate to be initial_point
    y_coords.append(f(initial_point))  # set the first y coordinate to be f(initial_point)
    i = 1
    while abs(deriv(f, x_coords[i-1])) > 0.001:
        x1 = x_coords[i-1] - learning_rate * deriv(f, x_coords[i-1])  # x1 is initial_point - learning_value * f'(x) at this point
        y1 = f(x1)
        x_coords.append(x1)  # add x1 to x as the last value
        y_coords.append(y1)  # add y1 to y as the last value
        i += 1
        if i == 10000:
            break

    plot_range = np.linspace(min(x_coords) - 0.5, max(x_coords) + 0.5, 1000)  # a nice plot range to make it look good
    function_range = [f(i) for i in plot_range]
    plt.plot(plot_range, function_range)  # this plots the function f(x)
    plt.plot(x_coords, y_coords)  # this will plot the sequence of points x_n, f(x_n)
    plt.show()

    return round(x_coords[i-1], 3), round(y_coords[i-1], 3)  # returns your last x_n and y_n, rounded to three decimal places.

# Function 1:
def f(x):
    return x**2

gradient_descent(f, 0.9, 5)


# +
import matplotlib.pyplot as plt #import Libraries
import numpy as np

def deriv(f, base): #estimate the derivative of the function f at base_point using the symmetric approx
    return ((f(base+10**(-10))-f(base-10**(-10)))/(2*10**(-10)))

#difference between very small step to the left and very small step to the right

def gradient_descent(f, learning_rate, initial_point):
    x_coords=[] #This List is where you will store the x_n's
    y_coords=[] #This List is where you will store the y_n's
    x_coords.append(initial_point) #set the first x coordinate to be initial_point
    y_coords.append(f(initial_point)) #set the first y coordinate to be f(initial_point)
    i = 1
    xi = initial_point
    while abs(deriv(f,xi)) > 0.001:
        xi = x_coords[-1]-learning_rate*deriv(f,x_coords[-1]) #xi is initial_point + learning_value * f'(x) at this point
        yi = f(xi)
        x_coords.append(xi) #add xi to x as the last value
        y_coords.append(yi) #add yi to y as the last value
        i = i+1
        if i == 10000:
            break

    plot_range=np.linspace(min(x_coords)-0.5, max(x_coords)+0.5,10000) #a nice plot range to make look good
    function_range=[f(i) for i in plot_range]
    plt.plot(plot_range, function_range) #this plots the function f(x)
    plt.plot(x_coords, y_coords) #This will plot the sequence of points x_n, f(x_n)
    plt.ylim(-1.2,0.2)
    plt.show()

    return round(x_coords[-1],3), round(y_coords[-1],3) #returns your last x_n and y_n, #rounded to three decimal places.

#function 2:
def g(x):
    return x**4 - 2*x**2

print(gradient_descent(g,0.24,1.2))
print()
print(gradient_descent(g,0.24,-1.2))
print()
print(gradient_descent(g,0.24,0))

#if x_0 is chosen as 0 for the initial value, the code will not work because it is a maximum and the derivative at x = 0 is
#already 0 and thus the gradient descent will not move anywhere.


# +
import matplotlib.pyplot as plt #import Libraries
import numpy as np

def deriv(f, base): #estimate the derivative of the function f at base_point using the symmetric approx
    return ((f(base+10**(-10))-f(base-10**(-10)))/(2*10**(-10)))

#difference between very small step to the left and very small step to the right

def gradient_descent(f, learning_rate, initial_point):
    x_coords=[] #This List is where you will store the x_n's
    y_coords=[] #This List is where you will store the y_n's
    x_coords.append(initial_point) #set the first x coordinate to be initial_point
    y_coords.append(f(initial_point)) #set the first y coordinate to be f(initial_point)
    i = 1
    xi = initial_point
    while abs(deriv(f,xi)) > 0.001:
        xi = x_coords[-1]-learning_rate*deriv(f,x_coords[-1]) #xi is initial_point + learning_value * f'(x) at this point
        yi = f(xi)
        x_coords.append(xi) #add xi to x as the last value
        y_coords.append(yi) #add yi to y as the last value
        i = i+1
        if i == 10000:
            break

    plot_range=np.linspace(min(x_coords)-0.5, max(x_coords)+0.5,10000) #a nice plot range to make look good
    function_range=[f(i) for i in plot_range]
    plt.plot(plot_range, function_range) #this plots the function f(x)
    plt.plot(x_coords, y_coords) #This will plot the sequence of points x_n, f(x_n)
    plt.show()

    return round(x_coords[-1],3), round(y_coords[-1],3) #returns your last x_n and y_n, 

#function 2:
def h(x):
    return abs(x)

print(gradient_descent(h,0.2,1))




# +
import matplotlib.pyplot as plt #import libraries
import numpy as np

def deriv(f, base): 
    return (f(base+10**(-10))-f(base-10**(-10)))/(2*10**(-10))



def gradient_descent(f, learning_rate, initial_point):
    x_coords=[] #This list is where you will store the x_n's
    y_coords=[] #This list is where you will store the y_n's
    x_coords.append(initial_point) #set the first x coordinate to be initial_point
    y_coords.append(f(initial_point)) #set the first y coordinate to be f(initial_point)
    xi = initial_point
    i = 1
    while abs(deriv(f,xi)) > 0.001:
        xi = x_coords[i-1]-learning_rate*deriv(f,x_coords[i-1])
      
        yi = f(xi)
        x_coords.append(xi) 
        y_coords.append(yi) 
        i = i+1
        if i == 10000:
            break

    plot_range=np.linspace(min(x_coords)-0.5, max(x_coords)+0.5,10000) #a nice plot range to make look good
    function_range=[f(i) for i in plot_range]
    plt.plot(plot_range, function_range) #this plots the function f(x)
    plt.plot(x_coords, y_coords) #This will plot the sequence of points x_n, f(x_n)
    plt.ylim(0.6, 1.2)

    return round(x_coords[-1],3), round(y_coords[-1],3) #returns your last x_n and y_n, #rounded to three decimal places.


def funny_function(x):
    if x>0:
        return x**x
    elif x==0:
        return 1
    else:
        return abs(x)**abs(x)

print(gradient_descent(funny_function,0.89,1))
print()
print(gradient_descent(funny_function,0.89,-1))
# -



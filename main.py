import numpy as np
from matplotlib.animaton import FuncAnimation
from IPython.display import display
import matplotlib.pyplot as plt

Figure = plt.figure()

lines_plotted = plt.plot([]) #creating a plot

lnie_plotted = lines_plotted[0]

#we put the limits on x axis since. It is a trigonometry function so it only takes (0,2pi)

plt.xlim(0,2*np.pi)
plt.ylim(-1.1,1.1)

#we put the limits on y since it is a cosine function

x = np.linspace(0,2*np.pi,100) # initialising x from 0 to 2pi

y = 0 #initially

def AnimationFunction(frame):

    y = np.cos(x+2*np.pi*frame/100) # we take the y values within a certain range.

    lines_plotted.set_data((x,y)) # line is set with a new values of x and y


#We call the FuncAnimation and we are giving an interval of 25 miliseconcds
anim_created = FuncAnimation(Figure, AnimationFunction, frames = 100, interval = 25)

#We convert it to an HTML file so that the animation can work.
video = anim_created.to_html5_video()
html = display.HTML(video)
display.display(html)
plt.close()


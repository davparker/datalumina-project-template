# 11.1 Plotting Using PyLab

import pylab

# a simple plot pg. 170
pylab.figure(1)  # create figure 1
pylab.plot([1, 2, 3, 4], [1, 7, 3, 5])  # draw on figure 1
pylab.show()  # show figure on screen

# plot multiple figures and write to file pg. 171
pylab.figure()  # create figure 1
pylab.plot([1, 2, 3, 4], [1, 2, 3, 4])  # draw on figure 1
pylab.figure(2)  # create figure 2
pylab.plot([1, 4, 2, 3], [5, 6, 7, 8])  # draw on figure 2
pylab.savefig("Figure-Addie")  # save figure 2
pylab.figure(1)  # go back to working on figure 1
pylab.plot([5, 6, 10, 3])  # draw again on figure 1
pylab.savefig("Figure-Jane")  # save figure 1

# plotting compound growth pg. 172
principal = 10000  # initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
pylab.plot(values)

# adding labels to plots pg. 173
pylab.title("5% Growth, Compounded Annually")
pylab.xlabel("Years of Compounding")
pylab.ylabel("Value of Principal ($)")

# change3 type size and line width pg. 174
principal = 10000  # initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
pylab.plot(values, linewidth=30)
pylab.title("5% Growth, Compounded Annually", fontsize="xx-large")
pylab.xlabel("Years of Compounding", fontsize="x-small")
pylab.ylabel("Value of Principal ($)")

# plotting with common rcParams settings pg. 175
# used in classroom presentations
# set line width
pylab.rcParams["lines.linewidth"] = 4
# set font size for titles
pylab.rcParams["axes.titlesize"] = 20
# set font size for labels on axes
pylab.rcParams["axes.labelsize"] = 20
# set size of numbers on x-axis
pylab.rcParams["xtick.labelsize"] = 16
# set size of numbers on y-axis
pylab.rcParams["ytick.labelsize"] = 16
# set size of ticks on x-axis
pylab.rcParams["xtick.major.size"] = 7
# set size of ticks on y-axis
pylab.rcParams["ytick.major.size"] = 7
# set size of markers, e.g., circles representing points
pylab.rcParams["lines.markersize"] = 10
# set number of times marker is shown when displaying legend
pylab.rcParams["legend.numpoints"] = 1

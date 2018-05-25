'''
Energy Efficiency of Chicago Schools (35pts)

https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking-2016-Data-Reported-in-/fpwt-snya\

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2016 which was reported in 2017.

We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.  
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 5 highest and 5 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)


- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)

'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("files/Chicago_Energy_Benchmarking_-_2016_Data_Reported_in_2017.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

#print(data)
headers = data.pop(0)
print("\n\n\n\n", headers)

school_names = []
school_pow = []
school_foot = []

for i in range(len(data)):
    if data[i][6] == 'K-12 School':
        try:
            school_name = data[i][2]
            school_pw = float(data[i][12])
            school_ft = float(data[i][7])
            school_names.append(school_name)
            school_pow.append(school_pw)
            school_foot.append(school_ft)
        except:
            print(school_name, "has no data")

print(school_names)
plt.figure(1)
plt.scatter(school_pow, school_foot, s=4, c='red')
plt.title("School Square Feet vs Electricity Usage")
plt.xlabel("Electricity Usage(kBtu)")
plt.ylabel("Square Feet(ft^2)")


m, b = np.polyfit(school_pow, school_foot, 1)

x = [0, 100000000]
y = [m * point + b for point in x]
plt.plot(x, y, color="green")


for i in range(len(school_names)):
    if school_names[i] == "Francis W Parker School":
        plt.annotate(school_names[i], xy=(school_pow[i], school_foot[i])) # text, xy=()
        plt.scatter(school_pow[i], school_foot[i], s=8, c='green')
    if school_names[i] == "LaneTechHS-CPS":
        plt.annotate(school_names[i], xy=(school_pow[i], school_foot[i]))  # text, xy=()
        plt.scatter(school_pow[i], school_foot[i], s=8, c='green')
    if school_names[i][0] == "U":
        print(school_names[i])

plt.show()
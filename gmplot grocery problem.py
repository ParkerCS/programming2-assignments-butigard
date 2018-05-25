# In 2013, an interesting dataset was released for Chicago which identified a number of food deserts.
# In many areas of the city, there were no suitable grocery stores with adequate produce, meats, refrigerated, and frozen food sections
# Many areas were only served by corner stores and convenience stores.

# Using gmplot and the chicago grocery csv, which contains updated grocery store data, 
# create a map with the following characteristics.
# - Map is centered on Chicago at a zoom level that shows all stores (5pts)
# - All adequate grocery stores are plotted (could be scatterplot, circles, or markers) (use the one looks best to you) (10pts)
#   Inadequate grocery stores are NOT plotted (you decide what inadequate means)
# - Shows a heatmap which helps to visualize the greatest concentration of adequate stores. (10pts) 
#   Your heatmap should be optimized for the city level view.  Tweak the radius and maxIntensity to adjust blob.

from gmplot import *
import csv
apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"

mymap = GoogleMapPlotter(41.8781, -87.6298, 11, apikey=apikey)

with open("files/Grocery_Stores_-_2013.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

for i in range(len(data)):
    if "LIQUOR" in data[i][0]:
        del data[i]


print(data.pop(0))
lats = [float(data[x][14]) for x in range(len(data))]
longs = [float(data[x][15]) for x in range(len(data))]

mymap.heatmap(lats, longs, maxIntensity=10, radius=50, dissipating=True)

mymap.scatter(lats, longs, color="blue", marker=True, size=50)

mymap.draw("mymap.html")


# Challenges:  
# Instead of a heatmap, make each store a circle with varying size based on square footage of the store.  
# Filter out all liquor stores, drug stores, and convenience stores.
# Place markers or other indicators where you still see inadequate food access.

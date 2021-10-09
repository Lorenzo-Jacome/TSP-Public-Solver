from matplotlib import pyplot as plt
from geopy.geocoders import Nominatim

class tspSolver:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="LorenzoSuperApp")
        self.allCoordinates = [[],[],[]]

    #Recives a direction as string, adds its coordinates to the "allCordinates" list
    def getCoordinates(self, direction):
        location = self.geolocator.geocode(direction)
        self.allCoordinates[0].append(location.longitude)
        self.allCoordinates[1].append(location.latitude)
        self.allCoordinates[2].append(direction)

    #Based on variable "allCoordinates", generates a plot where [[X-COORDINATES], [Y-COORDINATES]]
    #generates a plot
    def generatePlot(self):
        plt.scatter(self.allCoordinates[0], self.allCoordinates[1])
        plt.plot(self.allCoordinates[0], self.allCoordinates[1])
        plt.show()

test = tspSolver()

test.getCoordinates("Mexico City")
test.getCoordinates("Puebla")
test.getCoordinates("Monterrey")
test.getCoordinates("Texas")
test.getCoordinates("California")

test.generatePlot()
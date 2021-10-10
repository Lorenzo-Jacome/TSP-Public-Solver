from matplotlib import pyplot as plt
from geopy.geocoders import Nominatim

class tspSolver:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="LorenzoSuperApp")
        self.coordinatesToPlot = [[],[],[]]

    #Recieves a direction as a string
    #Returns: [[X-COORDINATES], [Y-COORDINATES], [FULL ADDRESS]]
    def getCoordinates(self, direction):
        coordinatesMat = []

        location = self.geolocator.geocode(direction)

        coordinatesMat.append(location.longitude)
        coordinatesMat.append(location.latitude)
        coordinatesMat.append(location.address)

        return coordinatesMat

    def normalOrderVisits(matToProcess):
        resultMat = [[],[],[]]

        for i in matToProcess:
            resultMat[0].append(i[0])
            resultMat[1].append(i[1])
            resultMat[2].append(i[2])

        return resultMat

    #Based on variable "allCoordinates", generates a plot where [[X-COORDINATES], [Y-COORDINATES]]
    #generates a plot
    def generatePlot(self, xCoordinates, yCoordinates):
        plt.scatter(xCoordinates, yCoordinates)
        plt.plot(xCoordinates, yCoordinates)
        plt.show()

test = tspSolver()

print(test.getCoordinates("Serrania 72, pedregal, mexico city"))
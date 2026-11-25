class Train:
    def __init__(self, trainID, route):
        self.__trainID = trainID #STRING
        self.__route = route #INTEGER

    def GetTrainIDNumber(self):
        return self.__trainID

    def GetRoute(self):
        return self.__route

train1 = Train("12ADV", 134)
train2 = Train("33ART", 20)
train3 = Train("9FKF", 3)
train4 = Train("21VBC", 24)

class Station:
    def __init__(self, stationID, numberOfTrains, numberPlatform):
        self.__stationID = stationID #STRING
        self.__numberPlatform = numberPlatform #INTEGER
        self.__numberOfTrains = numberOfTrains # INTEGER
        self.__Trains = [] #ARRAY

    def AddTrain(self, train):
        if self.__numberOfTrains <= self.__numberPlatform:
            self.__Trains.append(train)
            return True
        else:
            return False
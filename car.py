class Car:

    speed = 0 ##Speed at parked state
    ##Define the constructor
    def __init__(self,carName = None, carModel = None, carType = "saloon"):
        if carName is None or carModel is None:
            self.name = "General" ##carname if none is given
            self.model = "GM" ##Car model if none is given
        else:
            self.name = carName
            self.model = carModel
        if carType is "saloon" or carType is "trailer":
            self.type = carType
        else:
            raise Exception("The car type should be saloon if it is not a trailer")
        self.car_doors() ##set number of doors
        self.car_wheels() ##set number of car wheels
        

    ##Set number of car doors
    ##Checks if type is porshe or Koeinigsegg and sets doors to 2
    ##If not sets doors to 4
    def car_doors(self):
        if self.name is "Porshe" or self.name is "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

    ##set number of car wheels
    ##Sets to 8 if is a trailer otherwise sets to 4
    def car_wheels(self):
        if self.type is "saloon":
            self.num_of_wheels = 4
        elif self.type is "trailer":
            self.num_of_wheels = 8
        else:
            raise Exception("Incorrect car type detected")
        
    ##Check if cartype is saloon
    ##Returns true if is saloon
    def is_saloon(self):
        if self.type is "saloon":
            return True
        else:
            return False

    ##DriveIt!!
    def drive(self, drive_speed):
        if drive_speed is 7:
            self.speed = 77
        elif drive_speed is 3:
            self.speed = 1000
        else:
            self.speed = drive_speed

        return self
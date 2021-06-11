class ParkingSystem:
    
    parks=[]
    def __init__(self, big: int, medium: int, small: int):
        self.parks = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.parks[0] >0:
            self.parks[0] -=1
            return True
        elif carType == 2 and self.parks[1] >0 :
            self.parks[1] -=1
            return True
        elif carType == 3 and self.parks[2] >0 :
            self.parks[2] -=1
            return True
        return False
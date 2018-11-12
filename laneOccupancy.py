from car import Car

class LaneOccupancy:
    def __init__(self):
        self.display_h = 1000
        self.display_w = 600
        self.ego_car = Car(id=-1,speed=5,top_pos=500,bottom_pos=540)
        self.car0 = Car(id=-1,speed=5,top_pos=100,bottom_pos=140)

    def grid_speed(self):
        []

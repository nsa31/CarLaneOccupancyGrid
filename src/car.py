
class Car:
    def __init__(self, id, speed, lane_id, top_pos, bottom_pos):
        self.id = id
        self.speed = speed
        self.lane_id = lane_id
        self.top_pos = top_pos
        self.bottom_pos = bottom_pos
        self.car_len = top_pos - bottom_pos

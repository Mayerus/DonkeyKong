_AUTHOR_ = "Omri Mayer"


class HitEventListener:

    def __init__(self, mario, barrels_list):
        self.Mario = mario
        self.Barrel_1 = barrels_list[0]
        self.Barrel_2 = barrels_list[1]
        self.Barrel_3 = barrels_list[2]
        self.Barrel_4 = barrels_list[3]
        self.Barrel_5 = barrels_list[4]
        self.Barrel_6 = barrels_list[5]

    def hit_listener(self):
        mx, my, dir = self.Mario.get_pos()
        px1, py1 = self.Barrel_1.get_pos()
        px2, py2 = self.Barrel_2.get_pos()
        px3, py3 = self.Barrel_3.get_pos()
        px4, py4 = self.Barrel_4.get_pos()
        px5, py5 = self.Barrel_5.get_pos()
        px6, py6 = self.Barrel_6.get_pos()
        cords = [(px1, py1), (px2, py2), (px3, py3), (px4, py4), (px5, py5), (px6, py6)]
        # checks if there's a collusion of any barrel with mario
        for pos in cords:
            if not ((not (not (not (my < pos[1] + 24 <= my + 24) or not (mx <= pos[0] + 12 <= mx + 24))) and not (
                    my < pos[1] <= my + 32 and mx <= pos[0] + 12 <= mx + 24) and not (
                    mx <= pos[0] + 24 < mx + 24) or not (my <= pos[1] + 12 <= my + 32)) and not (
                    not (not (mx < pos[0] <= mx + 24) or not (my <= pos[1] + 12 <= my + 32)))):
                return True

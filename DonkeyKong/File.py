import os
_AUTHOR_ = "Omri Mayer"


class LoadFile:
    def __init__(self, filename):
        self.filename = filename
        while not os.path.exists(filename + '.txt'):
            print("a game with such a name doesn't exists, try another name")
            self.filename = input()

    def load(self, barrels_list, Mario):
        """loads previous game"""
        file = open(self.filename + ".txt", 'r')
        data = file.read()
        lines = data.split("\n")
        m_pos = lines[0].split(",")
        m_x, m_y = float(m_pos[0]), float(m_pos[1])
        barrels_pos = lines[1].split(";")
        b1 = barrels_pos[0].split(",")
        b_x, b_y = float(b1[0]), float(b1[1])
        b2 = barrels_pos[1].split(",")
        b_x2, b_y2 = float(b2[0]), float(b2[1])
        b3 = barrels_pos[2].split(",")
        b_x3, b_y3 = float(b3[0]), float(b3[1])
        b4 = barrels_pos[3].split(",")
        b_x4, b_y4 = float(b4[0]), float(b4[1])
        b5 = barrels_pos[4].split(",")
        b_x5, b_y5 = float(b5[0]), float(b5[1])
        b6 = barrels_pos[5].split(",")
        b_x6, b_y6 = float(b6[0]), float(b6[1])
        count = float(lines[2])
        Mario.set_pos(m_x, m_y)
        barrels_list[0].set_pos(b_x, b_y)
        barrels_list[1].set_pos(b_x2, b_y2)
        barrels_list[2].set_pos(b_x3, b_y3)
        barrels_list[3].set_pos(b_x4, b_y4)
        barrels_list[4].set_pos(b_x5, b_y5)
        barrels_list[5].set_pos(b_x6, b_y6)
        lives = int(lines[3])
        file.close()
        return count, lives

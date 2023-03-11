class fbclass(object):
    def __init__(self):
        self.name = "fb"
        self.pos = (0,230)
        self.pulse = True
        self.acc = 2
        self.vel = -10
        self.alive = True

    #def __str__(self):



    def get_pos(self):
        x,y = self.pos
        self.vel += self.acc
        y += self.vel
        if y> 508:
            y = 508
        if y <= 0:
            y = 0

            
        self.pos = (x,y)
        return self.pos

    def fly(self):
        self.vel = -10



    def DieDie(self,y1,Y1):
        x,y = self.pos
        if y< y1:
            self.alive = False
            #print("Death")
            return True
        if y + 92 > Y1:
            self.alive = False
            #print("Death")
            return True

        
    def revive(self):
        self.alive = True
        #print("Revived")

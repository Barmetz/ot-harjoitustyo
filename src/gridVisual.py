import pygame, sys
from gridLogic import MSGrid
class Main():
    def __init__(self):
        pygame.init()
        self.windowheight = 555
        self.windowwidth = 555
        self.pad = 5
        self.squaresize = 50
        self.gridheight = 10
        self.gridwidth = 10
        self.mineTotal = 10
        self.gridObj = MSGrid(self.gridheight,self.gridwidth,self.mineTotal)
        self.HiddenCount = self.gridheight * self.gridwidth
        self.colors =  [(210,210,210), (150,150,150),(255,255,255)]
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.largefont = pygame.font.Font(pygame.font.get_default_font(), 100)
    
    def main(self):
        lose = False
        while True:
            self.Surface = pygame.display.set_mode((self.windowheight, self.windowwidth))
            self.drawsquares()
            self.drawnotHidden()
            mouse_y, mouse_x = 0, 0
            mouseleft = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    mouseleft = True
                elif event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
            pos_y, pos_x = self.getsquareMouse(mouse_y, mouse_x)
            if mouseleft and (pos_y, pos_x) != (None, None):
                if self.gridObj.grid[pos_y][pos_x].value == "M":
                    lose = True
                self.gridObj.grid[pos_y][pos_x].isHidden = False
                self.HiddenCount -= 1
                mouseleft = False
            
            if lose:
                self.drawText("Lost", self.windowheight/2, self.windowwidth/2, self.largefont, (255,0,0))
            if self.HiddenCount == self.mineTotal:
                self.drawText("Won", self.windowheight/2, self.windowwidth/2, self.largefont, (255,0,0))
            pygame.display.flip()

    def drawsquares(self):
        for j in range(self.gridheight):
            for i in range(self.gridwidth):
                pos_y, pos_x = self.getsquareCorner(j, i)
                if self.gridObj.grid[j][i].isHidden:
                    pygame.draw.rect(self.Surface, self.colors[1], (pos_y, pos_x,self.squaresize,self.squaresize))
                else:
                    pygame.draw.rect(self.Surface, self.colors[0], (pos_y, pos_x,self.squaresize,self.squaresize))

    def drawnotHidden(self):
        for j in range(self.gridheight):
            for i in range(self.gridwidth):
                if not self.gridObj.grid[j][i].isHidden:
                    pos_y, pos_x = self.getsquareCenter(j, i)
                    square = self.gridObj.grid[j][i]
                    self.drawText(square.value, pos_x, pos_y, self.font, self.colors[2]) 

    def drawText(self, text, y, x, font, color):
        textObj = font.render(text, True, color)
        textsquare = textObj.get_rect()
        textsquare.y = y-textsquare.height//2
        textsquare.x = x-textsquare.width//2
        self.Surface.blit(textObj, textsquare)

    def getsquareCorner(self, y, x):
        pos_y = self.pad + y*(self.squaresize+self.pad)
        pos_x = self.pad + x*(self.squaresize+self.pad)
        return pos_y, pos_x

    def getsquareCenter(self, y, x):
        pos_y = self.pad + y*(self.squaresize+self.pad)+self.squaresize/2
        pos_x = self.pad + x*(self.squaresize+self.pad)+self.squaresize/2
        return pos_y, pos_x

    def getsquareMouse(self, mouse_y, mouse_x):
        for j in range(self.gridheight):
            for i in range(self.gridwidth):
                pos_y, pos_x = self.getsquareCorner(j, i)
                square = pygame.Rect(pos_y, pos_x, self.squaresize,self.squaresize)
                if square.collidepoint(mouse_x, mouse_y):
                    return j, i
        return None, None
if __name__ == "__main__":
    a = Main()
    print(a.gridObj)
    a.main()
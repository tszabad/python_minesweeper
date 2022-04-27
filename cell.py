from tkinter import Button
import random
import settings


class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x= x
        self.y= y

        Cell.all.append(self)


    def create_btn_object(self, location):
        btn = Button(
            location,
            background="grey",
            width="2",
            height="1",
           
        )
        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click
        self.cell_btn_object = btn



    @staticmethod
    def create_mines():
        mine_objects = random.sample(Cell.all, settings.MINE_COUNT)
        for cell in Cell.all:
            if cell in mine_objects:
                cell.is_mine = True


    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
            for i in Cell.all:
                if i.is_mine == True:
                    i.cell_btn_object.configure(background="red")
        else:
            if self.count_mines == 0:
                for i in self.surround:
                    i.show_cell()

            self.show_cell()
            
    def show_mine(self):
        self.cell_btn_object.configure(background="red")

    
    def get_cell(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surround(self):
        surroundings = []
        surroundings.append(self.get_cell(self.x-1, self.y))
        surroundings.append(self.get_cell(self.x-1, self.y-1))
        surroundings.append(self.get_cell(self.x, self.y-1))
        surroundings.append(self.get_cell(self.x-1, self.y+1))
        surroundings.append(self.get_cell(self.x+1, self.y))
        surroundings.append(self.get_cell(self.x+1, self.y+1))
        surroundings.append(self.get_cell(self.x, self.y+1))
        surroundings.append(self.get_cell(self.x+1, self.y-1))
      

        final_cells = [c for c in surroundings if c is not None]
        return final_cells
        
    @property
    def count_mines(self):
        count = 0
        for i in self.surround:
            if i.is_mine:
                count += 1
        return count

    def show_cell(self):
        self.cell_btn_object.configure(background="white")
        self.cell_btn_object.configure(background="white", text = self.count_mines if self.count_mines !=0 else None)

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    def __repr__(self):
        return f"{self.x},{self.y}"
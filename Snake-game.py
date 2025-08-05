import tkinter as tk
import random

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SPEED = 150  

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Змейка на tkinter")

        self.canvas = tk.Canvas(root, width=GRID_WIDTH*CELL_SIZE, height=GRID_HEIGHT*CELL_SIZE, bg="black")
        self.canvas.pack()

        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.food = self.spawn_food()
        self.running = True

        self.root.bind("<Key>", self.change_direction)
        self.update()

    def spawn_food(self):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in self.snake:
                return pos

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key == "Down" and self.direction != (0, -1):
            self.direction = (0, 1)
        elif key == "Left" and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == "Right" and self.direction != (-1, 0):
            self.direction = (1, 0)

    def update(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        
        if (new_head in self.snake or
            not 0 <= new_head[0] < GRID_WIDTH or
            not 0 <= new_head[1] < GRID_HEIGHT):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(SPEED, self.update)

    def draw(self):
        self.canvas.delete("all")

        
        x, y = self.food
        self.canvas.create_rectangle(
            x * CELL_SIZE, y * CELL_SIZE,
            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill="red"
        )

        
        for i, (x, y) in enumerate(self.snake):
            color = "green" if i == 0 else "light green"
            self.canvas.create_rectangle(
                x * CELL_SIZE, y * CELL_SIZE,
                (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                fill=color
            )

    def game_over(self):
        self.running = False 
        self.canvas.create_text(
            GRID_WIDTH * CELL_SIZE // 2,
            GRID_HEIGHT * CELL_SIZE // 2,
            text="Game OVer",
            fill="white",
            font=("Arial", 24)
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

class Node:
    def __init__(self, canvas, name, x, y):
        self.x = x
        self.y = y
        self.radius = 22
        self.color = '#e1dd72'
        self.outline = 'black'
        self.active_color = '#a8c66c'
        self.disabled_color = '#db4c04'
        self.width = 1
        self.canvas = canvas
        self.type = "node"

        self.selected = False
        self.disabled = False
        self.related_channels = []
        self.name = name
        queue = []

        self.draw()
        self.canvas.tag_bind(self.view, '<B1-Motion>', self.move)
        self.canvas.tag_bind(self.view, '<Button-1>', self.select)
        self.canvas.tag_bind(self.view, '<Button-3>', self.disable)

    def draw(self):
        x1 = self.x - self.radius
        x2 = self.x + self.radius
        y1 = self.y - self.radius
        y2 = self.y + self.radius

        self.view = self.canvas.create_oval(x1, y1, x2, y2, tag='node', outline=self.outline, width=2,
                                            fill=self.color)
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        self.text = self.canvas.create_text(center_x, center_y, font=("Time New Roman", 14), text=str(self.name))

    def move(self, event):
        self.canvas.move(self.view, event.x - self.x, event.y - self.y)
        self.canvas.move(self.text, event.x - self.x, event.y - self.y)
        for element in self.related_channels:
            if (element.x1, element.y1) == (self.x, self.y):
                element.canvas.coords(element.view, event.x, event.y, element.x2, element.y2)
                element.canvas.coords(element.text, (element.x2 + event.x) // 2, (element.y2 + event.y) // 2)
                element.x1 = event.x
                element.y1 = event.y
            elif (element.x2, element.y2) == (self.x, self.y):
                element.canvas.coords(element.view, element.x1, element.y1, event.x, event.y)
                element.canvas.coords(element.text, (element.x1 + event.x) // 2, (element.y1 + event.y) // 2)
                element.x2 = event.x
                element.y2 = event.y
        self.x = event.x
        self.y = event.y

    def select(self, event):
        if self.selected and not self.disabled:
            self.canvas.itemconfig(self.view, fill=self.color)
            self.selected = False
        elif not self.selected and not self.disabled:
            self.canvas.itemconfig(self.view, fill=self.active_color)
            self.selected = True

    def disable(self, event):
        if self.disabled:
            self.canvas.itemconfig(self.view, fill=self.color)
            self.disabled = False
        else:
            self.canvas.itemconfig(self.view, fill=self.disabled_color)
            self.disabled = True

    def delete(self):
        self.canvas.delete(self.view)
        self.canvas.delete(self.text)

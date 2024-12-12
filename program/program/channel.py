
class Channel:
    def __init__(self, canvas, nodes, channel_type, positions, weight, is_satellite=False):
        self.first_node, self.second_node = nodes
        self.x1, self.y1, self.x2, self.y2 = positions
        self.canvas = canvas
        self.duplex_color = '#000000'
        self.half_duplex_color = '#00BFFF'

        self.active_color = '#00ff26'
        self.disabled_color = 'red'
        self.path_color = 'crimson'
        self.path_width = 3
        self.width = 3
        self.active_width = 5
        self.current_color = "red"

        self.selected = False
        self.disabled = False
        self.type = channel_type
        self.is_satellite = is_satellite

        if self.is_satellite:
            self.weight = weight*3
        else:
            self.weight = weight

        self.error_prob = 0.00

        self.draw()
        self.canvas.tag_bind(self.view, '<Button-1>', self.select)
        self.canvas.tag_bind(self.view, '<Button-3>', self.disable)

    def draw(self):
        if self.type == 'duplex':
            self.current_color = self.duplex_color
        elif self.type == 'half-duplex':
            self.current_color = self.half_duplex_color

        if self.is_satellite:
            self.view = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                                            fill=self.current_color, activefill=self.active_color,
                                            width=self.width, activewidth=self.active_width, dash=(8, 2))

            self.text = self.canvas.create_text(int((self.x1 + self.x2) / 2), int((self.y1 + self.y2) / 2 - 20),
                                            font=("Time New Roman", 10), text=f"{self.weight//3}  ({self.weight})", fill="#FF00FF")
        else:
            self.view = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                                            fill=self.current_color, activefill=self.active_color,
                                            width=self.width, activewidth=self.active_width)

            self.text = self.canvas.create_text(int((self.x1 + self.x2) / 2), int((self.y1 + self.y2) / 2 - 14),
                                            font=("Time New Roman", 10), text=str(self.weight), fill="#FF00FF")

    def select(self, event):
        if self.selected and not self.disabled:
            self.canvas.itemconfig(self.view, fill=self.current_color)
            self.selected = False
        elif not self.selected and not self.disabled:
            self.canvas.itemconfig(self.view, fill=self.active_color)
            self.selected = True

    def disable(self, event):
        if self.disabled:
            self.canvas.itemconfig(self.view, fill=self.current_color)
            self.disabled = False
        else:
            self.canvas.itemconfig(self.view, fill=self.disabled_color)
            self.disabled = True

    def delete(self):
        self.canvas.delete(self.view)
        self.canvas.delete(self.text)


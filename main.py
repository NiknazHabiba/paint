
import tkinter as tk
from tkinter import ttk, colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk, ImageColor


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Paint App")
        self.root.geometry("1024x768")

        # Default settings
        self.current_tool = "pencil"
        self.current_pencil_style = "solid"
        self.current_shape = None
        self.color = "#000000"
        self.bg_color = "#FFFFFF"
        self.pen_width = 5
        self.eraser_width = 20

        # Image for canvas
        self.image = Image.new("RGB", (1024, 768), self.bg_color)
        self.draw = ImageDraw.Draw(self.image)

        # Initialize UI
        self.create_toolbar()
        self.create_canvas()

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg="#DDDDDD", height=50)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Pencil menu
        pencil_menu = ttk.Menubutton(toolbar, text="Pencil Styles")
        pencil_menu.menu = tk.Menu(pencil_menu, tearoff=0)
        pencil_menu["menu"] = pencil_menu.menu
        for style in ["solid", "dotted", "wavy"]:
            pencil_menu.menu.add_radiobutton(
                label=style.capitalize(),
                command=lambda s=style: self.set_pencil_style(s)
            )
        pencil_menu.pack(side=tk.LEFT, padx=5)

        # Pen size spinbox
        self.pen_size_spinbox = ttk.Spinbox(toolbar, from_=1, to=50, width=5, command=self.update_pen_size)
        self.pen_size_spinbox.set(self.pen_width)
        self.pen_size_spinbox.pack(side=tk.LEFT, padx=5)

        # Eraser button
        ttk.Button(toolbar, text="Eraser", command=lambda: self.select_tool("eraser")).pack(side=tk.LEFT, padx=5)

        # Shapes menu
        shape_menu = ttk.Menubutton(toolbar, text="Shapes")
        shape_menu.menu = tk.Menu(shape_menu, tearoff=0)
        shape_menu["menu"] = shape_menu.menu
        for shape in ["rectangle", "oval", "line"]:
            shape_menu.menu.add_radiobutton(
                label=shape.capitalize(),
                command=lambda s=shape: self.select_tool("shape", s)
            )
        shape_menu.pack(side=tk.LEFT, padx=5)

        # Fill button
        ttk.Button(toolbar, text="Fill", command=lambda: self.select_tool("fill")).pack(side=tk.LEFT, padx=5)

        # Color picker
        self.color_btn = ttk.Button(toolbar, text="Color", command=self.select_color)
        self.color_btn.pack(side=tk.LEFT, padx=5)

        # Color palette
        self.create_color_palette(toolbar)

        # Save/Open buttons
        ttk.Button(toolbar, text="Save", command=self.save_image).pack(side=tk.RIGHT, padx=5)
        ttk.Button(toolbar, text="Open", command=self.open_image).pack(side=tk.RIGHT, padx=5)

    def create_color_palette(self, toolbar):
        colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF",
                  "#00FFFF", "#800000", "#808000", "#008080", "#808080"]
        for idx, color in enumerate(colors):
            btn = tk.Button(toolbar, bg=color, width=2, height=1,
                            command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=2 if idx % 5 else 10, pady=5)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", width=1024, height=768)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_tool)
        self.canvas.bind("<ButtonRelease-1>", self.reset_draw)

        self.start_x = self.start_y = None
        self.current_item = None

    def set_pencil_style(self, style):
        self.current_pencil_style = style

    def select_tool(self, tool, shape=None):
        self.current_tool = tool
        if tool == "shape":
            self.current_shape = shape

    def select_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def set_color(self, color):
        self.color = color

    def update_pen_size(self):
        self.pen_width = int(self.pen_size_spinbox.get())

    def start_draw(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.current_tool == "fill":
            self.flood_fill(event.x, event.y)

    def draw_tool(self, event):
        if self.current_tool == "pencil":
            if self.current_pencil_style == "solid":
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                        fill=self.color, width=self.pen_width, capstyle=tk.ROUND, smooth=tk.TRUE)
                self.draw.line((self.start_x, self.start_y, event.x, event.y), fill=self.color, width=self.pen_width)
            elif self.current_pencil_style == "dotted":
                x1, y1 = self.start_x, self.start_y
                x2, y2 = event.x, event.y
                self.canvas.create_oval(x1, y1, x1 + self.pen_width, y1 + self.pen_width, fill=self.color)
                self.draw.ellipse((x1, y1, x1 + self.pen_width, y1 + self.pen_width), fill=self.color)
            elif self.current_pencil_style == "wavy":
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                        fill=self.color, width=self.pen_width, dash=(4, 2))
                self.draw.line((self.start_x, self.start_y, event.x, event.y), fill=self.color, width=self.pen_width)
            self.start_x, self.start_y = event.x, event.y
        elif self.current_tool == "eraser":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                    fill=self.bg_color, width=self.eraser_width, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.start_x, self.start_y = event.x, event.y
        elif self.current_tool == "shape" and self.current_shape:
            if self.current_item:
                self.canvas.delete(self.current_item)
            if self.current_shape == "rectangle":
                self.current_item = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y,
                                                                 outline=self.color, width=self.pen_width)
            elif self.current_shape == "oval":
                self.current_item = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y,
                                                            outline=self.color, width=self.pen_width)
            elif self.current_shape == "line":
                self.current_item = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                                            fill=self.color, width=self.pen_width)

    def reset_draw(self, event):
        if self.current_tool == "shape" and self.current_shape and self.current_item:
            coords = self.canvas.coords(self.current_item)
            if self.current_shape == "rectangle":
                self.draw.rectangle(coords, outline=self.color, width=self.pen_width)
            elif self.current_shape == "oval":
                self.draw.ellipse(coords, outline=self.color, width=self.pen_width)
            elif self.current_shape == "line":
                self.draw.line(coords, fill=self.color, width=self.pen_width)
            self.current_item = None

    def flood_fill(self, x, y):
        target_color = self.image.getpixel((x, y))
        fill_color = ImageColor.getcolor(self.color, "RGB")

        if target_color == fill_color:
            return

        edge = [(x, y)]
        while edge:
            new_edge = []
            for (x, y) in edge:
                if (0 <= x < self.image.width and 0 <= y < self.image.height
                        and self.image.getpixel((x, y)) == target_color):
                    self.image.putpixel((x, y), fill_color)
                    new_edge.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
            edge = new_edge

        self.refresh_canvas()

    def refresh_canvas(self):
        tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=tk_image, anchor=tk.NW)
        self.canvas.image = tk_image

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All files", "*.*")])
        if file_path:
            opened_image = Image.open(file_path)
            self.image.paste(opened_image, (0, 0))
            self.refresh_canvas()


# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()

### 🖌️ **Python Paint App - README** 🎨

---

#### **Overview**
Welcome to the **Python Paint App**, a powerful, feature-rich, and highly customizable painting tool built with Python's `tkinter` module and enhanced with `Pillow` for seamless image handling. Whether you're sketching, doodling, or creating art, this app offers intuitive controls and a versatile set of tools to turn your ideas into reality.

---

#### **Features**

🔧 **Toolbar Tools**:
- **Pencil Styles**: Choose from **Solid**, **Dotted**, or **Wavy** lines to match your artistic flow.
- **Eraser**: Quickly clean up your canvas with adjustable eraser sizes.
- **Shape Drawing**: Create **Rectangles**, **Ovals**, **Lines**, **Triangles**, and **Diamonds** effortlessly.
- **Text Tool**: Add text annotations anywhere on the canvas.
- **Fill Tool**: Quickly flood areas with a solid color.

🎨 **Customization Options**:
- **Color Picker**: Select from a wide range of colors or use the predefined palette for quick access.
- **Pen Size**: Adjustable pen width for finer control.

📁 **File Management**:
- **Save Your Work**: Save your creations as `.png` images.
- **Open Existing Files**: Load images directly onto the canvas to edit or draw over.

🖥️ **Responsive Canvas**:
- Full-screen support with the `Esc` key for easy exit.
- Real-time **cursor position tracking** for precise drawing.

💾 **Persistence**:
- All text items and shapes are seamlessly integrated into the saved image.

---

#### **Getting Started**

1. **Install Required Libraries**:
   ```bash
   pip install pillow
   ```

2. **Run the Application**:
   Save the code to a file named `paint_app.py` and run it:
   ```bash
   python paint_app.py
   ```

3. **Start Creating**:
   - Use the toolbar to select tools and colors.
   - Draw directly on the canvas, and use the text or fill tools for additional customization.

---

#### **How to Use**

- **Pencil Tool**: Select your desired style (Solid, Dotted, Wavy) and start drawing.
- **Shapes**: Choose a shape from the `Shapes` menu and draw it by dragging your mouse.
- **Text**: Click on the canvas to create a text entry box. Type your text and hit `Enter` to place it.
- **Color Palette**: Click on any color or use the color picker to choose a custom shade.
- **File Options**:
  - **Save**: Save your masterpiece as a `.png` file.
  - **Open**: Load an image file onto the canvas to edit.

---

#### **Pro Tips**

- Use the **Pen Size Spinbox** to adjust the thickness of your pencil, shapes, or eraser for finer details or broader strokes.
- Use **Fill** to quickly apply background colors or fill areas with a specific hue.
- For **text precision**, you can position the entry box and edit before committing it to the canvas.
- The **Fullscreen Mode** is perfect for large-screen drawing. Exit anytime with the `Esc` key.

---

#### **Technical Details**

- **Languages & Libraries**:
  - Python 3.x
  - `tkinter`: For GUI development.
  - `Pillow (PIL)`: For image manipulation and saving.

- **Code Highlights**:
  - Flood Fill Algorithm: Used to fill areas with a selected color.
  - Real-time Shape Drawing: Draw and preview shapes as you move the mouse.
  - Text Persistence: Ensures text is saved as part of the image file.

---

#### **Planned Features**
- Undo/Redo functionality for quick edits.
- Layer support for complex artwork.
- Advanced brushes and effects.

---

#### **Contributions**
Want to add your touch to this project? Fork the repository or send your suggestions to the author. Together, we can make this tool even more awesome!

---

Enjoy your creative journey with **Python Paint App**! 🚀
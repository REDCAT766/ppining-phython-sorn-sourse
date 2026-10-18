import tkinter as tk
import math

class SpinningPalFace:
    def __init__(self, root):
        self.root = root
        self.root.title("Spinning Pal Face")
        
        # Setup Canvas
        self.canvas = tk.Canvas(root, width=400, height=400, bg="#1a1a1a")
        self.canvas.pack()
        
        self.angle = 0  # Rotation angle tracker
        self.update_animation()

    def rotate_point(self, x, y, cx, cy, angle_rad):
        """Rotates a point (x, y) around a center (cx, cy) by angle_rad."""
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Translate to origin
        nx = x - cx
        ny = y - cy
        
        # Rotate and translate back
        rx = nx * cos_a - ny * sin_a + cx
        ry = nx * sin_a + ny * cos_a + cy
        return rx, ry

    def draw_pal_face(self):
        self.canvas.delete("all")
        cx, cy = 200, 200  # Center of rotation
        rad = math.radians(self.angle)
        
        # 1. Yellow Head Base
        x1, y1 = self.rotate_point(100, 100, cx, cy, rad)
        x2, y2 = self.rotate_point(300, 300, cx, cy, rad)
        # Use a bounding box approximation or center circle for the base head
        self.canvas.create_oval(cx-100, cy-100, cx+100, cy+100, fill="#EBA33F", outline="#D18C2C", width=3)
        
        # 2. Left Eye
        le_cx, le_cy = self.rotate_point(160, 175, cx, cy, rad)
        self.canvas.create_oval(le_cx-12, le_cy-18, le_cx+12, le_cy+18, fill="white", outline="black", width=2)
        # Pupil
        lp_cx, lp_cy = self.rotate_point(160, 175, cx, cy, rad)
        self.canvas.create_oval(lp_cx-6, lp_cy-6, lp_cx+6, lp_cy+6, fill="black")

        # 3. Right Eye (Slightly larger/goofy style)
        re_cx, re_cy = self.rotate_point(240, 170, cx, cy, rad)
        self.canvas.create_oval(re_cx-14, re_cy-20, re_cx+14, re_cy+20, fill="white", outline="black", width=2)
        # Pupil
        rp_cx, rp_cy = self.rotate_point(240, 170, cx, cy, rad)
        self.canvas.create_oval(rp_cx-7, rp_cy-7, rp_cx+7, rp_cy+7, fill="black")
        
        # 4. The Iconic Open Mouth Grin
        # Coordinates defining the open smile polygon
        mouth_points = [
            (150, 230), (250, 225), (240, 275), (165, 275)
        ]
        rotated_mouth = []
        for pt in mouth_points:
            rotated_mouth.extend(self.rotate_point(pt[0], pt[1], cx, cy, rad))
            
        self.canvas.create_polygon(rotated_mouth, fill="#7A1F1D", outline="black", width=3)

        # 5. Red Tongue
        tongue_points = [
            (175, 260), (230, 258), (225, 275), (180, 275)
        ]
        rotated_tongue = []
        for pt in tongue_points:
            rotated_tongue.extend(self.rotate_point(pt[0], pt[1], cx, cy, rad))
            
        self.canvas.create_polygon(rotated_tongue, fill="#E65C5C")

    def update_animation(self):
        self.angle = (self.angle + 3) % 360  # Adjust spin speed here
        self.draw_pal_face()
        self.root.after(20, self.update_animation) # ~50 FPS

if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningPalFace(root)
    root.mainloop()

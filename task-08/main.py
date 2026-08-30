import cv2
import glob
import numpy as np
import re
from PIL import Image, ImageDraw


path = "assets/*.png"
files = sorted(
    glob.glob(path),
    key=lambda x: int(re.search(r'Layer\s+(\d+)', x).group(1)))

images = []

for file in files:    
    img = cv2.imread(file)
    if img is not None:
        images.append(img)

blank_img = np.ones_like(images[0])*255
img
points = []
colors = []


for i in range(1,len(images)):
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    corner = cv2.goodFeaturesToTrack(gray,1,0.01,10)
    if corner is not None:
        corner = np.intp(corner)
        x, y = corner[0,0]
        points.append((x,y))
        
        color = images[i][y,x]
        colors.append(tuple(color.tolist()))

        cv2.circle(blank_img, (x, y), 3, color.tolist(), -1)
    else:
        points.append((-1,-1))
        colors.append(None)


blank_img = cv2.cvtColor(blank_img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(blank_img)
draw = ImageDraw.Draw(pil_img)


for i in range(1, len(points)):

    previous_point = points[i - 1]
    current_point = points[i]

    if previous_point == (-1, -1) or current_point == (-1, -1):  # <-- CHANGE
        continue

    draw.line(
        [previous_point, current_point],
        fill=colors[i-1][::-1],
        width=3
    )

pil_img.save("starry_night.png")

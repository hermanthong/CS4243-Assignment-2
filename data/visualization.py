import csv
from PIL import Image, ImageDraw
import numpy as np
frame_50 = Image.open('frame_0050.jpg')
labels = {}
with open('gt.csv') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        if int(row[0]) <= 50 and row[1] in ['9', '15', '19']:
            if row[1] not in list(labels):
                labels[row[1]] = []
            labels[row[1]].append({'frame': int(row[0]), 'bb_left': float(row[2]), 'bb_top': float(row[3]), 'bb_width': float(row[4]), 'bb_height': float(row[5])})


draw = ImageDraw.Draw(frame_50)
for id in labels:
    points = []
    for bbox in labels[id]:
        cx = bbox['bb_left'] + bbox['bb_width']/2
        cy = bbox['bb_top'] + bbox['bb_height']/2
        points.append((int(cx), int(cy)))
    draw.line(points, width=2, fill='white')
    

frame_50.save('trajectory.png')
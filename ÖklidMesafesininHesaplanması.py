import math

points = [(1,2), (4,6), (2,7), (-1,4)]

def euclideanDistance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

pointCount = len(points)
distances = []

for i in range(pointCount-1):
    for j in range(i+1, pointCount):
        distances.append(euclideanDistance(points[i], points[j]))

min = distances[0]
for i in range(1, len(distances)):
    if(distances[i] < min):
        min = distances[i]

print("minimum distance: " + str(min))
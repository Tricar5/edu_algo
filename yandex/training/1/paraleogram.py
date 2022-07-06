
point_list = []
num = int(input())

for i in range(num):

    s = input()

    points = []
    nums = [int(n) for n in s.split()]

    for i in range(1, 8, 2):
        points.append((nums[i-1], nums[i]))

    point_list.append(points)

# Algorythm

# Посчитать расстояния между точками


# Длина отрезков в координатах a = sqrt((x2 - x1)^2 + (y2 - y1)^2)

def pointDistance(p1, p2):

    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5

def magnitudePoints(p1, p2):

    return (p2[0] - p1[0], p2[1] - p1[0])

def getMidPoint(p1, p2):
    return ((p1[0] + p2[0])/2 , (p1[1] + p2[1]) / 2)

def checkParalleogram(points):

    midpoints = {}

    for i in range(4):
        for j in range(i, 4):
            if i != j:
                mid_p = getMidPoint(points[i], points[j])
                if mid_p not in midpoints.keys():
                    midpoints[mid_p] = []

                midpoints[mid_p].append((points[i], points[j]))


    if len(midpoints.keys()) == 5:
        return 'YES'

    return 'NO'


for i in range(num):
    print(checkParalleogram(point_list[i]))
"""
На парковке в торговом центре N мест (занумерованных от 1 до N).
За день в ТЦ приезжало М автомобилей, при этом некоторые из них
длинные и занимали несколько подряд идущих парковочных мест.
Для каждого автомобиля известно время приезда и отъезда, а также
два числа - с какого по какое парковочные места он занимал.
Если в какой-то момент времени один автомобиль уехал
с парковочного места, то место считается освободившимся
и в тот же момент времени на его место может встать другой
Необходимо определить, был ли момент, в который были заняты
все парковочные места.
"""

def isparkingfull(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timein, -1, placeto - placefrom + 1))

    events.sort()
    occupied = 0

    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]

        if occupied == n:
            return True
    return False

# Минимальное кол-во автомобилей в полном паркинге

def mincarsonfullparking(cars, n):
    events = []
    for i in range(len(cars)):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto - placefrom + 1, i))
        events.append((timein, -1, placeto - placefrom + 1, i))

    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1

    for i in range(len(events)):

        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1

    carnums = set()
    nowcars = 0

    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars == mincars:
            return carnums

    return set()


#
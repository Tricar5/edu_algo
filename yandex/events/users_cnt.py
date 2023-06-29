# Макс число посетителей

def max_visitor_online(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], 1))
        events.append((tout[i], -1))

    events.sort()
    online = 0
    maxonline = 0
    for event in events:
        if event[1] == 1:
            online += 1
        else:
            online -= 1
        maxonline = max(online, maxonline)
    return maxonline


# Время когда кто-то на сайте

def time_with_visitors(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], 1))
        events.append((tout[i], -1))

    events.sort()
    online = 0
    notemptytime = 0
    for i in range(len(events)):
        if online > 0:
            notemptytime += events[i][0] - events[i - 1][0]
        if events[i][1] == 1:
            online += 1
        else:
            online -= 1

    return notemptytime


def max_visitorы_online(n, tin, tout, m, tboss):
    events = []
    for i in range(n):
        events.append((tin[i], 1))
        events.append((tout[i], -1))

    for i in range(m):
        events.append((tboss[i], 0))

    events.sort()
    online = 0
    bossans = []
    for i in range(len(events)):
        if events[i][1] == 1:
            online += 1
        elif events[i][i]:
            online -= 1
        else:
            bossans.append(online)
    return bossans

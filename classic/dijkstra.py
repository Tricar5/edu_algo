# initializing hash tables

graph = {}
costs = {}
parents = {}


# appending nodes and their distances to each other into graph structure

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}


# determing cost's table

infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 3
costs['fin'] = infinity

# creating parents table

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

proceed = []


def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in proceed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)  # начинаем с узла с наименьшей стоимостью среди необработанных

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]

        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    proceed.append(node)

    node = find_lowest_cost_node(costs)
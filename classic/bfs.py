from collections import deque

graph = {}

graph['you'] = ['alice', 'bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom','jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['tom'] = []
graph['jonny'] = []

sellers = {'anuj'}


def is_seller(name):
    return (name in sellers)


def bfs_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        print(searched)
        print(search_queue)
        person = search_queue.popleft()

        if not person in searched:
            if is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, node):
        if not isinstance(node, Node):
            raise ValueError("Only instances of Node class can be enqueued.")
        self.queue.append(node)
        self.queue.sort(key=lambda x: x.d)  

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.color = 'white'  
        self.d = 0  
        self.p = None  
    def __repr__(self):
        return '({}, {})'.format(self.i, self.j)

def BFS(s,G,d):
    G[s.i][s.j].color = 'gray'
    cq = PriorityQueue()
    cq.enqueue(G[s.i][s.j])
    while len(cq) != 0:
        u =cq.dequeue()
        L = []
        if u.i+2 <= 7 and u.j+1 <= 7:
            L.append((u.i+2,u.j+1))
        if u.i+2 <= 7 and u.j- 1 >=0:
            L.append((u.i+2,u.j-1))
        if u.i-2 >= 0 and u.j+1 <=7:
            L.append((u.i-2,u.j+1))
        if u.i-2 >= 0 and u.j- 1 >=0:
            L.append((u.i-2,u.j-1))
        if u.i+1 <= 7 and u.j+2 <=7:
            L.append((u.i+1,u.j+2))
        if u.i+1 <= 7 and u.j-2 >=0:
            L.append((u.i+1,u.j-2))
        if u.i-1 >= 0 and u.j+2 <=7:
            L.append((u.i-1,u.j+2))
        if u.i-1 >=0 and u.j-2 >=0:
            L.append((u.i-1,u.j-2))
        
        for x in L:
            i= x[0]
            j= x[1]
            if G[i][j].color == 'white':
                G[i][j].color = 'gray'
                G[i][j].d = u.d + 1
                G[i][j].p = u
                cq.enqueue(G[i][j])
        u.color = 'black'
    dest = None
    for row in G:
        for y in row:
            if y.i == d[0] and y.j == d[1]:
                dest = y
                break
        if dest:
            break

    return dest

def Print_Path(s,d):
    if d.i == s.i and d.j == s.j:
        print(s.i, s.j)
    elif d.p == None:
        print('no path from ',(s.i, s.j),'to ',(d.i, d.j))
    else:
        Print_Path(s,d.p)
        print('(',d.i,',',d.j,')')

user_input = input('Enter the starting square: ')
s = tuple(int(item) for item in user_input.split())

user_input1 = input('Enter the destination square: ')
d = tuple(int(item) for item in user_input1.split())

G = [[Node(i, j) for j in range(8)] for i in range(8)]
s = Node(s[0], s[1])

destination_node = BFS(s, G, d)
if destination_node:
    Print_Path(s, destination_node)
else:
    print('Destination node not found.')
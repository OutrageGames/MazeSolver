import queue

maze = [["0","I", "0", "0", "0"],
        ["0"," ", " ", " ", "0"],
        ["0"," ", "0", " ", "0"],
        ["0"," ", "0", " ", "0"],
        ["0"," ", " ", " ", "0"],
        ["0","G", "0", "0", "0"]]

def ShowResult(maze, path=""):
    for x, index in enumerate(maze[0]):
        if index == "I":
            arxh = x

    i = arxh
    j = 0
    index = set()
    for kinhsh in path:
        if kinhsh == "A": i -= 1
        elif kinhsh == "D": i += 1
        elif kinhsh == "P": j -= 1
        elif kinhsh == "K": j += 1
        index.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in index:
                print("1 ", end="")
            else:
                print(col + " ", end="")
        print()
        


def Valid(maze, kinhseis):
    for x, index in enumerate(maze[0]):
        if index == "I":
            arxh = x

    i = arxh
    j = 0
    for kinhsh in kinhseis:
        if kinhsh == "A": i -= 1
        elif kinhsh == "D": i += 1
        elif kinhsh == "P": j -= 1
        elif kinhsh == "K": j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "0"):
            return False

    return True


def Telos(maze, kinhseis):
    for x, index in enumerate(maze[0]):
        if index == "I":
            arxh = x

    i = arxh
    j = 0
    for kinhsh in kinhseis:
        if kinhsh == "A": i -= 1
        elif kinhsh == "D": i += 1
        elif kinhsh == "P": j -= 1
        elif kinhsh == "K": j += 1

    if maze[j][i] == "G":
        print("DIADROMH: " + kinhseis)
        ShowResult(maze, kinhseis)
        return True

    return False



queue = queue.Queue()
queue.put("")
path = ""

while not Telos(maze, path): 
    path = queue.get()
    for j in ["A", "D", "P", "K"]:
        put = path + j
        if Valid(maze, put):
            queue.put(put)
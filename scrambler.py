from tkinter.constants import W
import kociemba
import random
import conf

corners = None
corner_orientations = None
edges = None
edge_orientations = None

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def rotate(l, i):
    if i == 0:
        return
    son = l[0]
    for j in range(len(l)-1):
        l[j] = l[j+1]
    l[-1] = son
    rotate(l, i-1)
    return l

def replace_corner(c, place, cube):
    if place == 0:
        cube[0][6] = c[0]
        cube[2][0] = c[1]
        cube[1][2] = c[2]
    elif place == 1:
        cube[0][8] = c[0]
        cube[3][0] = c[1]
        cube[2][2] = c[2]
    elif place == 2:
        cube[0][2] = c[0]
        cube[4][0] = c[1]
        cube[3][2] = c[2]
    elif place == 3:
        cube[0][0] = c[0]
        cube[1][0] = c[1]
        cube[4][2] = c[2]
    elif place == 4:
        cube[5][0] = c[0]
        cube[1][8] = c[1]
        cube[2][6] = c[2]
    elif place == 5:
        cube[5][2] = c[0]
        cube[2][8] = c[1]
        cube[3][6] = c[2]
    elif place == 6:
        cube[5][8] = c[0]
        cube[3][8] = c[1]
        cube[4][6] = c[2]
    elif place == 7:
        cube[5][6] = c[0]
        cube[4][8] = c[1]
        cube[1][6] = c[2]

def replace_edge(c, place, cube):
    if place == 0:
        cube[0][3] = c[0]
        cube[1][1] = c[1]
    if place == 1:
        cube[0][7] = c[0]
        cube[2][1] = c[1]
    if place == 2:
        cube[0][5] = c[0]
        cube[3][1] = c[1]
    if place == 3:
        cube[0][1] = c[0]
        cube[4][1] = c[1]
    if place == 4:
        cube[2][3] = c[0]
        cube[1][5] = c[1]
    if place == 5:
        cube[2][5] = c[0]
        cube[3][3] = c[1]
    if place == 6:
        cube[4][3] = c[0]
        cube[3][5] = c[1]
    if place == 7:
        cube[4][5] = c[0]
        cube[1][3] = c[1]
    if place == 8:
        cube[5][3] = c[0]
        cube[1][7] = c[1]
    if place == 9:
        cube[5][1] = c[0]
        cube[2][7] = c[1]
    if place == 10:
        cube[5][5] = c[0]
        cube[3][7] = c[1]
    if place == 11:
        cube[5][7] = c[0]
        cube[4][7] = c[1]

def getCornerPiece(i):
    if i == 0:
        return ['U', 'F', 'L']
    if i == 1:
        return ['U', 'R', 'F']
    if i == 2:
        return ['U', 'B', 'R']
    if i == 3:
        return ['U', 'L', 'B']
    if i == 4:
        return ['D', 'L', 'F']
    if i == 5:
        return ['D', 'F', 'R']
    if i == 6:
        return ['D', 'R', 'B']
    if i == 7:
        return ['D', 'B', 'L']

def getEdgePiece(i):
    if i == 0:
        return ['U', 'L']
    if i == 1:
        return ['U', 'F']
    if i == 2:
        return ['U', 'R']
    if i == 3:
        return ['U', 'B']
    if i == 4:
        return ['F', 'L']
    if i == 5:
        return ['F', 'R']
    if i == 6:
        return ['B', 'R']
    if i == 7:
        return ['B', 'L']
    if i == 8:
        return ['D', 'L']
    if i == 9:
        return ['D', 'F']
    if i == 10:
        return ['D', 'R']
    if i == 11:
        return ['D', 'B']

def getCube():
    cube = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    #* Corners
    for i in range(8):
        c = getCornerPiece(i)
        rotate(c, corner_orientations[i])
        replace_corner(c, corners[i], cube)
        # print('piece ', corners[i], c, 'placed on place', i)

    #* Edges
    for i in range(12):
        c = getEdgePiece(i)
        rotate(c, edge_orientations[i])
        replace_edge(c, edges[i], cube)
    
    #* Centers
    cube[0][4] = 'U'
    cube[1][4] = 'L'
    cube[2][4] = 'F'
    cube[3][4] = 'R'
    cube[4][4] = 'B'
    cube[5][4] = 'D'

    return ''.join(cube[0][:] + cube[3][:] + cube[2][:] + cube[5][:] + cube[1][:] + cube[4][:])

#* Parameters
moveEdgeCount = 6
allowEdgeCycles = False
dontUseEdges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0] 
edgeTwistCount = 0

moveCornerCount = 0
allowCornerCycles = False
dontUseCorners = [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1] 
cornerTwistCount = 0

edgeSequence = ''
cornerSequence = ''

#* Scrambling Edges
def getEdgeNext(nxt=None):
    if nxt==None:
        nxt = random.randint(0, 23)
        while used[nxt]:
            nxt = random.randint(0, 23)
    if nxt%12 == buffer%12:
        return buffer
    global edgeSequence
    edgeSequence += conf.edgeLetters[nxt]
    swap(edges, buffer%12, nxt%12)
    swap(edge_orientations, buffer%12, nxt%12)
    edge_orientations[nxt%12] += nxt//12
    edge_orientations[buffer%12] += 2-nxt//12
    return nxt

def setUsedEdge(nxt):
    global used
    used[nxt%12] = used[nxt%12+12] = 1

def unsetUsedEdge(nxt):
    global used
    used[nxt%12] = dontUseEdges[nxt%12]
    used[nxt%12+12] = dontUseEdges[nxt%12+12]
    
def scrambleEdges():
    global buffer
    global used
    global dontUseEdges
    count = 0
    buffer = conf.edgeBuffer 
    hand = buffer
    handyeni = True
    newcycle = False
    used = dontUseEdges[:]
    used[(buffer%12)] = used[(buffer%12) + 12] = 1
    if moveEdgeCount == 16 and allowEdgeCycles:
        a = getEdgeNext()
        setUsedEdge(a)
        for _ in range(5):
            a = getEdgeNext()
            setUsedEdge(a)
            b = getEdgeNext()
            setUsedEdge(b)
            unsetUsedEdge(a)
            if used[a%12] == 0 and used[a%12+12] == 0:
                getEdgeNext(a%12 + random.randint(0, 1)*12)
            else:
                getEdgeNext(a)
            setUsedEdge(a)
        return True
    while count < moveEdgeCount:
        if used == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            return False 
        if hand == -1:
            hand = getEdgeNext()
            setUsedEdge(hand)
            handyeni = True
            newcycle = True
        elif handyeni:
            nxt = getEdgeNext()
            setUsedEdge(nxt)
            if allowEdgeCycles:
                unsetUsedEdge(hand)
            handyeni = False
        else:
            nxt = getEdgeNext()
            setUsedEdge(nxt)
            if hand%12 == nxt%12:
                hand = -1
                if nxt%12 == buffer%12:
                    count -= 1
        count += 1
    if newcycle and hand != -1:
        return False
    for i in range(12):
        edge_orientations[i] %= 2
    return True

#* Scrambling Corners
def getCornerNext():
    nxt = random.randint(0, 23)
    while used[nxt]:
        nxt = random.randint(0, 23)
    if nxt%8 == buffer%8:
        return buffer
    global cornerSequence
    cornerSequence += conf.cornerLetters[nxt]
    swap(corners, buffer%8, nxt%8)
    swap(corner_orientations, buffer%8, nxt%8)
    corner_orientations[nxt%8] += nxt//8 + 3 - buffer//8
    corner_orientations[buffer%8] += 3-nxt//8 + buffer//8
    return nxt

def setUsedCorner(nxt):
    # print('set used', nxt)
    global used
    used[nxt%8] = used[nxt%8+8] = used[nxt%8+16] = 1

def unsetUsedCorner(nxt):
    # print('unset used', nxt)
    # print('dontUseCorners:', dontUseCorners)
    global used
    used[nxt%8] = dontUseCorners[nxt%8]
    used[nxt%8+8] = dontUseCorners[nxt%8+8]
    used[nxt%8+16] = dontUseCorners[nxt%8+16]
    # print('unsetted', nxt, ':', used[nxt%8])

def scrambleCorners():
    global buffer
    global used
    count = 0
    used = dontUseCorners[:]
    buffer = conf.cornerBuffer 
    # print('corner buffer: ', buffer)
    hand = buffer
    handyeni = True
    newcycle = False
    used[(buffer%8)] = used[(buffer%8) + 8] = used[(buffer%8) + 16] = 1
    while count < moveCornerCount:
        if used == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            return False
        if hand == -1:
            hand = getCornerNext()
            setUsedCorner(hand)
            handyeni = True
            newcycle = True
        elif handyeni:
            nxt = getCornerNext()
            setUsedCorner(nxt)
            if allowCornerCycles:
                unsetUsedCorner(hand)
            handyeni = False
        else:
            nxt = getCornerNext()
            setUsedCorner(nxt)
            if hand%8 == nxt%8:
                hand = -1
                if nxt%8 == buffer%8:
                    count -= 1
        count += 1
    if newcycle and hand != -1:
        return False
    for i in range(8):
        corner_orientations[i] %= 3
    return True

#* Main Method
def getScramble(p1=moveEdgeCount, p2=allowEdgeCycles, p3=dontUseEdges, p4=edgeTwistCount, 
        p5=moveCornerCount, p6=allowCornerCycles, p7=dontUseCorners, p8=cornerTwistCount):
    global corners, corner_orientations
    global edges, edge_orientations
    global moveEdgeCount, allowEdgeCycles, dontUseEdges, edgeTwistCount
    global moveCornerCount, allowCornerCycles, dontUseCorners, cornerTwistCount
    global edgeSequence, cornerSequence
    moveEdgeCount, allowEdgeCycles, dontUseEdges, edgeTwistCount = p1, p2, p3, p4
    moveCornerCount, allowCornerCycles, dontUseCorners, cornerTwistCount = p5, p6, p7, p8
    dontUseEdges[conf.edgeBuffer%12] = dontUseEdges[conf.edgeBuffer%12+12] = 1-allowEdgeCycles
    dontUseCorners[conf.cornerBuffer%8] = dontUseCorners[conf.cornerBuffer%8+8] = dontUseCorners[conf.cornerBuffer%8+16] = 1-allowCornerCycles
    for i in range(1000):
        corners = [0, 1, 2, 3, 4, 5, 6, 7]
        corner_orientations = [0, 0, 0, 0, 0, 0, 0, 0] 
        cornerSequence = ''
        if not scrambleCorners():
            continue
        break
    else:
        return '', None
    for i in range(10000):
        edges = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edge_orientations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        edgeSequence = ''
        if not scrambleEdges():
            continue
        break
    else:
        return '', None
    
    edgeSequence = edgeSequence[::-1]
    cornerSequence = cornerSequence[::-1]
    # move cycles to the end
    first_not_cycle = len(edgeSequence)-1
    while first_not_cycle > 0:
        if edgeSequence.count(edgeSequence[first_not_cycle]) == 2:
            first_not_cycle += 1
            break
        first_not_cycle -= 1
    if first_not_cycle > 1:
        edgeSequence = edgeSequence[first_not_cycle:] + edgeSequence[:first_not_cycle]

    first_not_cycle = len(cornerSequence)-1
    while first_not_cycle > 0:
        if cornerSequence.count(cornerSequence[first_not_cycle]) == 2:
            first_not_cycle += 1
            break
        first_not_cycle -= 1
    if first_not_cycle > 1:
        cornerSequence = cornerSequence[first_not_cycle:] + cornerSequence[:first_not_cycle]


    for i in range(0, int(len(edgeSequence)*1.5), 3):
        edgeSequence = edgeSequence[:i] + ' ' + edgeSequence[i:]
    for i in range(0, int(len(cornerSequence)*1.5), 3):
        cornerSequence = cornerSequence[:i] + ' ' + cornerSequence[i:]
    cube_str = getCube()
    # print(cube_str)
    try:
        return 'Edges: {}   Corners: {}'.format(edgeSequence, cornerSequence), kociemba.solve(cube_str, 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB')
    except:
        return '', 'An Error Occurred'

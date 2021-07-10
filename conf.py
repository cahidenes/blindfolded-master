edgeBuffer = 0
cornerBuffer = 0
cornerLetters = []

edgeLetters = []

moveEdgeCount = 0
allowEdgeCycles = False
dontUseEdges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
edgeTwistCount = 0

moveCornerCount = 0
allowCornerCycles = False
dontUseCorners = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
cornerTwistCount = 0

file = open('conf.txt')
edgeBuffer, cornerBuffer = [int(x) for x in file.readline().strip().split()]
cornerLetters = [c for c in file.readline().strip()]
edgeLetters = [c for c in file.readline().strip()]

moveEdgeCount = int(file.readline().strip())
allowEdgeCycles = file.readline().strip() == '1'
dontUseEdges = [int(x) for x in file.readline().strip()]
edgeTwistCount = int(file.readline().strip())

moveCornerCount = int(file.readline().strip())
allowCornerCycles = file.readline().strip() == '1'
dontUseCorners = [int(x) for x in file.readline().strip()]
cornerTwistCount = int(file.readline().strip())

file.close()

def saveConf():
    file = open('conf.txt', 'w')
    file.write('{} {}\n'.format(edgeBuffer, cornerBuffer))
    for c in cornerLetters:
        file.write(c)
    file.write('\n')
    for c in edgeLetters:
        file.write(c)
    file.write('\n')
    file.write('{}\n{}\n'.format(moveEdgeCount, int(allowEdgeCycles)))
    for c in dontUseEdges:
        file.write(str(c))
    file.write('\n')
    file.write('{}\n'.format(edgeTwistCount))
    file.write('{}\n{}\n'.format(moveCornerCount, int(allowCornerCycles)))
    for c in dontUseCorners:
        file.write(str(c))
    file.write('\n')
    file.write('{}\n'.format(cornerTwistCount))
    file.close() 
    # print('saved!')
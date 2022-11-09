#This program takes a video of a Mario Kart Wii time trial and returns the frames where shrooms were used.
#Currently, this is a test version that isn't working with actual video.

shroomArray = [3 for i in range(6)] + [2 for i in range(7)] + [1 for i in range(3)] + [0 for i in range(10)]
print(shroomArray)

def binarySearch(leftBound, leftShrooms, rightBound, rightShrooms):
    if leftShrooms == rightShrooms:
        return
    if leftBound == rightBound-1:
        shroomSpots.append(leftBound)
        return

    middle = (leftBound+rightBound)//2
    middleShrooms = shroomArray[middle]
    binarySearch(leftBound, leftShrooms, middle, middleShrooms)
    binarySearch(middle, middleShrooms, rightBound, rightShrooms)

shroomSpots = []
binarySearch(0, shroomArray[0], len(shroomArray)-1, shroomArray[-1])
print(shroomSpots)
#Looks like the algorithm works!
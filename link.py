## A simple Code for finding linkage distance

import math

distType = 'e'
def distance(point1,point2):
    if distType == 'e':
        return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    
    elif distType == 'm':
        return (abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]))


def dists(clustpoints,x,y):
    maxi,mini,av,count = -1,99999999999999,0,0
    for i in clustpoints[x]:
        for j in clustpoints[y]:
            dist = distance(i,j)
            print('        ',i,j,dist)
            maxi = max(maxi,dist)
            mini = min(mini,dist)
            av += dist
            count+=1
    if count!=0:
        av/=count
    return mini,maxi,av

if __name__ == '__main__':
    distType = input('m for manhattan / e for euclidian : ')
    clust = int(input('No.of clusters : '))
    npoints = [int(input('no.of points in '+str(i)+' th cluster : ')) for i in range(clust)]
    clustpoints = []
    for i in range(clust):
        print('Enter points in Cluster',i,'in X Y format')
        clustpoints.append([list(map(int,input().split())) for x in range(npoints[i])])

    i,j = 0,0
    while i < len(clustpoints):
        j = i+1
        while j < len(clustpoints):
            print('s link, c link, av link between',i,'and',j,':',dists(clustpoints,i,j))
            j+=1
        i+=1
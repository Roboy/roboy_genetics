import numpy as np



def trisMinDistance(tris, point):
    #print(tris)
    #print(point)
    #print(np.sqrt((tris[0,0] - point[0])**2 + (tris[0,1] - point[1])**2 + (tris[0,2] - point[2])**2))
    dist1 = np.linalg.norm(np.squeeze(np.asarray(tris[:,0:3])) - np.asarray(point))
    dist2 = np.linalg.norm(np.squeeze(np.asarray(tris[:,3:6])) - np.asarray(point))
    dist3 = np.linalg.norm(np.squeeze(np.asarray(tris[:,6:9])) - np.asarray(point))
    #print("distances %f, %f, %f" % (dist1, dist2, dist3))
    return min(dist1, dist2, dist3)


def trisByMinDistanceSortedMap(trisList, point):
    tris = [(i, trisMinDistance(tris, point)) for (i, tris) in enumerate(trisList)]
    tris.sort(key=lambda el: el[1])
    return tris

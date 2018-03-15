import numpy as np


def get_random_trafomatrix(alpha, beta, gamma, x, y, z):
	
	#Random translation
	#x = np.random.randint(0,100)
	#y = np.random.randint(0,100)
	#z = np.random.randint(0,100)


	#Random rotation
	#alpha = np.random.randint(0,180)
	#beta = np.random.randint(0,180)
	#gamma = np.random.randint(0,180)

	alpha = 90
	beta = 90
	gamma = 90


	#Rotation matrices
	Rx = np.matrix(([1,0,0],[0,np.cos(alpha),np.sin(alpha)],[0,-np.sin(alpha),np.cos(alpha)]))
	Ry = np.matrix(([np.cos(beta),0,-np.sin(beta)],[0,1,0],[np.sin(beta),0,np.cos(beta)]))
	Rz = np.matrix(([np.cos(gamma),np.sin(gamma),0],[-np.sin(gamma),np.cos(gamma),0],[0,0,1]))

	rotationmatrix = Rx.dot(Ry).dot(Rz)

	#Initialize translation vector
	translation = np.matrix(([x],[y],[z],[1]))


	trafomatrix = np.insert(rotationmatrix, 3,axis = 0, values = 0)
	trafomatrix = np.append(trafomatrix, translation, axis = 1)


	return trafomatrix
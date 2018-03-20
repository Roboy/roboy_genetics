import numpy as np
import random


def getRandomTrafomatrix():
	
	#Random translation
	x = np.random.randint(-1,1)
	y = np.random.randint(-1,1)
	z = np.random.randint(-1,1)


	#Random rotation
	alpha = np.random.randint(-180,180)
	beta = np.random.randint(-180,180)
	gamma = np.random.randint(-180,180)


	#Rotation matrices
	Rx = np.matrix(([1,0,0],[0,np.cos(alpha),-np.sin(alpha)],[0,np.sin(alpha),np.cos(alpha)]))
	Ry = np.matrix(([np.cos(beta),0,np.sin(beta)],[0,1,0],[-np.sin(beta),0,np.cos(beta)]))
	Rz = np.matrix(([np.cos(gamma),-np.sin(gamma),0],[np.sin(gamma),np.cos(gamma),0],[0,0,1]))

	rotationmatrix = Rx.dot(Ry).dot(Rz)

	#Initialize translation vector
	translation = np.matrix(([x],[y],[z],[1]))


	trafomatrix = np.insert(rotationmatrix, 3,axis = 0, values = 0)
	trafomatrix = np.append(trafomatrix, translation, axis = 1)


	return trafomatrix


def getRandomRotationmatrix():

	#Random rotation
	alpha = np.pi*random.uniform(-1,1)
	beta = np.pi*random.uniform(-1,1)
	gamma = np.pi*random.uniform(-1,1)


	#Rotation matrices
	Rx = np.matrix(([1,0,0],[0,np.cos(alpha),-np.sin(alpha)],[0,np.sin(alpha),np.cos(alpha)]))
	Ry = np.matrix(([np.cos(beta),0,np.sin(beta)],[0,1,0],[-np.sin(beta),0,np.cos(beta)]))
	Rz = np.matrix(([np.cos(gamma),-np.sin(gamma),0],[np.sin(gamma),np.cos(gamma),0],[0,0,1]))

	rotationmatrix = Rx.dot(Ry).dot(Rz)

	return rotationmatrix
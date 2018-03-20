from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def plot_mesh(path):
	# Create a new plot
	figure = plt.figure()
	axes = mplot3d.Axes3D(figure)

	# Load the STL files and add the vectors to the plot
	your_mesh = mesh.Mesh.from_file(path)
	axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
	
	# Auto scale to the mesh size
	scale = your_mesh.points.flatten(-1)
	axes.auto_scale_xyz(scale, scale, scale)

	# Show the plot to the screen
	plt.show()
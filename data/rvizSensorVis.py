import rospy
import roslib
import numpy as np
from visualization_msgs.msg import Marker, MarkerArray
#Visualization mesh



def sensorVisualization(sensors,rate, sphereSize=0.01, color=(0,0,0,1)):

	#Sensor visualization in RVIZ
	topic = 'visualization_marker'
	publisher = rospy.Publisher(topic, Marker, queue_size=1000)

	for i,sensor in enumerate(sensors):

	    sensor = np.squeeze(np.array(sensor[1]))
	    
	    rate3 = rospy.Rate(rate)
	    while not rospy.is_shutdown():

	        markers = Marker()
	        markers.header.frame_id = 'world'
	        markers.ns = 'ns'
	        markers.type = Marker.SPHERE

	        markers.pose.position.x = sensor[0];
	        markers.pose.position.y = sensor[1];
	        markers.pose.position.z = sensor[2];
	        markers.pose.orientation.x = 0
	        markers.pose.orientation.y = 0
	        markers.pose.orientation.z = 0
	        markers.pose.orientation.w = 0

	        #print(marker.points)
	        markers.color.r = color[0]
	        markers.color.g = color[1]
	        markers.color.b = color[2]
	        markers.color.a = color[3]

	        markers.scale.x = 0.02
	        markers.scale.y = 0.02
	        markers.scale.z = 0.02
	        markers.lifetime = rospy.Duration(-1);
	        markers.header.stamp = rospy.Time.now()
	        markers.action = Marker.ADD
	        markers.id = 100+i

	        #mesh.mesh_resource = "package://common_utilities/stls/testcube_40mm.stl"
	        #mesh.mesh_resource = "package://roboy_models/roboy_2_0_simplified/meshes/CAD/head.stl"

	        publisher.publish(markers);
	        rate3.sleep()
	        break
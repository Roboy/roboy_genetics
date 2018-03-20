import rospy
import roslib
from visualization_msgs.msg import Marker, MarkerArray



def bestSensorVis(sensorDict, bestSensors, rate, color=(1,0,0,1),sphereSize=0.03):

	topic = 'visualization_marker'
	publisher = rospy.Publisher(topic, Marker, queue_size=1000)
	rate3 = rospy.Rate(rate)

	for i, best in enumerate(bestSensors):

	    showSensor = sensorDict[best][1]

	    while not rospy.is_shutdown():

	        markers = Marker()
	        markers.header.frame_id = 'world'
	        markers.ns = 'ns'
	        markers.type = Marker.SPHERE

	        markers.pose.position.x = showSensor[0];
	        markers.pose.position.y = showSensor[1];
	        markers.pose.position.z = showSensor[2];
	        markers.pose.orientation.x = 0
	        markers.pose.orientation.y = 0
	        markers.pose.orientation.z = 0
	        markers.pose.orientation.w = 0

	        #print(marker.points)
	        markers.color.r = color[0]
	        markers.color.g = color[1]
	        markers.color.b = color[2]
	        markers.color.a = color[3]

	        markers.scale.x = sphereSize
	        markers.scale.y = sphereSize
	        markers.scale.z = sphereSize
	        markers.lifetime = rospy.Duration(-1);
	        markers.header.stamp = rospy.Time.now()
	        markers.action = Marker.ADD
	        markers.id = 100+i

	        #mesh.mesh_resource = "package://common_utilities/stls/testcube_40mm.stl"
	        #mesh.mesh_resource = "package://roboy_models/roboy_2_0_simplified/meshes/CAD/head.stl"

	        publisher.publish(markers);
	        rate3.sleep()
	        break
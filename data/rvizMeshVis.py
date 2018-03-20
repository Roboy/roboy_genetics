import rospy
from visualization_msgs.msg import Marker, MarkerArray

def meshVisualization(orientationMesh, stlFile, posMesh=(0,0,0), scale=0.01):
	#Visualization mesh
	topic = 'visualization_marker'
	publisher = rospy.Publisher(topic, Marker, queue_size=10)
	rate2 = rospy.Rate(100)


	while not rospy.is_shutdown():
	    
	    for i in range(5):
	        mesh = Marker()
	        mesh.header.frame_id = 'world';
	        mesh.ns = 'ns';
	        mesh.type = Marker.MESH_RESOURCE
	        mesh.color.r = 1.0
	        mesh.color.g = 1.0
	        mesh.color.b = 1.0
	        mesh.color.a = 0.9
	        mesh.scale.x = scale
	        mesh.scale.y = scale
	        mesh.scale.z = scale
	        mesh.lifetime = rospy.Duration(-1);
	        mesh.header.stamp = rospy.Time.now()
	        mesh.action = Marker.ADD
	        mesh.id = 10000000;
	        mesh.pose.position.x = posMesh[0];
	        mesh.pose.position.y = posMesh[1];
	        mesh.pose.position.z = posMesh[2];
	        mesh.pose.orientation.x = orientationMesh[1];
	        mesh.pose.orientation.y = orientationMesh[2];
	        mesh.pose.orientation.z = orientationMesh[3];
	        mesh.pose.orientation.w = orientationMesh[0];
	        mesh.mesh_resource = ("package://" + stlFile)

	        publisher.publish(mesh);
	        rate2.sleep()
	    break
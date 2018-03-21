import rospy
from visualization_msgs.msg import Marker, MarkerArray

def meshVisualization(orientationMesh, stlFile, posMesh=(0,0,0), scale=0.01, color=(1.0,1.0,1.0,0.9)):
	#Visualization mesh
	topic = 'visualization_marker'
	publisher = rospy.Publisher(topic, Marker, queue_size=10)
	rate2 = rospy.Rate(100)


	while not rospy.is_shutdown():
	    
	    for i in range(7):
	        mesh = Marker()
	        mesh.header.frame_id = 'world';
	        mesh.ns = 'ns';
	        mesh.type = Marker.MESH_RESOURCE
	        mesh.color.r = color[0]
	        mesh.color.g = color[1]
	        mesh.color.b = color[2]
	        mesh.color.a = color[3]
	        mesh.scale.x = scale
	        mesh.scale.y = scale
	        mesh.scale.z = scale
	        mesh.lifetime = rospy.Duration(-1);
	        mesh.header.stamp = rospy.Time.now()
	        mesh.action = Marker.ADD
	        mesh.id = 10;
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
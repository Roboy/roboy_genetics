from geometry_msgs.msg import Point
import numpy as np
import rospy
import roslib
import math
import tf
from visualization_msgs.msg import Marker, MarkerArray


def NormalsVisual(sensors, normals):
    topic = 'visualization_marker'
    publisher = rospy.Publisher(topic, Marker, queue_size=1000)

    for (i, sensor) in enumerate(sensors):

    	sensor = np.squeeze(np.asarray(sensor))
        normal = np.squeeze(np.asarray(normals[i,:]))
        #print(sensor)
        #print(normal)
        origin_arrow = Point()
        origin_arrow.x = sensor[0]
        origin_arrow.y = sensor[1]
        origin_arrow.z = sensor[2]
        arrow_ray = Point()
        arrow_ray.x = (sensor[0]+normal[0])
        arrow_ray.y = (sensor[1]+normal[1])
        arrow_ray.z = (sensor[2]+normal[2])
	    #Visualization mesh
	    
        rate3 = rospy.Rate(100)
        while not rospy.is_shutdown():

	        marker = Marker()
	        marker.header.frame_id = 'world'
	        marker.ns = 'ns'
	        marker.type = Marker.ARROW

	        marker.points.append(origin_arrow)
	        marker.points.append(arrow_ray)
	        
	        #print(marker.points)

	        marker.color.r = 1.0
	        marker.color.g = 0.0
	        marker.color.b = 0.0
	        marker.color.a = 1.0
	        
	            
	        marker.scale.x = 0.001
	        marker.scale.y = 0.5
	        marker.scale.z = 0.5
	        marker.lifetime = rospy.Duration(-1);
	        marker.header.stamp = rospy.Time.now()
	        marker.action = Marker.ADD
	        marker.id = 100000+i;
	        publisher.publish(marker);
	        rate3.sleep()

	        break
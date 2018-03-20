from geometry_msgs.msg import Point
import numpy as np
import rospy
import roslib
import math
import tf
from visualization_msgs.msg import Marker, MarkerArray



# Ray Triangle Intersection for fitness function


#origin is starting point of the line, here: current Lighthouse position
#ray is a vector from Lighthouse to the sensor, should be d = SensorPosition - t * LighthousePosition
    #t is length of ray

def rayIntersectsTriangleVisual(origin, sensor, tri, LH_CSframe,j):

    topic = 'visualization_marker'
    publisher = rospy.Publisher(topic, Marker, queue_size=1000)
       
    ray = sensor - origin
    v0 = tri[0:3]
    v1 = tri[3:6]
    v2 = tri[6:9]
    
    e1 = v1 - v0
    e2 = v2 - v0
    #print('test')
    #print(v0); print(v1); print(v2); print(e1); print(e2) 
    
    h = np.cross(ray, e2)
    
    a = e1.dot(h)
    if(a > -0.00001 and a < 0.00001):
        return False
    
    f = 1/a
    s = origin - v0
    u = f * (s.dot(h))
    
    if (u < 0.0 or u > 1.0):
        return False
    
    q = np.cross(s, e1)
    v = f * (ray.dot(q))
    
    if (v < 0.0 or u+v > 1.0):
        return False
    
    t = f * (e2.dot(q))
    if (t > 0.00001):
        
        origin_arrow = Point()
        origin_arrow.x = origin[0]
        origin_arrow.y = origin[1]
        origin_arrow.z = origin[2]
        arrow_ray = Point()
        arrow_ray.x = (origin+(t*ray))[0]
        arrow_ray.y = (origin+(t*ray))[1]
        arrow_ray.z = (origin+(t*ray))[2]
        #Visualization mesh
        
        rate3 = rospy.Rate(-1)
        while not rospy.is_shutdown():

            marker = Marker()
            marker.header.frame_id = 'world'
            marker.ns = 'ns'
            marker.type = Marker.ARROW

            marker.points.append(origin_arrow)
            marker.points.append(arrow_ray)
            
            #print(marker.points)
            if(LH_CSframe=='lighthouse1'):
                marker.color.r = 1.0
                marker.color.g = 1.0
                marker.color.b = 1.0
                marker.color.a = 1.0
            elif(LH_CSframe=='lighthouse2'):
                marker.color.r = 1.0
                marker.color.g = 0.0
                marker.color.b = 1.0
                marker.color.a = 1.0
                
            marker.scale.x = 0.01
            marker.scale.y = 0.05
            marker.scale.z = 0.05
            marker.lifetime = rospy.Duration(1);
            marker.header.stamp = rospy.Time.now()
            marker.action = Marker.ADD
            marker.id = 1000000+np.random.randint(0,10000000);

            #mesh.mesh_resource = "package://common_utilities/stls/testcube_40mm.stl"
            #mesh.mesh_resource = "package://roboy_models/roboy_2_0_simplified/meshes/CAD/head.stl"

            publisher.publish(marker);
            rate3.sleep()
            break
            
        return t
    else:
        return False

def rayIntersectsTriangle(origin, sensor, tri, LH_CSframe):
       
    ray = sensor - origin
    v0 = tri[0:3]
    v1 = tri[3:6]
    v2 = tri[6:9]
    
    e1 = v1 - v0
    e2 = v2 - v0
    #print('test')
    #print(v0); print(v1); print(v2); print(e1); print(e2) 
    
    h = np.cross(ray, e2)
    
    a = e1.dot(h)
    if(a > -0.00001 and a < 0.00001):
        return False
    
    f = 1/a
    s = origin - v0
    u = f * (s.dot(h))
    
    if (u < 0.0 or u > 1.0):
        return False
    
    q = np.cross(s, e1)
    v = f * (ray.dot(q))
    
    if (v < 0.0 or u+v > 1.0):
        return False
    
    t = f * (e2.dot(q))
    if (t > 0.00001):            
        return t
    else:
        return False
import random

# Find random sensors
def randomSensor(v):
    i = random.randint(0,len(v)-1)
    rand = v[i]
    
    return rand[0]
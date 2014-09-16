#Jamie Hilton
#12/09/14
#Pool Calculator V1.1
length = float(input("Please enter the length of the pool in ft: ")) 

deepend_width = float(input("Please enter the width of the deepest end of the pool in ft: "))

deepend_depth = float(input("Please enter the depth of the deepest end of the pool in ft: "))

shallowend_width = float(input("Please enter the width of the shallowest end of the pool in ft: "))

shallowend_depth = float(input("Please enter the depth of the shallowest end of the pool in ft: "))


average_depth = (deepend_depth+shallowend_depth)/2

average_width = (deepend_width+shallowend_width)/2

volume = average_width*average_depth*length

print("The volume of water required to fill your pool is {0} L".format(volume))

from tdw.controller import Controller

c = Controller(launch_build=False) 
print("Hello world!")
c.communicate({"$type": "terminate"})

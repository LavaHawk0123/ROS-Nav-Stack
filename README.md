## To install and run via docker:

### Pull the docker image:
```
sudo docker pull marsrovermanipal/marsrovermanipal_erc_nav:latest
```
### Run the docker image (setup Nvidia Container Toolkit first):
```
sudo docker run --env-file credentials.env --name mrm_erc --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all marsrovermanipal/marsrovermanipal_erc_nav:latest
```
### On another terminal:
```
sudo docker exec -it mrm_erc bash
```
#### To launch simulation:
```
roslaunch leo_erc_gazebo leo_marsyard.launch
```
#### To launch rviz:
```
roslaunch leo_erc_viz rviz.launch
```
<h2> Elements of the Navigation Stack : </h2>
<h3>Mapping using RTab Map</h3>
<br>

![Map_comp_comp](https://user-images.githubusercontent.com/75236655/182971440-314e3cf0-3adb-4591-ab6c-1b8d9139b01c.gif)

<h3>Path Planning and Obstacle Avoidance</h3>

#### Move Base for path Planning

![Path_Planning](https://user-images.githubusercontent.com/75236655/182969562-12e0fdc2-1962-4525-82b4-2460ae57b635.gif)

#### Rviz Visualization 

![Planner_Move_Base](https://user-images.githubusercontent.com/75236655/182968953-5a2928bd-1676-4d9d-9bf0-8ec24757ea3f.gif)


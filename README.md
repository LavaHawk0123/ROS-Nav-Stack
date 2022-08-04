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

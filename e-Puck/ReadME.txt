## Fracisco de Asís Bermúdez Campuzano ##

## Redis - Server ##
The redis server has been implemented in wsl, (The Windows Subsystem for Linux)
lets developers run a GNU/Linux environment -- including most command-line tools,
utilities, and applications -- directly on Windows, unmodified, without the overhead
of a traditional virtual machine or dualboot setup.

GitHub link -> https://github.com/Franbercam/e-Puck_ISRLAB # The code is accessible from my github (Franbercam)

## Observations
 - The calibration of the sensors could not be carried out correctly due to the meticulous
   sensitivity of the mobile robot (e-Puck)
 - The position and assignment of the ids for each sensor is detailed in the
   diagram in png format. (e-Puck_sensor_scheme.png)
 - The original project began developing on the Robotnik mobile robot, but due to the lack
   of sensors it was discarded.
 - The development and architecture of the project has been carried out following the model seen in class
 - The redis server has been implemented using wsl because Redis is not officially supported on Windows.
 - AI prioritizes turning right due to right hand maze solving method.
   Documentation method -> https://ingenieriabasica.es/como-salir-de-un-laberinto/ # (Spanish info)
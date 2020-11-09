.. Author: Moritz Schubert
.. License: CC-BY


Proximity Management
====================

.. code-block:: python

    #Create proximity manager
    manager = vizproximity.Manager()
    
    #Add main viewpoint as proximity target
    target = vizproximity.Target(viz.MainView)
    manager.addTarget(target)

In our experiment, the spheres reveal their true color when the particpant comes close to them.
In order for that to work, we need a way for the spheres to "know" that the participant is close.
In Vizard this job is done by a proximity manager.

In the first line of this code chunk, we create an instance of the ``Manager`` class from the ``vizproximity`` module.
You might remember the concept of classes and instances from the turtle chapter.
If not, I recommend that you have a look at chapter 5.3 and 5.4 in order to refresh your memory.

Next to managers the two other important classes of the vizproximity module are targets and sensors.
Their roles are quite straightforward: Sensors detect when a certain target enters their range.
In our experiment, each of the spheres is "equipped" with a sensor that registers if the participants' avatar is close to them.
However, it does not check for every part of the avatar's 3D model whether it is inside the sensor, but only for its *main view*.
The participant's view of the virtual world is provided by what in 3D graphics is called a camera; you are seeing your sorroundings through the "eyes" of the camera.
The main view can be thought of as the lens of the camera.

In the last line, we add the target to the manager.
We are saying to the manager "keep track of this target".
If we want a target or a sensor to do something, we need to add it to a manager.
In cases like this one, where we only have one manager, needing to add every single target and/or sensor to it can seem a little tedious.
However, the usefulness of the ``addTarget()`` function becomes more apparent when we think of the case of multiple managers.
For example, we might want to carry out multiple trials of our experiment and vary the distances needed to reveal the true colors from one trial to the next.
This could be implemented by creating a small range, medium range and wide range sensors for each sphere and adding them to one of three managers, respectively.
Depending on the range needed for any given trial, one of managers could be activated.
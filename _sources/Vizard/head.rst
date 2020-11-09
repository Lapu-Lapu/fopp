.. Author: Moritz Schubert
.. License: CC-BY

Getting an Overview of the Code
===============================

A good practice when reading someone else's code is to skip functions and come back to them when they are mentioned in the code.
You can think about it like treating the functions like black boxes and only looking into the boxes when you need to.

So let's turn each of the functions into a black box and then look at the code again:

.. code-block:: python

    import viz
    import viztask
    import vizact
    import vizinfo
    import vizproximity
    import vizshape
    
    viz.fov(60)
    viz.go()
    
    #Set up the environment and proximity sensors
    dojo = viz.addChild('dojo.osgb')

    #Create proximity manager
    manager = vizproximity.Manager()
    
    #Add main viewpoint as proximity target
    target = vizproximity.Target(viz.MainView)
    manager.addTarget(target)
    
    #fade to true color when viewpoint moves near
    def EnterSphere(e, sphere, color):
        ..........
    
    #fade to white when viewpoint moves away
    def ExitSphere(e, sphere):
        ..........
    
    #add spheres and create a proximity sensor around each one
    sphereSensors = []
    
    def AddSphere(name, color, position):
        ..........
    
    AddSphere('red', viz.RED, [0,1.8,4])
    AddSphere('blue', viz.BLUE, [3.5,1.8,2])
    AddSphere('yellow', viz.YELLOW, [3.5,1.8,-2])
    AddSphere('green', viz.GREEN, [0,1.8,-4])
    AddSphere('purple', viz.PURPLE, [-3.5,1.8,-2])
    AddSphere('gray', viz.GRAY, [-3.5,1.8,2])

    #Set debug off. Toggle debug with d key
    manager.setDebug(viz.OFF)
    debugEventHandle = vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)
    
    #Add a sensor in the center of the room for the participant to return to after each trial
    centerSensor = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(0.0,0.0)),None)
    manager.addSensor(centerSensor)
    
    #Add vizinfo panel to display instructions
    info = vizinfo.InfoPanel("Explore the environment\nPress 'd' to toggle the visibility of the sensors\nPress spacebar to begin the experiment")
    
    def participantInfo():
        ..........
    
    def learnPhase():
        ..........
    
    def testPhase():
        ..........
    
    def experiment():
        ..........
    
    viztask.schedule(experiment)

It looks way less scary now, right?

Now we can go through the code chunk by chunk and try to understand what it means. Starting with...

Import Statements
-----------------

.. code-block:: python

    import viz
    import viztask
    import vizact
    import vizinfo
    import vizproximity
    import vizshape

The importing of modules is traditionally done right at the top of the script.
You could also load each modul right before you use for the first time, but this way someone who is reading your script can easily see which modules they need to have installed in order to be able to run your code.

`viz` is the shorthand for the Vizard module.
Vizard is a proprietary and commercial Python module which can be used to program virtual reality scenarios.
"Proprietary" means that the source code is not freely available and may not be changed by anyone other than Worldviz, the publisher of Vizard.
The other five modules can be thought of as addons to `viz`.
You might wonder why they are separate modules and not simply part of `viz`.
One reasone for this might be that this way you are able to load only the modules that you need which could free up valuable resources for running the VR experiment more smoothly.

General Setup
-------------

.. code-block:: python

    viz.fov(60)
    viz.go()

``fov`` is short for "field of view".
``.fov(60)`` sets the field of view to 60 degrees.
Making it wider lets the participant see more of their sorrounding, but it might also look unrealistic and disorienting.

``go()`` simply launches Vizard.

Set Up the Environment
----------------------

.. code-block:: python

    #Set up the environment and proximity sensors
    dojo = viz.addChild('dojo.osgb')

This adds the environment in which the VR secnario takes place in: a 3D model of a dojo.
``osgb`` is a common file format for 3D models.

The function is called ``addChild()``, but "add" to *what* exactly?
The 3D environment of Vizard is organized in a tree structure.
Each 3D object loaded has a *parent*, i.e. another 3D model it is "attached" to, and is in turn the *child* of said parent.
For example, if I have a table in my virtual environment and I want to put something on top of it (e.g. the 3D model of a vase), one of the easiest ways to accomplish this goal is to add the vase as a child of the table.
Assuming the model for the table is saved in the variable ``table``, I can accomplish this with

``vase = viz.addChild('vase.osgb', table)``, where the first argument is the file path to the 3D model of the vase and the second argument is its parent.

You might wonder why ``viz.addChild('dojo.osgb')`` does not have a parent argument.
The reason for this is that we are using the default value of this argument and therefore do not need to specify it.
Said default value is ``viz.WORLD``.
``viz.WORLD`` can be thought of as a gigantic void, the huge nothingness out of which existence sprang.
Its the fabric of our virtual reality, the one thing that is if everything else isn't.
Sorry, I got carried away there a little bit, back on track: You can see ``viz.WORLD``, if you run viz.go() without loading a 3D object (such as ``dojo.osgb``) that is big enough to serve as your environment.
Honetly, it's not much to look at, just a neverending black void.



.. For example, if I have a table in my virtual environment and I want to put something on top of it (e.g. the 3D model of a vase), one of the easiest ways to accomplish this goal is to add the vase as child of the table. Let's say that the model of the vase is 30 cm high and 15 cm in both width and depths. Each model has a center point. For the table this might be the center of its surface and for the vase its center (which would be in inside of the vase). If I add a model as the child to a parent, their two center points are aligned. This means in our example, that if I just execute ``viz.addChild('vase.osgb', table)``, the vase would now be stuck *inside* of the table surface.






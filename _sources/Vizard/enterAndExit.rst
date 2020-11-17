.. Author: Moritz Schubert
.. License: CC-BY

The enter and exit functions
============================

.. code-block:: python

    #fade to true color when viewpoint moves near
    def enterSphere(t, sphere, color):
        sphere.runAction(vizact.fadeTo(color,time=1))
    
    #fade to white when viewpoint moves away
    def exitSphere(t, sphere):
        sphere.runAction(vizact.fadeTo(viz.WHITE,time=1))

Every time a function is called by the ``onEnter`` or ``onExit`` method, Vizard automatically passes the target object that entered/exited the spehre to said function as its first argument.
This means, in our case the function call ``manager.onEnter(sensor, enterSphere, sphere, color)`` actually passes three arguments to the ``enterSphere`` function: First of all the target, and only after that the ``sphere`` and ``color`` object.
The automatic passing of the target object can be really helpful in cases where we want to manipulate the target itself.
However, in this case we only want to manipulate the sensor.
Therefore, we assign the target to the variable ``t`` and forget about it.

As you can see, the ``enterSphere`` function does not do a whole lot: It runs an action on the ``sphere`` object.
Said action is ``vizact.fadeTo``, which changes the color of the 3D object it is called on through a fade animation.
In our case, the color is the one specified in the function call of ``enterSphere`` (in the example above it was ``'red'``).
On top of that we specify that the animation should last one 1 second through the ``time`` keyword argument.

``exitSphere`` works complimentarily to ``enterSphere``, only in this case the sphere *always* fades to white.
This explains why as opposed to the ``onEnter`` method we didn't need to pass a ``color`` argument to the ``onExit`` method.

We can see here that the colors that spheres "reveal" when the participant approaches them in the experiment, are not actually "attached" to the spheres.
In the experiment it looks like the true color of a sphere is hidden under a white mantle and that said mantle is lifted when the participant approaches the sphere.
As you can see here, what is actually happening is that the default color of a sphere, white, is switched to a new color upon entering and then switched back to default upon the exiting of a sphere's sensor.



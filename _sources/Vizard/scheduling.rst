.. Author: Moritz Schubert
.. License: CC-BY

Scheduling
==========

.. code-block:: py

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

First, we create a window with ``vizinfo.InfoPanel`` that displays a note about the debug mode.

Then there are bunch of black box functions until the code ends with the line ``viztask.schedule(experiment)``.
The ``schedule`` function of the ``viztask`` module organizes our experiment.
Its single argument is a function that should be called.
If we call ``schedule`` multiple times, each new function is put into a queue.
Viztask will call one function after the other until it reaches the end of the queue.
However, in this case we only fed the function ``experiment`` into ``schedule``, but before we can take a look at that function, we have to understand the concept of a generator.




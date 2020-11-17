.. Author: Moritz Schubert
.. License: CC-BY


Classses
========

Before we are able to understand the next code chunk, we must take a short excursion to understand what Python classes are.
Often in programming, we want to create the same object multiple times, sometimes with small variations between them.
*Classes* can be thought of as the recipes for these objects, while the objects themselves are called *instances* of the class.

For example, for our experiment we need several spheres that hide their color from the user.
Vizard could have offered this feature to the user through a class called ``vizshape.HiddenSphere``.
This is a mere hypothetical scenario for purposes of illustration.
We will later see how this feature is *actually* implemented in Vizard.
``vizshape`` is the module that contains the ``HiddenSphere`` class.
Note that names for classes like ``HiddenSphere`` are conventionally capitalized.
We could create an instance of the ``HiddenSphere`` class by running ``red_sphere = vizshape.HiddenSphere('red')``.
The argument ``'red'`` specifies the actual color of the sphere that is revealed when the participant approaches it.
If we wanted to created another sphere with green as its hidden color, we would write ``green_sphere = vizshape.HiddenSphere('green')``.

Classes can be thought of as factories that produces instances.
The arguments of the classes are nobs that we can turn to change what the factory produces.

.. You have actually already encountered classes when you used the ``random`` module, but for the ease of use they were hidden from you.
    Every method of ``random`` is actually performed on the ``random.Random`` class.
    Here is an example:
    
    .. activecode:: ac22_1
    
        import random
    
        rng = random.Random(123)
        die_roll = rng.randrange(1,7)
        print(die_roll)
    
    The argument for ``random.Random()`` is a so called *seed*.
    ``random`` does not produce truely random numbers.
    Normal computers are unable to accomplish this feat, because every calculation is the strictly determined by the values of 0s and 1s on its hardware - there is no randomness involved.
    They get around this by performing complicated mathmatical operations starting from a seed number, which produces numbers that from the view of the user are close enough to random (called *pseudorandom*) to be used in most applications.
    This seed number could be, for example, the system's current time, down to the millisecond.
    We can set the seed ourselves and thereby make sure that the pseudorandom number generator always produces the same results.
    
    The code above is equivalent to:
    
    .. activecode:: ac22_2
    
        import random
    
        random.set_seed(123)
        die_roll = rng.randrange(1,7)
        print(die_roll)
    
    Of course, it produces different results, because this is a *random* number generator.
    The ``random.Random`` class produces instances of random number generators.
    We can then ask this random number generator to perform different actions (for example, as we did above produce an integer between 1 and 6).
    
    I would like to show you a (kind of) useful usage of the ``random.Random`` class, but first I have to explain what the
    


.. Author: Benjamin Knopp
.. License: CC-BY


Intermezzo: Generators
======================

You might have noticed, that different collections of items can be
iterated over in a for loop, for example strings and lists:

.. activecode:: ac22_1

    for element in [1, 2, 3]:
        print(element)
    for char in "123":
        print(char)

Most psychological experiments consist of trials, which are iterated
over the course of the experiment:

.. activecode:: ac22_2

    for trial in ["TrialA", "TrialB", "TrialC"]:
        print(trial)

In Python, `generators` are a powerful tool to create flexible iterators without
the need to create every item in the collection (like the strings in the list above).

Here is the code above using the new generator syntax:

.. activecode:: ac22_3

    def experiment():
        yield "TrialA"
        yield "TrialB"
        yield "TrialC"
        
    for trial in experiment():
        print(trial)

Here, ``experiment`` is a generator function, which returns a generator, when invoked (with parethesis, similar as function calls: ``experiment()``).
In each iteration of the for-loop, the generator jumps to the next ``yield`` statement, and returns the value left of the yield expression.

.. Let's extend this example, to get some intuition why generators are useful for scheduling tasks within an experiment:
..
.. .. code-block:: python
..     def experiment():
..         print("Subject is doing Trial A")
..         yield "TrialA is finished"
..         print("Subject is doing Trial B")
..         yield "TrialB is finished"
..         print("Subject is doing Trial C")
..         yield "TrialC is finished"
..         
..     for trial in experiment():
..         print(trial)

Vizard uses generators to schedule tasks, which we can use to structure the
order of events in experiments. This enables much flexibility while still
keeping the for-loop clean [5]_. 

The ``schedule`` function of the ``viztask`` module basically does the same 
thing as our for loop, but with functions instead of strings.

The module also contains "wait functions". These are used instead of
the strings we yielded in our example. Each time the program progresses
to the next yield statement, these wait functions are passed to the scheduler,
which can continuously check if the awaited event has occured. If this
is the case, the scheduler tells the generator to progress to the next yield
statement.

.. [5] There are more reasons why the Vizard developers chose to use generators, but this is not important in order to use them for programming your experiment. Here are some additional resources: https://www.python-course.eu/generators.php ; https://www.cosc.canterbury.ac.nz/greg.ewing/python/tasks/SimpleScheduler.html

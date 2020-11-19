.. Author: Moritz Schubert
.. License: CC-BY


The Main Function
=================

We have finally reached the point at which we can look into the ``experiment`` function, the centerpiece of this script:

.. code-block:: py

    def experiment():

        #Wait for spacebar to begin experiment
        yield viztask.waitKeyDown(' ')
    
        #Proceed through experiment phases
        participant = yield participantInfo()
        yield learnPhase()
        results = yield testPhase()
    
        #Log results to file
        with open(participant.id + '_experiment_data.txt','w') as f:
            #write participant data to file
            data = "Participant ID: {p.id}\nLast Name: {p.lastName}\nFirst Name: {p.firstName}\nGender: {p.gender}\nAge: {p.ageGroup}\n\n".format(p=participant)
            f.write(data)

            #write result of each trial
            for result in results:
                name = result[0]
                time = result[1]
                data = "The {} trial took {:.2f} seconds\n".format(name,time)
                f.write(data)
        
Right at the beginning is one of those wait functions mentioned in the previous section.
It ways for the press of a key on the keyboard, in this case the spacebar (indicated by the string only containing a space, ``' '``).

Once the spacebar has been pressed, the experiment proceeds to the next yield statement.
In this case, it's the function ``participantInfo()``.
``participantInfo()`` generates the windows that we have seen at the beginning of the demo video, in which we entered participant information such as their gender and age.
Said information is returned by the ``participantInfo()`` function and assigned to the variable ``participant``.
Then the program continues with the ``learnPhase`` and finally concludes with the ``testPhase``.
We will have a closer look at each of those functions in just a bit, but first we will try to make sense of the rest of the ``experiment`` function.

While this concludes the part of the experiment that is visible to the participant, the rest of the lines of ``experiment`` are vitally important to the experimenter, because they save the data generated during the experiment to a file.

We open the file with the ``with`` statement we've seen in the video of section 10.1 and assign it to ``f``.
``data`` is a long string on which we use the ``format()`` method.
If you want to learn more about string formatting, take a look at subsection 9.9.1.
The short of it is that string formatting allows us to include empty spaces (indicated by squirly brackets) in our string and specify a variable which value will determine the content of said space.
In this case, all the values are attributes of ``participant`` (which we have shortened to ``p``).
``participant`` contains the user input from the participant info window mentioned above.

After writing the string with all the participant information to ``f``, we record the actual results of the experiment.
``results`` is a list of two item lists.
Therefore, in each step of the ``for`` loop, result takes up the value of the next two item list in result.
The first item of each of these lists is the sphere color asked for in the task instruction (which we assign to the variable ``name``) and the second item, which we assign to the variable ``time``, is the time that it took to approach the correct sphere.
Again, we plug those values into a formatted string and save them to the data file.

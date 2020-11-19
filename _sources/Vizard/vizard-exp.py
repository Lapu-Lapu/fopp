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
def enterSphere(e, sphere, color):
    sphere.runAction(vizact.fadeTo(color,time=1))

#fade to white when viewpoint moves away
def exitSphere(e, sphere):
    sphere.runAction(vizact.fadeTo(viz.WHITE,time=1))

#add spheres and create a proximity sensor around each one
sphereSensors = []
def addHiddenSphere(name, color, position):

    sphere = vizshape.addSphere(radius=0.2)
    sphere.setPosition(position)

    sensor = vizproximity.addBoundingSphereSensor(sphere,scale=5)
    sensor.name = name
    sphereSensors.append(sensor)
    manager.addSensor(sensor)

    manager.onEnter(sensor, enterSphere, sphere, color)
    manager.onExit(sensor, exitSphere, sphere)

addHiddenSphere('red', viz.RED, [0,1.8,4])
addHiddenSphere('blue', viz.BLUE, [3.5,1.8,2])
addHiddenSphere('yellow', viz.YELLOW, [3.5,1.8,-2])
addHiddenSphere('green', viz.GREEN, [0,1.8,-4])
addHiddenSphere('purple', viz.PURPLE, [-3.5,1.8,-2])
addHiddenSphere('gray', viz.GRAY, [-3.5,1.8,2])

# set debug on. Toggle debug with d key
manager.setDebug(True)
debugEventHandle = vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

#Add a sensor in the center of the room for the participant to return to after each trial
centerSensor = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(0.0,0.0)),None)
manager.addSensor(centerSensor)

#Add vizinfo panel to display instructions
info = vizinfo.InfoPanel("Explore the environment\nPress 'd' to toggle the visibility of the sensors\nPress spacebar to begin the experiment")

def participantInfo():

    #Turn off visibility of proximity sensors and disable toggle
    manager.setDebug(False)
    debugEventHandle.setEnabled(False)

    #Hide info panel currently displayed
    info.visible(False)

    #Add an InfoPanel with a title bar
    participantInfo = vizinfo.InfoPanel('',title='Participant Information',align=viz.ALIGN_CENTER, icon=False)

    #Add name and ID fields
    textbox_last = participantInfo.addLabelItem('Last Name',viz.addTextbox())
    textbox_first = participantInfo.addLabelItem('First Name',viz.addTextbox())
    textbox_id = participantInfo.addLabelItem('ID',viz.addTextbox())
    participantInfo.addSeparator(padding=(20,20))

    #Add gender and age fields
    radiobutton_male = participantInfo.addLabelItem('Male',viz.addRadioButton(0))
    radiobutton_female = participantInfo.addLabelItem('Female',viz.addRadioButton(0))
    droplist_age = participantInfo.addLabelItem('Age Group',viz.addDropList())
    ageList = ['20-30','31-40','41-50','51-60','61-70']
    droplist_age.addItems(ageList)
    participantInfo.addSeparator()

    #Add submit button aligned to the right and wait until it's pressed
    submitButton = participantInfo.addItem(viz.addButtonLabel('Submit'),align=viz.ALIGN_RIGHT_CENTER)
    yield viztask.waitButtonUp(submitButton)

    #Collect participant data
    data = viz.Data()
    data.lastName = textbox_last.get()
    data.firstName = textbox_first.get()
    data.id = textbox_id.get()
    data.ageGroup = ageList[droplist_age.getSelection()]

    if radiobutton_male.get() == viz.DOWN:
         data.gender = 'male'
    else:
         data.gender = 'female'

    participantInfo.remove()

    # Return participant data
    viztask.returnValue(data)

def learnPhase():

    #provide instructions for the participant
    info.setText("You'll have 30 seconds to walk around and learn the true color of each sphere")
    info.visible(True)

    #hide instructions after 5 seconds
    yield viztask.waitTime(5)
    info.visible(False)

    #let participant know learning phase has ended
    yield viztask.waitTime(30)
    info.setText("Please return to the center of the room to begin the testing phase")
    info.visible(True)

    #Start testing phase after 5 seconds
    yield viztask.waitTime(5)

def testPhase():

    results = []
    trials = [3,2,0,4,1]

    for i in trials:

        #Check to see if participant is already in room center. If not
        #wait until the centerSensor is activated
        if centerSensor not in manager.getActiveSensors():
            yield vizproximity.waitEnter(centerSensor)

        #Get sensor for this trial
        sensor = sphereSensors[i]

        #Instruct participant where to go
        instruction = 'Walk to the {} sphere'.format(sensor.name)
        info.setText(instruction)

        #store the time at which this trial started
        startTime = viz.tick()

        #The yielded command returns a viz.Data object with information
        #about the proximity event such as the sensor, target involved
        yield vizproximity.waitEnter(sensor)
        info.setText('Please return to the center of the room')

        #calculate the time it took for the subject to find the correct object
        elapsedTime = viz.tick() - startTime

        #save results
        results.append((sensor.name, elapsedTime))

    info.setText('Thank You. You have completed the experiment')

    #return results
    viztask.returnValue(results)


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
                
viztask.schedule(experiment)
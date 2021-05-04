import paho.mqtt.client as mqtt
import uuid
import qwiic_joystick

myJoystick = qwiic_joystick.QwiicJoystick()
if myJoystick.is_connected() == False:
    print("The Qwiic Joystick device isn't connected to the system. Please check your connection", file=sys.stderr)
myJoystick.begin()

play_position = "400 400"
x_position = 400
y_position = 400
topic = 'IDD/Gomoku'
# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')


#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

print(f"Now, you are playing {topic}!")
player_number = input(">> Enter your player ID: ")
while True:
    play_here = 0
    if myJoystick.get_horizontal() == 1023:
        if (x_position + 40) <= 680:
            x_position += 40
    if myJoystick.get_horizontal() == 0:
        if (x_position - 40) >= 120:
            x_position -= 40
    if myJoystick.get_Vertical() == 1023:
        if (y_position + 40) <= 680:
            y_position += 40
    if myJoystick.get_Vertical() == 0:
        if (y_position - 40) >= 120:
            y_position -= 40
    play_position = (x_position, y_position)
    print("Current Position: ", play_position)
    if myJoystick.get_button() == 0:
        play_here = 1
    send_play = play_position + " " + play_here + " " + player_number
    client.publish(topic, send_play)
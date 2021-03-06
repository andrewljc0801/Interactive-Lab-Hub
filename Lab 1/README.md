

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.



For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Set up [your Github "Lab Hub" repository](../../../) by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Spring/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how](https://guides.github.com/features/mastering-markdown/) to post links to your submissions on your readme.md so we can find them easily.

### For lab, you will need:

1. Paper
1. Markers/ Pen
1. Smart Phone--Main required feature is that the phone needs to have a browser and display a webpage.
1. Computer--we will use your computer to host a webpage which also features controls
1. Found objects and materials--you’ll have to costume your phone so that it looks like some other device. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case. Be creative!
1. Scissors

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process.
1. Video sketch of the prototyped interaction.
1. Submit these in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
For this assignment, you are going to 

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

**In the kitchen. Usually, it happens when Andrew open the fridge, check on the food and think about what he is going to eat.**

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

**Andrew is the primary player involved in the interaction. When his family members use the fridge, they can be secondary players. In general, whoever uses this fridge involves in the interaction.**

_Activity:_ What is happening between the actors?

**Andrew stuck the Fridge Reminder on the fridge which uses different colors of light to indicate whether the food in the fridge is fresh or not. When the light is green, it means the food in the fridge is still fresh. When the light is yellow, it tells Andrew to pay attention to the food in the fridge that something needs to be eaten soon. When the light is red, it is an urgent reminder and some food in the fridge must be eaten immediately. As the light goes from green to red, it reminds Andrew how fresh the food is.**

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

**The ultimate goal for Andrew is not wasting the food. As long as the food does not go bad and is eaten, Andrew achieves his goal of not wasting the food.**

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 
**Include a picture of your storyboard here.**

![storyboard](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%201/CS%205424%20lab1%20storyboard.jpeg?raw=true)

Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.
**Summarize feedback you got here.**


**Peer Feedback**
* Usefulness
  * A good idea since many people are bothered by this problem (wasting food due to not eat it on time).
  * The light can have a more complicated setting to point out the specific food that people need to pay attention to.
* User Friendliness
  * It's hard for people with deuteranomaly and protanomaly (red-green color blind) to use.


## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**

* Different food has different guidelines of storing (time of being fresh, storage place, etc). How can this device interact with this issue?
* How does the device work? (Using a sensor to detect the freshness of the food or using a timer.)
* People still need to find out the food in "urgent" by themselves.

  
**Are there new ideas that occur to you or your collaborators that come up from the acting?**

* Besides different colors of the light, the device can use the flashing frequency of the light to indicate how fresh the food is. For instance, if the food needs to be eaten immediately, it can flash quickly.
* The device can have different regions of color to indicate the position of the food.
* The device can turn on the green light indicator only when people approach the fridge and always turn on the red light until people take action.
  

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

**Give us feedback on Tinkerbelle.**

*Feedback*
* Pros
  * It works pretty well in controlling the color and voice. A great tool in general.
* Cons
  * It would be helpful if an instruction is provided on both terminals (smartphone and laptop).
  * The buttons on the client-side should be hidden after the user press the "Tinkerbelle" since the buttons are no longer needed as being a client.


## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**

*Set-up Video:*

https://drive.google.com/file/d/1ivWbRjfowvjkjHJvuQx1eHTee6XSctZg/view?usp=sharing

Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

*Follow-up Video(paper prototype):*

https://drive.google.com/file/d/1oCXDv8Pmf02n8tqZ9T_sy1aELVwLskdE/view?usp=sharing
https://drive.google.com/file/d/1yTTa-2VzCNbcL3iS-bHmkWYN7Flu4KaW/view?usp=sharing

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**

*The device looks exactly the same as showing in the set-up video. Instead, the real device should use magnet in order to adhere on the fridge.*

![magnet](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%201/fridge%20magnet.jpg?raw=true)


**What concerns or opportunitities are influencing the way you've designed the device to look?**
* The convenience and exsiting products played an important role in the design process. The fridge magnet determines how it sticks on the fridge, and the simple light emphasize how easy it can be used.


## Part F. Record

**Take a video of your prototyped interaction.**

*Final Video:*

https://drive.google.com/file/d/1ffCEUi5kNyCPdcr5TPWW3jFun-uJA-sT/view?usp=sharing
https://drive.google.com/file/d/1GETH-EEZ1-95ro7HngnYPIrZf_9Lz1Pa/view?usp=sharing

**Please indicate anyone you collaborated with on this Lab.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

*My wife Quinn helps me to record the video.*

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

**Summarize feedback from your partners here.**

*I received feedback from Jianang Wang(jw2594), Hangyu Lin(hl2357), and Quinn Wu(yw2325):*
* **Video Content:** It's not very clear that what does the device indicate. It's better to have some conversations or explainations.
  * "The goal was to pervent the person from opening the fridge for some condition and waste energy." (Peer's understanding of the video)
* **Design of The Device:** The light only tells the user that there is some food that need to be eaten in the near future. However, it doesn't specifically point out what it is, or how emergency it is.
* It would be nice to have some sound to make the interaction more accessible.

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors, 
3) We will be grading with an emphasis on creativity. 


**Document everything here.**

**According to the feedback of part 1, I decided to add several features and  make some changes:**
* Name and location of the food: Use the text and food images to give the users clear information.
* Sound and vibration: Use the sound and vibration to describe the severity.
* Flashing light: Use the flashing light to attract the users' attention.
* Water level: Use water with light instead of different colors of light to represent how fresh the food is.

**Storyboard:**
This is a continued storyboard which includes the upgrade version of the device, Fridge Reminder.
![storyboard](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%201/IDD%20Lab1%20Part%202%20Continued.jpg?raw=true)



**Paper Prototype: (Design of the Fridge Reminder)**
![PaperPrototype](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%201/IDD%20Lab1%20Part%202%20Paper%20Prototype.jpg?raw=true)



**Final Video Link: (Upgrade Version of the Fridge Reminder)**

https://drive.google.com/file/d/1U4u_S3rWd8-M5qvicGS-GZAeWH4OyMf5/view?usp=sharing



**Feedback:**
Quinn gave me some feedbacks:

* It has been improved a lot in both user-friendliness and functionalities.
* A good design that only when the users approach the fridge, the screen displays the information they need.
* The next improvement might be how to make it easier to set up. For instance, it won't be complicated to enter all the food expiration dates, so it can support multiple types of food.

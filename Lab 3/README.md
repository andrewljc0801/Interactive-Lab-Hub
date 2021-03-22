# You're a wizard, Andrew Liu

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

*Here is a screenshot of the demo:

![Demo](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%203/demo.png?raw=true)

## Optional

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

Here is my idea:

![Sketch](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%203/Sketch_JL.jpg?raw=true)


## Share your idea sketches with Zoom Room mates and get feedback

I got a lot of valuable feedback from Quinn, John, and James. The problems they addressed mainly about the accelerometer sensor using for cutting the music. Idealy, the user can cut the music if they shake the accelerometer sensor. However, it is not stable to use that and easy to cut the music by mistake. Another thing is, it will be better if the color of the twist stick can be changed as the volume being modified. The system should also allow the user to keep enjoying the music until they don't want to.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

Autonomous Music Player:
* It will ask the user's mood of the day and play a song based on the mood/story the user said.
* The users can control the music state (playing, pause, stop) by voice and can control the volume of the music by knobbing the twist sticker.
* The users can keep enjoying the music until they don't want to.
* The users are allowed to say they don't know or they can't describe their mood.


*Here is the final video of the link:*

https://drive.google.com/file/d/1-8q-Tub1XoERjGCEs_h18ZWFPK5TESMw/view?usp=sharing


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

*Due to the pandemic and the limilation of meeting with the people face to face, I can only let Quinn to interact with the device (Autonomous Music Player) since we are living together.*

Answer the following:

### What worked well about the system and what didn't?
The system did a great job in providing the users great songs based on their mood. And it had great functionalities that the user could play/pause/stop the music at any time. It was also great that the users could control the volume and enjoy the music until they don't want to. One thing that didn't work well when Quinn was interatced with it is the songs are limited now and is not suitable for all possible moods. Quinn answered a mood that was out of my expectation, and the song was not quiet suitable in that case. This is a good point actually, and it can be the further developing direction.

### What worked well about the controller and what didn't?
The main controller of my device is the twist sticker, which can control the volume of the music. It works pretty well in controlling the volume of the song. However, Quinn told me that it was not sensitive. In other words, the user needed to knob it for many cycles to increase or decrease the volume, and it is not user-friendly in this case.


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
Like I mentioned before, one important thing is to cover the different situations as many as you can. The users can give a lot of surprising answers that are out of our expectations. When I tested my device, Quinn told an imaginary story that she broke up with her boyfriend. Even though it played a sad song, the lyrics of the song were not suitable. To make the system more autonomous, we must create a environment which can handle almost all sutiations that could happen.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
I believe recording the user's moods and stories will be very useful. It's one of the best ways to solve the problem of creating an environment that handling multiple responses.
Storing the users' settings of the volume would be another useful thing, because it can help us to set a better default value of the volume. 

The color sensor could be used if we ask the users to choose something near them and use the color of it to represent their moods. In this case, the color that is captured can also be a valid input. 



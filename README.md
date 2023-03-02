<h1 align="center">INTELLIGENT NOTICE PANEL WITH ALEXA</h1>

## TABLE OF CONTENTS:

**1. INTRODUCTION**

**2. HARDWARES USED**

**3. SOFTWARES USED**

**4. PROGRAMMING LANGUAGES**

**5. WORKFLOW**

**6. STEPS**

  1. Create an Amazon developer account. 
  
  2. Create the Alexa skill with the desired invocation name and make the necessary intent blocks.
  
  3. Make the raspberry pi ready.
  
  4. Setup ngrok server in the Raspberry pi 
  
  5. Setup the flask server for handling the alexa skills.
  
  6. Circut connection
  
  7. Setup the alexa end point with the 'HTTPS' instead of AWS Lambda ARN
  
  8. Link the created skill with the AMAZON-ECHO-DOT

**7. COMMANDS**

**8. CONCLUSION**


## INTRODUCTION:
Introducing the project, "INTELLIGENT NOTICE PANEL WITH ALEXA". With this state-of-the-art technology, you can effortlessly control your display with the power of your voice. Whether you need to turn the display on or off or change the text to display precisely what you need, this system provides a hands-free solution to all your display needs.The beauty of this project lies in its simplicity. By utilizing the power of Alexa, you can seamlessly integrate your display into your smart home network and easily manage it with just a few simple voice commands. No more fumbling for remotes or struggling with confusing menus - with "Smarter Display using Alexa," you can easily take control of your display.

Whether you're looking to improve your office productivity or want a more streamlined experience at home, this project is the perfect solution. With its intuitive design and user-friendly interface, it's always been challenging to manage your display and ensure you always have the information you need.
So why wait? Experience the convenience and efficiency of "INTELLIGENT NOTICE PANEL WITH ALEXA" today, and take the first step towards a smarter, more connected future.

## **2. HARDWARES USED:**

- [RASPBERRY PI 4 MODEL B](https://www.hackster.io/raspberry-pi/products/raspberry-pi-4-model-b)
- [W5100S-EVB-PICO](https://www.hackster.io/wiznet/products/w5100s-evb-pico1)
- [JUMPER WIRES](https://www.hackster.io/diyables/products/jumper-wires)
- [AMAZON ECHO-DOT](https://www.hackster.io/amazon-alexa/products/echo-dot)
- [LED DOT-MATRIX](https://www.hackster.io/diyables/products/led-matrix-4-in-1-32x8)

## **3. SOFTWARE AND SERVICES USED:**

- [AMAZON ALEXA SKILLS KIT](https://developer.amazon.com/en-US/alexa)
- [FLASK-ASK](https://github.com/johnwheeler/flask-ask)
- [MQTT SERVICE](https://mqtt.org/)
- [NGROK](https://ngrok.com/)
- [AURDINO IDE](https://www.arduino.cc/)

## **4. PROGRAMMING LANGUAGES**
- [C++](https://isocpp.org/)
- [PYTHON](https://www.python.org/)

## **5.STORY**

- User says the invocation name "device" to Alexa to start the project.
- User issues a voice command such as "Alexa ask device, display to turn on" or "Alexa ask device, display to change to this is work time".
- The voice command is sent to the Amazon Skill Set Kit (ASK) where the "display" intent is invoked.
- The intent block in the flask server running on Raspberry Pi receives the message from the ASK and maps it to a variable inside the intent block.
- The intent block then sends the message to the MQTT server, which is hosted on an online server with HOST: 'port:1883 and HOST:'54.87.92.106'.
- The Wiznet board, which is running in the background, is waiting for messages from the MQTT server and is subscribed to the same topic as the Raspberry   Pi.
- The Raspberry Pi publishes the message to a particular topic and the Wiznet board receives the message.
- Based on the message, an action is performed on the dot matrix display and the message is returned back to the Flask server.
- The Flask server sends the message back to the ASK, which then responds back to the end user.
- The display is turned on or off or changed to the required text as per the user's command.

### DIAGRAM:

<p align="center">
  <img src="https://user-images.githubusercontent.com/114398468/221115134-7f208f9d-abfc-477d-9c7d-71a412035f18.png" />
</p>

## **6. STEPS**
1. Create an Amzazon developer account. 
2. Create the Alexa skill with the desired invocation name and make the necessary intent blocks.
3. Make the raspberry pi ready.
4. Setup ngrok server in the Raspberry pi 
5. Setup the flask server for handling the alexa skills.
6. Circut connection
7. Setup the alexa end point with the 'HTTPS' instead of AWS Lambda ARN
8. Link the created skill with the AMAZON-ECHO-DOT

### 1. AMAZON DEVELOPER CONSOLE:

Follow this link for the steps-> [AMAZON DEVELOPER ACCOUNT](https://developer.amazon.com/en-US/docs/alexa/ask-overviews/create-developer-account.html)

### 2. CREATING THE ALEXA SKILLS:

Amazon Skills are voice-activated capabilities that allow Amazon Alexa to perform a wide variety of tasks, from playing music to controlling smart home devices. These skills can be created by anyone, from individual developers to large companies, and can be published on the Amazon Alexa Skills Store for millions of users to access. To create a custom skill, one can use the Alexa Skills Kit, a set of tools and resources provided by Amazon that includes a web-based interface for designing and building custom skills. The process involves defining the skill's invocation name, intents, and sample utterances, as well as coding the skill's back-end logic using either AWS Lambda or a custom web service. Here in our case we will be using custom web service with the help of ngrok. To make the above mentioned steps i have added a json file which includes all the above mentioned attributes. The invocation name given is "chat", which can be changed to any name of your choice. 

Copy paste the [AMAZON_SKILLS.JSON](https://github.com/Stebin-17/INTELLIGENT-NOTICE-PANEL-WITH-ALEXA/blob/main/ALEXA_SKILLS.JSON) file given in the github and paste it to the JSON Editor section given

<p align="center">
  <img src="https://user-images.githubusercontent.com/114398468/220568727-c1e6d4a0-8475-4c85-979f-74f35509146d.png" />
</p>

In this JSON file, the intent name chatGPT is responsible for sending the phrase given by the user through AMAZON-ECHO-DOT. It is given a slot value called {question}, which is of type "AMAZON.SearchQuery." So whatever phrase the user sends through this intent, like "Alexa ask the chat, I want to see," the {question} will take the value as the phrase after the invocation name("chat") and sends it to the flask server. In further steps, this question value is used by chatGPT for mapping the phrase to a required target.

### 3. SETTING UP THE RASPBERRY PI: 

Follow the [link](https://www.tomshardware.com/how-to/set-up-raspberry-pi) for setting up the raspberry pi 4 for the first time. If you have a already setup raspberry pi 4 skip this step.

### 4. SETTING UP ngrok SERVER:

In the raspberry pi open the terminal and type the following commands.
For updating the Raspberry pi use the commands below: 
```
sudo apt-get update
sudo apt-get upgrade
```
Download ngrok for "linux arm" from this [link](https://ngrok.com/download). Unzip the downloaded ngrok file using the command below.
```
unzip path/ngrok.zip  
```

Start an HTTP tunnel in the port 5000 as the same port will be used by the flask server later
```
./ngrok http 5000
```
A new screen wuill be open with the webaddress that is used to mask the https://localhost:5000. Copy that webaddress as it will be used by the Alexa as end point.

### 5.SETTING UP THE FLASK SERVER:

Install Flask-Ask using following command
```
sudo pip install Flask-Ask
```
Make sure the cryptography is installed below the version of 1.9 to check the version of the cryptography currently installed use the command below:
```
sudo pip show cryptography
```
Install the required cryptography version.
```
pip install cryptography==1.9
pip install pyopenssl ndg-httpsclient pyasn1
```

The flask is installed in the Raspberry pi. Now we have to run the flask server, which will receive requests from the Alexa skills through the endpoint given. The ngrok is working on the same system as the flask server, which will help the local host to be publicly visible and accessible. To run the flask server, open the code in the [link](https://github.com/Stebin-17/AIOT-SMARTER-ALEXA-WITH-CHATGPT/blob/main/FLASK_SERVER_ALEXA.py).
 
### 6. CIRCUT CONNECTION
The last hardwares to set up is the W5100S-EVB-PICO board, LED and 8*8 DOT-MATRIX. The circut connection for the same is given below.

<p align="center">
  <img src="https://user-images.githubusercontent.com/114398468/222353452-b3ef3a23-1d50-4466-9748-bdbc23290dc1.jpg"/>
</p>

- Connect the VCC of the dot matrix to pin VBUS
- Connect the GND of the dot matrix to pin GND
- Connect the DIN of the dot matrix to pin GP11
- Connect the CS of the dot matrix to pin GP13
- Connect the CLK of the dot matrix to pin GP10

Make the connection as shown in the figure and copy paste the [code](https://github.com/Stebin-17/INTELLIGENT-NOTICE-PANEL-WITH-ALEXA/blob/main/ALEXA_SUBSCRIPTION_INTELLIGENT_PANEL.ino) into the Aurdino ide. 

### 7. SETUP THE ALEXA ENDPOINT

Make the endpoint of Alexa to the webaddress obtained from ngrok. For SSL certificate type, select 'My development endpoint is sub-domain of domain that has a wildcard certificate from a certificate authority.' Save the Endpoint. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/114398468/220596776-abe33b33-b898-445c-8937-493636b6603a.png" />
</p>

### 8. TEST THE SKILLS AND CONNECT TO ECHO DOT:
Head over to 'test' section of your skill console and start testing your skill. Try saying commands like ```Alexa ask chat to i wanna see```. This should turn on LED light connected to you Raspberry Pi. For attaching the Echo-Dot to  this project refer the steps mentioned in the [link](https://www.theverge.com/2019/11/19/20972973/amazon-echo-alexa-how-to-add-skills-smart-home-games-sounds).

## **7. COMMANDS**

- FOR TURNING ON THE PANEL- ```Alexa ask device, display turn on the panel'```
- FOR TURNING OFF THE PANEL- ```Alexa ask device, display turn off the panel```
- FOR CHANGING THE DISPLAY ON THE PANEL- ```Alexa ask device, display to display {subject}```

## 8. CONCLUSION

In summary, the Intelligent Display Panel with Alexa project has successfully demonstrated the integration of an 8x8 matrix display with Alexa voice control technology to create a user-friendly and interactive display. With the ability to turn on/off the display and change its display patterns using voice commands, this project offers a convenient and accessible way to control the display. This project is a great example of how the combination of different technologies can lead to the development of innovative and intelligent devices that can simplify our daily lives.

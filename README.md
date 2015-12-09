# myRemote
Remote control for all your devices

Officially tested on Linux, Mac and Windows. If you want to test our product send me a private message.
I will give you a temporary API key.
#Documentation
Getting started.
The first thing you have to do if you want to use our programm is register an 
account on our register page: https://myremote.io/panel/reg.php. 
 
If you have an account, you have access to the main website. If you go to the 
dashboard page you will see three things. Commands, Add/remove key and All devices. 
 
All of this is still useless, if you haven't downloaded the Client. With this 
Client you can register your devices. If you don't have the Client yet, click on 'Download', 
and choose the Client for your OS. 
 
Now we can register a device. There are a few steps to do this. First place the client 
folder in a easy place to find. In this example I place it on the desktop. 
 
Next you open your Terminal (Linux or mac) or CMD (In windows), and browse to the 
client file. 
![](https://myremote.io/scr/instruction1.png)

If you are in the folder that contains the client file, type 'python myRemote.py'. 
This will ask you for a key. 
![](https://myremote.io/scr/instruction2.png)
Now you have to go to the website and click on the 'Generate key' button. In the table 
under this button you can see a table with trerein all your devices. Now copy the key you 
just registered, and paste it in the terminal. You have to paste it right behind the tekst that is already there. 
![](https://myremote.io/scr/instruction6.png) 

Now push enter and if there are no errors you get a message in your terminal 
that says 'Registration successfully'. 
![](https://myremote.io/scr/instruction4.png)
When you go back to the dashboard page and you refresh the page you van see your key is 
registered and the device you activated is bound to the key. 
It's possible to test this with the 'Command' area. Here you can see three fields and a button. 
In the first field you have to select the name of the device you want to perform a command on. 
In the second field you have two options: message and Browser action. This says all you have to know, 
message sends a message to your Client, so if you watch in the CMD you will see the message you just sent 
to your device and browser action Gives an action to your browser. So for example if you enter 
the url 'https://myremote.io', your browser will automatically open a new window with myremote.io. 
Another thing that is important to know about the dashboard page is the 'Delete key' button. 
You see a field with 'ID' in it. If you want to delete a key you have to insert this key in the field 
and click on the Remove button. The button will be deleted immediately, so be sure you have deleted the key 
that you wanted to delete. 
 ![](https://myremote.io/scr/instruction8.png)
The table on the page is not too hard. These are all the devices that are bount to your account. 
There are two important columns, Status and Active. The status is exactly what is says. It checks whether 
your devices are online or not. A device cannot be online if it's not activated. So al unregistered keys 
will remain offline. Active checks if the key is bound to a device. If it's a registered device, it will say 
active is 'Yes', otherwise it will say 'No'. If you register a device, make sure you take a key that is not active.  

When you have registered devices and did some commands, you can see all your commands with the devices on tasks. 
You can enter this page in the sidemenu, and on the page is a table where all your commands (tasks) and devices are.
In this way it's easy to see what devices you are using and which tasks or commands are running.

#Disclaimer
To use our product you'll need a key to create an account, if you want a key you can contact me.
We hope our product fits you all!

Sincerely,

The myRemote Team.

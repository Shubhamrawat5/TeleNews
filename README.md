# Tele-News !
## To Create Your Own Telegram Tech-News Posting Bot
<img src = "https://user-images.githubusercontent.com/34619485/88335884-a7d4af00-cd51-11ea-8021-75e10a2a53f5.jpg" width="400"/>

<hr>

### Screenshot in termux app

<img src = "https://user-images.githubusercontent.com/34619485/88334741-d94c7b00-cd4f-11ea-8513-cd7f8beacf71.png" width="250"/>

### Instructions For Termux

1) Install Termux from play store

2) Install python on termux
```
$ pkg install python
```

3) Install git on termux
```
$ pkg install git
```

4) Give storage permission to termux
```
$ termux-setup-storage
```

5) Copy the github repository
```
$ git clone https://github.com/Shubhamrawat5/TeleNews.git
```

6) Open the TeleNews folder created on your phone
```
$ cd TeleNews
```

7. Upgrade
```
$ pkg upgrade
```

8. Install required libraries
``` 
$ pip install -r requirements.txt
```

<hr>

Now the main 2 steps!

`1) Get a bot token`

You would need to create a telegram bot now by [BotFather](https://telegram.me/BotFather)

Send /newbot message to BotFather telegram bot and create a bot then it would give you a bot token api, copy this token

Token looks like : XXXXXXXX:YYYYYYY-YYYYYYYYYYYYYYYYY_YY

`2) Get chat id or chat tag`

Now there are two different places to send news!

Do only one from 2.1 or 2.2 (any one, read heading of both)

`2.1) You want to send Tech News to a group or channel`

Create a channel/group (if you don't have) then add your bot to your group, to add your bot , you would need the username of bot that you gave to BotFather

Now create a link of your group by making group public then It'll ask to write a group unique link and then copy this group link and remove t.me/ and add @

Eg: Group link t.me/pvxtechnews tag is @pvxtechnews

[Note: You can use group id also, if you group/channel is private]

Now move to 9th step!

`2.2) You want to send Tech News to your telegram account`

Send a message to [Get your telegram id](http://t.me/get_user_id_bot)

Save your telegram id

[Important Note: You need to send a message to your bot because Bot can't start a conversation first so you would need to send a message to your bot (This is a restrictions by telegram to avoid spams by bots)]

<hr>

9) Now you have token and your_id or group_tag , Execute Data file
```
$ python Data.py
```
Now enter 1 and then enter token then enter your_id or group_tag or group_id

Now after saving send 0 to exit from the file

10) Finally last step to post some awesome tech news!!!
```
python Technews.py
```

Now it'll ask you to choose a source then ask for confirmation then send :)

[Note: if you've followed all the instructions correctly then tech news will surely be posted! Otherwise check after 8th step and read everything carefully]


`Now whenever you want to post tech news direct do 10th step only!`

`If you want to change bot or group then do 9th step`

<hr>

## Issues

If you face any issue, feel free to contact on telegram -> [Krypton](https://t.me/KryptonPVX)

Join My PVX Telegram TechNews group -> [TechNews](https://t.me/pvxtechnews)

Join the PVX chat group -> [PVX](https://t.me/PVX_Community)


~~ End ~~

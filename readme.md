# Poketext

Deploy your own Pokedex for Pokemon through SMS and MMS, powered by Twilio


## Setup

You can deploy this application to Heroku in seconds:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/phalt/poktext)

Then in your (Heroku app settings)[https://dashboard-next.heroku.com/apps] you need to add your Twilio Account SID and Twilio Auth Token as Config Vars:

![config_vars](http://i.imgur.com/BusCFML.png)

You can discover your Twilio Account SID and Twilio Auth Token in your [Twilio user account](https://www.twilio.com/user/account)

The application should be setup and running, all you need to do now is setup a [Twilio phone number]() and point the Messaging URL to your Heroku application:

![messaging_url](http://i.imgur.com/xBfPHbn.png)

Be sure to set the URL to

```
https://MY-HEROKU-APP.herokuapp.com/incoming/messsage
```

and replace MY-HEROKU-APP with the name of your heroku application.

Finally, send your Twilio number an SMS with the name of a Pokémon and voila! your own MMS Pokedex:

![mms_charizard](http://i.imgur.com/p4t0EHU.png)

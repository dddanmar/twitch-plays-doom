# Twitch Plays Doom

twitch-plays-doom is a Python Twitch IRC bot for making RESTful calls to a copy of  [restful-doom](https://github.com/jeff-1amstudios/restful-doom).

Stream is now down for the moment. Twitch played for 4 days and made it to E01M04. There were struggles, factions, walls, god mode toggles and a giant 6 second lag that got in everyone's way but it was fantastic all the way through. 

![twitch plays doom](./twitch-plays-doom.png?raw=true)


  - Doom is streamed via OBS to twitch.tv
  - Python subscribes to the twitch IRC channel and listens for single character commands
  - HTTP REST request is sent to restful-doom to update Doom world.
  - ????
  - Doomguy dies.
  - 8-10s lag makes this almost impossible

# Commands
 - "l" - left
 - "r" - right
 - "f" - forward
 - "b" - backward
 - "s" - shoot
 - "d" - toggle door/activate switch/restart after death/spacebar
 - "1" "2" "3" "4" "5" "6" - change weapon

## Thanks!
[restful-doom](https://github.com/jeff-1amstudios/restful-doom) Jeff & Richard  

[chocolate-doom](https://github.com/chocolate-doom/chocolate-doom) team  

[cJSON](https://github.com/DaveGamble/cJSON) - JSON parsing / generation  

[yuarel](https://github.com/jacketizer/libyuarel/) - URL parsing  

## Bonus

![twitch plays doom](./Hand.png?raw=true)


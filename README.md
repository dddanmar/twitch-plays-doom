# Twitch Plays Doom

twitch-plays-doom is a Python Twitch IRC bot for making RESTful calls to a copy of  [restful-doom](https://github.com/jeff-1amstudios/restful-doom).

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


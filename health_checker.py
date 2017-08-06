import requests
import json
from rdoom import rDoomAPI
import time

rd_port = 6666
rd_host = "http://localhost"

rda =  rDoomAPI(rd_host, rd_port)
while True:
    
    if rda.getplayerheath() < 0:
        rda.restartmap()
    time.sleep(1)

import requests
import json


class rDoomAPI(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.actions_url = "/api/player/actions"
        self.objects_url = "/api/world/objects"
        self.doors_url = "/api/world/doors"
        self.world_url = "/api/world"
        self.player_url = "/api/player"

        self.object_distance = 200

    def shoot(self):
        result = requests.post("%s:%s%s" % (self.host, self.port, self.actions_url), data = json.dumps({"type":"shoot"})).status_code
        if result == 201:
            return True
        else:
            return False
    def getplayerheath(self):
        result = requests.get("%s:%s%s" % (self.host, self.port, self.player_url), data = json.dumps({"type":"shoot"})).json()['health']
        return result
    def restartmap(self):
        result = requests.patch("%s:%s%s" % (self.host, self.port, self.world_url), data = json.dumps({"map":1, "episode":1})).json()
        return result

    def forward(self):
        result = requests.post("%s:%s%s" % (self.host, self.port, self.actions_url), data = json.dumps({"type":"forward"})).status_code
        if result == 201:
            return True
        else:
            return False

    def backward(self):
        result = requests.post("%s:%s%s" % (self.host, self.port, self.actions_url), data = json.dumps({"type":"backward"})).status_code
        if result == 201:
            return True
        else:
            return False

    def left(self):
        result = requests.post("%s:%s%s" % (self.host, self.port, self.actions_url), data = json.dumps({"type":"turn-left"})).status_code
        if result == 201:
            return True
        else:
            return False

    def right(self):
        result = requests.post("%s:%s%s" % (self.host, self.port, self.actions_url), data = json.dumps({"type":"turn-right"})).status_code
        if result == 201:
            return True
        else:
            return False

    def getdoor(self):
        result = requests.get("%s:%s%s" % (self.host, self.port, self.doors_url))
        print(result.text)
        result_code = result.status_code
        for door in result.json():
            if door['distance'] < 100:
                #print(door['id'])
                return door['id']
        if result_code == 200:
            return False
        else:
            return False

    def getdoors(self):
        result = requests.get("%s:%s%s" % (self.host, self.port, self.doors_url))
        print(result.text)
        result_code = result.status_code
        for door in result.json():
                print(door['id'])
                #return door['id']
        if result_code == 200:
            return False
        else:
            return False


    def getobjects(self):
        result = requests.get("%s:%s%s?distance=300" % (self.host, self.port, self.objects_url))
        result_code = result.status_code
        for object in result.json():
            print(object['type'])
            print(object['distance'])

            #if door['distance'] < 100:
                #print(door['id'])
            #    return door['id']
        if result_code == 200:
            return False
        else:
            return False


    def toggledoor(self, door_id=False):
        if not door_id:
            door_id = self.getdoor()
        state = requests.get("%s:%s%s/%s" % (self.host, self.port, self.doors_url, door_id)).json()
        print(state)
        try:
            if state['state'] == "closed":
                result = requests.patch("%s:%s%s/%s" % (self.host, self.port, self.doors_url, door_id),\
                    data = json.dumps({"state":"open"})).status_code
            else:
                result = requests.patch("%s:%s%s/%s" % (self.host, self.port, self.doors_url, door_id),\
                    data = json.dumps({"state":"closed"})).status_code
        except:
            return False
        if result == 201:
            return True
        else:
            return False

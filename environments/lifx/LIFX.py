import requests
from kivy.network.urlrequest import UrlRequest
import urllib
import certifi

class LIFX(object):

    
    def __init__(self):
        self.token = ""
        self.brightness = 1
        print(self.token)
        self.mexicana = '23939764-32c3-47ff-981d-ae0e9818b9b6'
        self.mango = 'a0db0ba0-614f-4b2f-a21e-7abd3ad5d931'
        self.pisces = 'ce23a2e2-0792-4860-8d67-b55859b3cb2c'
        self.focus = 'a0d027f4-5b71-46ed-bc31-32f093bd5d6f'
        self.hygge = '6a634783-704e-42c9-98e4-3f74bdd8226f'
        self.blue_haus = '1e07fd97-6261-474e-b996-9599cff686ac'
        self.lady_prep = 'dd97f9e7-a34b-4f69-976e-7ac9ea680c72'
        self.vday_vibes = 'c8e44a6a-c7e0-4bce-becf-f54a972a532c'
        self.habesha_nation = 'e4aac2bc-bf83-4ca1-b1c4-791758c5ba91'
    
    def auth(self):
        token = self.token
        headers = {
            "Authorization": "Bearer %s" % token,
        }
        # response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)
        # print(response.json())
        url = 'https://api.lifx.com/v1/lights/all'
        req = UrlRequest(url, req_body=True, req_headers = headers)
        print(req)

    def get_status(self):
        token = self.token
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)
        print(response.json())
    
    def effects_off(self):
        token = self.token
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        data = {
            "power_off": True
        }

        response = requests.post('https://api.lifx.com/v1/lights/all/effects/off', 
                                 data=data, headers=headers)
        print(response.json())
    
    def pulse(self, period=2, cycles=5, color="green"):
        token = self.token
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        data = {
            "period": {period},
            "cycles": {cycles},
            "color": {color},
        }

        response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse', 
                                 data=data, headers=headers)
        print(response.json())

    
    def power_off(self):
        token = self.token
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        payload = {
            "power": "off",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', 
                                data=payload, headers=headers)
        print(response.json())

        # url = 'https://api.lifx.com/v1/lights/all/state'
        # req = UrlRequest(url, req_body=payload, req_headers = headers, method='POST')
        # print(req)  

    def power_on(self):
        token = self.token
        headers = {"Authorization": "Bearer %s" % token,
        "Content-Type": "application/json"}

        payload = {"power": "on"}
        print(str(payload), str(headers))
        response = requests.put('https://api.lifx.com/v1/lights/all/state', 
                                data=payload, headers=headers)
        print(response.json())

        # url = 'https://api.lifx.com/v1/lights/all/state'
        # req = UrlRequest(url,req_body=str(payload), req_headers = str(headers), 
        # method="POST", ca_file=certifi.where())
        # # req.wait(delay=7)
        # print(req.result)  

        

    def preset(self):
        token = self.token
        presets= {"mexicana": self.mexicana,
                  "mango": self.mango,
                  "pisces": self.pisces,
                  "focus": self.focus,
                  "hygge": self.hygge,
                  "blue_haus": self.blue_haus,
                  "lady_prep": self.lady_prep,
                  "vday_vibes": self.vday_vibes,
                  "habesha_nation": self.habesha_nation
        }
        # s = input("""
        # Pick preset theme:\n 'mexicana'\n 'mango'\n
        # 'pisces'\n 'focus'\n 'hygge'\n 'blue_haus'\n
        # 'lady_prep'\n 'vday_vibes'\n 'habesha_nation' 
        # """)
        
        # b = input("Enter level of brightness 0 to 1 ")
        # scene = presets[s]
        # brightness = b

        headers = {
            "Authorization": "Bearer %s" % token,
        }

        # payload = {
        #     "brightness": brightness,
        # }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        # response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        print(response.json())

    def brightness(self, brightness):
        token = self.token
        brightness = brightness
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        payload = {
            "brightness": brightness,
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
        print(response.json())

    def mex(self):
        token = self.token
        mx= self.mexicana
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % mx, headers=headers)
        print(response.json())

    def mang(self):
        token = self.token
        scene= self.mango
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())

    def pisc(self):
        token = self.token
        scene= self.pisces
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())

    def pis(self):
        token = self.token
        scene= self.pisces
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())

    def hyg(self):
        token = self.token
        scene= self.hygge
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())

    def blu(self):
        token = self.token
        scene= self.blue_haus
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())

    def lad(self):
        token = self.token
        scene= self.lady_prep
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())

    def vda(self):
        token = self.token
        scene= self.vday_vibes
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())

    def hab(self):
        token = self.token
        scene= self.habesha_nation
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
        print(response.json())
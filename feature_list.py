display=["display", "screen","notch","resolution"]
camera=["camera", "picture", "video", "recording", "selfie", "potrait","rear" ,"flash", "megapixel", "front" ]
music=["music", "song", "speaker", "sound"]
battery=["battery", "charge", "power","lithium-ion","standbytime"]
money=["money","budget"] 
phone=["phone", "device", "model"]
design=["design", "look"]
color=["color"] 
ram=["ram"]
glass=["glass" "temper"]
os=["os","android" ,"nougat", "oxygen", "operating system"]
processor=["processor", "cpu", "snapdragon","hardware"]
heat=["heat","warm"] 
game=["game", "gpu"]
sensor=["sensor", "navigation", "finegerprint","face-reconigation","voice-reconigation","voice-reconigation","compass","magnetometer","proximity","accelerometer", "ambient", "gyroscope" "barometer" ,"temperature"]
network=["network","connectivity","4g","lte","volte","wifi","hotspot","usb","jack","gps","bluetooth","signal","location","standards","b/g", "nfc", "infrared", "sim", "fmgsm", "cdma", "gsm", "3g", "4g", "bands"] 
charger=["charger", "c-type", "dash", "usb", "turbo"]
hardisk=["harddisk", "memory", "storage","rom","internal", "expandable", "microsd", "gb", "tb", "mb"]
launche["launcher"]
warranty=["warranty", "guarantee"]
assisstant=["assisstant", "siri", "google"] 
notification=["notification", "alert", "gesture"]
dict={("display":0),("camera":0),("music":0),("battery":0),("notification":0),("warranty":0),("harddisk":0),("charger":0),("network":0),("sensor":0),("game":0),("heat":0),("processor":0),("os":0),("glass":0),("ram":0),("color":0),("design":0),("phone":0),("money":0)}
for token in tokens:
   for token in display:
        dict["display"]+=1;
        break;
   for token in camera:
        dict["camera"]+=1;
        break;
   for token in music:
        dict["music"]+=1;
        break;
   for token in battery:
        dict["battery"]+=1;
        break;
   for token in notification:
        dict["notification"]+=1;
        break;
   for token in warranty:
        dict["warranty"]+=1;
        break;
   for token in harddisk:
        dict["harddisk"]+=1;
        break;
   for token in charger:
        dict["charger"]+=1;
        break;
   for token in network:
        dict["network"]+=1;
        break;
   for token in sensor:
        dict["sensor"]+=1;
        break;
   for token in game:
        dict["game"]+=1;
        break;
   for token in heat:
        dict["heat"]+=1;
   for token in processor:
        dict["processor"]+=1;
        break;
   for token in os:
        dict["os"]+=1;
        break;
   for token in glass:
        dict["glass"]+=1;
	break;
   for token in ram:
	dict["ram"]+=1;
	break;
   for token in color:
	dict["color"]+=1;
	break;
   for token in design:
	dict["design"]+=1;
	break;
   for token in phone:
	dict["phone"]+=1;
	break;
   for token in money:
        dict["money"]+=1;
        break;

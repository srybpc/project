
import cv2
import imutils
from imutils.video import VideoStream
from paho.mqtt import client as mqtt_client
import random
rtsp_url = "http://172.20.10.7:36412/videostream.cgi?user=admin&pwd=12345678"
video_stream = VideoStream(rtsp_url).start()


broker = "172.20.10.2"
port = 1883
topic = "mynew/test"
randomInt = random.randint(0, 0xffff)
client_id = "ESP32Client-"+str(hex(randomInt)[2:])
username = "mymqtt"
password = "myraspi"
receiveVal = ""
i=0
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global receiveVal
        receiveVal = msg.payload.decode()[6]
        print(f"Received `{receiveVal}` from `{msg.topic}` topic")
        if receiveVal == "1":
            global i
            i = i + 1
            cv2.imwrite("Pictures/"+str(i)+".png", frame)

    client.subscribe(topic)
    client.on_message = on_message


client = connect_mqtt()
subscribe(client)

while True:
    frame = video_stream.read()
    if frame is None:
        continue
    client.loop_start()
    frame = imutils.resize(frame,width=1200)
    client.loop_stop()
    cv2.imshow('IPCam', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ('q'):
        break
    
cv2.destroyAllWindows()
video_stream.stop()



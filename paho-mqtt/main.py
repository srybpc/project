from paho.mqtt import client as mqtt_client

import random

broker = "172.20.10.2"
port = 1883
topic = "mynew/test"
randomInt = random.randint(0, 0xffff)
client_id = "ESP32Client-"+str(hex(randomInt)[2:])
username = "mymqtt"
password = "myraspi"
receiveVal = ""

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
        fromWhere = msg.payload.decode()[13:27]
        print(f"Received `{receiveVal}` from `{msg.topic}` topic and from `{fromWhere}`")
       
      
        if(receiveVal == "1"):
            print("Success")
            message =f"Received `{receiveVal}` from `{msg.topic}` topic and from `{fromWhere}`"
            client.publish(topic, message)
            
        else:
            print("Failed")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # rc is the result code.
    print(f"Connect with Result Code: {rc}")
    
def on_message(client, userdata, message):
    print(f"Received Message: {message.payload}")
    print(f"Message Topic: {message.topic}")
    print(f"QoS: {message.qos}")

def on_disconnect(client, userdata, rc):
    print("Client got disconnected")

brokerURL = "broker.hivemq.com"
brokerPort = 1883

mqttClient = mqtt.Client()

mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.on_disconnect = on_disconnect

mqttClient.connect(brokerURL, brokerPort)
# Used to get what everyone publishes
# mqttClient.subscribe("HTW_IoTM2425/#", qos=0)
# If you want to check for a specified folder for all people then add "+"
# mqttClient.subscribe("HTW_IoTM2425/+/temp", qos=0)
# In the above example we can see all the temp published by all the people
mqttClient.subscribe("HTW_IoTM2425/Rohan/test", qos=0)

# Used to start the loop
mqttClient.loop_start()

# Used to publish to broker
mqttClient.publish("HTW_IoTM2425/Rohan/test", payload="Hello it is Rohan", qos=0, retain=False)

# Disconnects the subscribing
mqttClient.disconnect()
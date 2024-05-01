import numpy as np
import paho.mqtt.client as mqtt
import time

broker = "broker.emqx.io"
port = 1883
topic = "/coding/sim"


# A function for processing the received MQTT message
def on_message(client, userdata, msg):
    try:
        print("Receiving data")
        data = msg.payload.decode('utf-8').split('#')
        return [float(d) for d in data]
    except Exception as e:
        print(f"Error parsing MQTT message: {e}")
        return None


# A function for saving data to NumPy arrays
def save_to_numpy(data_list):
    t_data, x_data, y_data, vx_data, vy_data = zip(*data_list)
    return np.array(t_data), np.array(x_data), np.array(y_data), np.array(vx_data), np.array(vy_data)


# A function for subscribing to the MQTT topic and receiving data
def mqtt_sub(broker, port, topic):
    client = mqtt.Client()
    client.connect(broker, port, 10)
    client.on_message = on_message
    client.subscribe(topic, qos=2)
    client.loop_start()
    return client


def main():
    data_list = []

    try:
        client = mqtt_sub(broker, port, topic)
        while True:
            # Waiting for data to be received
            time.sleep(1)
            # Getting data and adding it to the list
            data = on_message(None, None, client)
            if data:
                data_list.append(data)
    except KeyboardInterrupt:
        print("Program interrupted by user")
    finally:
        # Saving data to NumPy arrays at program termination
        if data_list:
            t_array, x_array, y_array, vx_array, vy_array = save_to_numpy(
                data_list)
            print("Data saved to numpy arrays")


if __name__ == '__main__':
    main()

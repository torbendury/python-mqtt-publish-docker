#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqtt


def main():
    parser = argparse.ArgumentParser(
        description="A simple MQTT publishing client written with paho-mqtt.")
    parser.add_argument("--client-name", dest="client_name", type=str,
                        help="Client name to use when connecting to MQTT broker.")
    parser.add_argument("--broker-endpoint", dest="hostname",
                        help="The MQTT broker's hostname to connect to.")
    parser.add_argument("--port", dest="port",
                        help="The MQTT broker port to connect to.")
    parser.add_argument("--topic", dest="topic",
                        help="The MQTT topic to publish to.")
    parser.add_argument("--message", dest="message",
                        help="The message to publish.")
    args = vars(parser.parse_args())

    client = mqtt.Client(client_id=args['client_name'], clean_session=False)
    client.connect(host=args['hostname'], port=int(args['port']), keepalive=60)
    msg_info = client.publish(topic=args['topic'], payload=args['message'])
    if msg_info.is_published():
        print("Message {0} published on {1}".format(
            args['message'], args['topic']))
        exit(0)
    else:
        print("Error sending message.")
        exit(1)


if __name__ == '__main__':
    main()

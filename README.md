# RemoteSwitchBricklet_MQTT

Tinkerforge Remote Switch Bricklet MQTT client for the control of 433Mhz outlets.

Open:
* Add transport level encryption and user authentication

## General Idea

* A physical Remote Switch Bricklet is connected to a machine.
* The machine hosts an MQTT client (MQTTClient) and a Remote Switch Bricklet controller (RSBController).
* The MQTTClient instructs the RSBController to send certain signals that aim to switch outlets.
* Only switches outlets with [type B](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Remote_Switch.html#remote-switch-bricklet).
* Should work well with [homebridge-mqttthing](https://github.com/arachnetech/homebridge-mqttthing).
* This software should not need knowledge about the to be switched outlets, all related information is send via MQTT.

## Installation/Setup

TODO

## MQTT

### MQTT Client Subscriptions

The client subscribes to `rsb/in/*`. It expects topics to be in this format: `rsb/in/<address>/<unit>`.

E.g., to switch the outlet with the address 10, unit 1 to on, a controlling client would have to publish `rsb/in/10/1` with the payload `1`.

### MQTT Client Publications

The client publishes to `rsb/out/*`. Every time the client receives anything on this topic, it publishes to the same topic the new state as a confirmation.

E.g., after it switched the before specified socket to on, the client publishes `rsb/out/10/1` with the payload `1`.

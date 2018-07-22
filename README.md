# RemoteSwitchBricklet_MQTT

Tinkerforge Remote Switch Bricklet MQTT client for the control of 433Mhz outlets.

Open TODO:
- Add transport level encryption and user authentication

## General Idea

- A physical Remote Switch Bricklet is connected to a machine.
- The machine hosts an MQTT Processor (MQTTProcessor) and a Remote Switch Bricklet controller (RSBController).
- The MQTTProcessor instructs the RSBController to send certain signals that aim to switch outlets.
- Only switches outlets with [type B](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Remote_Switch.html#remote-switch-bricklet).
- Should work well with [homebridge-mqttthing](https://github.com/arachnetech/homebridge-mqttthing).
- This software should not need knowledge about the to be switched outlets, all related information is send via MQTT.

## Installation/Setup

Install package:
```
git clone https://github.com/MoeweX/RemoteSwitchBricklet_MQTT.git
cd RemoteSwitchBricklet_MQTT
python setup.py install --user
```

Install Tinkerforge brickD. On Debian (also Ubuntu):
```
sudo apt-get -y install libusb-1.0-0 libudev1 pm-utils
wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb
sudo dpkg -i brickd_linux_latest_amd64.deb
rm brickd_linux_latest_amd64.deb
```

Run with `python tinkerforge_remote_switch/main.py`

## MQTT

The below described topics can be changed in the configuration file.

### MQTT Client Subscriptions

The client subscribes to `rsb/in/#`. It expects topics to be in this format: `rsb/in/<address>/<unit>`.

E.g., to switch the outlet with the address 10, unit 1 to on, a controlling client would have to publish `rsb/in/10/1` with the payload `1`.

### MQTT Client Publications

The client publishes to `rsb/out/#`. Every time the client receives anything for one if its subscriptions, it publishes to the  topic with the same suffix the new state as a confirmation.

E.g., after it switched the before specified socket to on, the client publishes `rsb/out/10/1` with the payload `1`.

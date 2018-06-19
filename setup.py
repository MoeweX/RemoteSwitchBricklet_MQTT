from setuptools import setup

setup(
    name="TinkerforgeRemoteSwitch",
    version="0.0.1",
    python_requires='>3.6.0',
    packages=["tinkerforge_remote_switch"],
    url="TBD",
    license="MIT",
    author="Jonathan Hasenburg",
    author_email="",
    description="An MQTT connected Tinkerforge Remote Switch for 433Mhz sockets.",
    install_requires=[
        "tinkerforge",
        "paho-mqtt"
    ]
)

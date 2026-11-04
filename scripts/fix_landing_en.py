"""Correcciones manuales sobre src/data/landing-domotica.en.ts (salida de translate_landing.py)."""
import os
import re
import sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "data", "landing-domotica.en.ts")
s = open(P, encoding="utf8").read()

PAIRS = [
    ('"[[REVIEW]] According to the official documentation of Amazon, some Echo and eero devices include integrated smart home hubs that connect Zigbee devices such as switches, outlets, lights, and locks."',
     '"According to Amazon\'s official documentation, some Echo and eero devices include built-in smart home hubs that connect Zigbee devices such as switches, outlets, lights and locks [1]."'),
    ('"[[REVIEW]] Alexa is also compatible with Matter over Wi-Fi and Thread for lights, outlets, sensors, locks, blinds, thermostats, fans, air purifiers, and robot vacuums. Amazon also indicates that with Matter devices, Alexa can control them locally, even during internet outages."',
     '"Alexa also supports Matter over Wi-Fi and over Thread, for lights, outlets, sensors, locks, blinds, thermostats, fans, air purifiers and robot vacuums [2]. Amazon also states that, with Matter devices, Alexa can control them locally, even during internet outages [2]."'),
    ('"title": "Weather"', '"title": "Climate"'),
    ('"text": "Control your compatible thermostats and fans from the app or with a command."', '"text": "Control compatible thermostats and fans from the app or with a command."'),
    ('"text": "Turn on and off lights by room, by scene, or with voice."', '"text": "Turn lights on and off by room, by scene or with your voice."'),
    ('"text": "Raise and lower motorized blinds compatible by time or scene."', '"text": "Raise and lower compatible motorized blinds by time of day or by scene."'),
    ("robotic vacuums", "robot vacuums"),
    ('"Home automation, smart home, and connected home are almost used as synonyms. Some experts call home automation an integrated installation, often wired and planned from the construction phase, while smart home refers to a set of wireless devices that are easier to expand."',
     '"Home automation and smart home are used almost interchangeably. Some specialists use home automation for an integrated installation, often wired and planned from the construction phase, and smart home for a set of wireless devices that are easier to expand."'),
    ('"We start from your home. If it\'s already built, almost everything is resolved with wireless devices. If you\'re building or remodeling, it\'s best to plan cabling and contacts from the beginning."',
     '"We start from your home as it is. If it is already built, almost everything can be done with wireless devices. If you are building or remodeling, it is best to plan wiring and outlets from the start."'),
    ('"An Alexa with integrated Zigbee hub"', '"An Echo with a built-in Zigbee hub"'),
    ('"An Alexa compatible with Matter. For Thread, an Echo with a Thread border router"', '"An Echo that supports Matter. For Thread, an Echo with a Thread border router"'),
    ('"Data consulted in November 2026."', '"Data checked in November 2026."'),
    ('"Not all Echo models include the same radios (Zigbee, Matter, and Thread). Before purchasing each device, we verify its model against Amazon\'s official list."',
     '"Not all Echo models include the same radios (Zigbee, Matter and Thread). Before buying each device, we check its model against Amazon\'s official list."'),
    ('"title": "Diagnosis"', '"title": "Assessment"'),
    ('"We check your home, your Wi-Fi network, and what you want to control."', '"We review your home, your Wi-Fi network and what you want to control."'),
    ('"We define what to install and with which compatible devices, based on your home and not with generic packages."', '"We define what to install and with which compatible devices, based on your home and not on generic packages."'),
    ('"We create the routines and scenes, and we review them with you to make sure everything works."', '"We create the routines and scenes, and check with you that everything works."'),
    ('"We provide follow-up and maintenance after installation."', '"We follow up and provide maintenance after the installation."'),
    ('"MelvTech started as an expert in video surveillance. That\'s why we designed the smart home together with alarms, cameras, and monitoring, so everything works from one place."',
     '"MelvTech started as a video surveillance specialist. That is why we design smart homes together with alarms, cameras and monitoring, so everything runs from one place."'),
    ('"Lighting, locks, and cameras depend on a stable signal throughout the house. If your coverage has dead zones, we resolve this with a mesh Wi-Fi network before installing the devices."',
     '"Lights, locks and cameras depend on a stable signal throughout the house. If your coverage has dead zones, we fix them with a mesh Wi-Fi network before installing the devices."'),
    ('"label": "View networks and Wi-Fi mesh"', '"label": "See networks and mesh Wi-Fi"'),
    ('"label": "View solutions for businesses"', '"label": "See solutions for businesses"'),
    ('"For homes, apartments, and businesses"', '"For houses, apartments and businesses"'),
    ('"We serve households and businesses in Monterrey and its metropolitan area. For offices and branches, access control, structured cabling, and network infrastructure have their own pages."',
     '"We serve homes and businesses in Monterrey and its metropolitan area. For offices and branches, access control, structured cabling and network infrastructure have their own pages."'),
    ('"The cost depends on how many areas you automate, the devices you choose, and the state of your network. That\'s why we quote after the diagnosis and don\'t publish fixed prices. You can start with one area or a function and expand later."',
     '"The cost depends on how many areas you automate, the devices you choose and the state of your network. That is why we quote after the assessment and do not publish fixed prices. You can start with one area or one function and expand later."'),
    ('"q": "What is the difference between home automation, smart home, and connected home?"', '"q": "What is the difference between home automation and a smart home?"'),
    ('"They are almost used as synonyms. Some experts call domótica an integrated installation, often wired and planned from the construction, while smart home refers to a set of connected and wireless devices that are easier to expand. In practice, both concepts are getting closer to each other."',
     '"They are used almost interchangeably. Some specialists use home automation for an integrated installation, often wired and planned from the construction phase, and smart home for a set of connected wireless devices that are easier to expand. In practice, the two concepts are getting closer together."'),
    ('"You need at least one device with Alexa, such as an Echo, or the Alexa app on your phone, a stable Wi-Fi network, and compatible devices. Some Echo models include Zigbee hubs or Matter support, which simplifies installation. We check the model before purchasing it."',
     '"You need at least one Alexa device, such as an Echo, or the Alexa app on your phone, a stable Wi-Fi network and compatible devices. Some Echo models include a Zigbee hub or Matter support, which simplifies the installation. We check the model before you buy it."'),
    ('"Amazon mentions lights, outlets, switches, locks, blinds, thermostats, fans, air purifiers, and robot vacuums, among others. Exact compatibility depends on each device."',
     '"Amazon mentions lights, outlets, switches, locks, blinds, thermostats, fans, air purifiers and robot vacuums, among others. Exact compatibility depends on each device."'),
    ('"Yes, in many cases. Wireless devices (Wi-Fi, Zigbee and Thread) do not require any work. Some functions, such as changing switches or operating blinds, may require electrical work. We define this in the diagnosis."',
     '"Yes, in many cases. Wireless devices (Wi-Fi, Zigbee and Thread) do not require construction work. Some functions, such as replacing switches or motorizing blinds, may need electrical work. We define that during the assessment."'),
    ('"q": "Does it work without internet?"', '"q": "Does it work if the internet goes down?"'),
    ('"It depends on the devices. Amazon says that with Matter devices, Alexa can control them locally, even during internet outages. Controlling from outside the house does require an internet connection. In our proposal, we explain what will continue to work in each case."',
     '"It depends on the devices. Amazon states that, with Matter devices, Alexa can control them locally, even during internet outages. Control from outside the home does require internet. In our proposal we explain what will keep working in each case."'),
    ('"It depends on how many areas you automate, the devices you choose, and the state of your network. We quote after the diagnosis and don\'t publish fixed prices. You can start with one zone or a function and expand later."',
     '"It depends on how many areas you automate, the devices you choose and the state of your network. We quote after the assessment and do not publish fixed prices. You can start with one area or one function and expand later."'),
    ('"A smart home is as secure as its network and passwords. We recommend using a unique password for your Amazon account, enabling two-step verification, and keeping your devices updated."',
     '"A smart home is only as secure as its network and passwords. We recommend a unique password for your Amazon account, two-step verification and keeping your devices updated."'),
    ('"q": "Can they integrate my cameras and my alarm?"', '"q": "Can you integrate my cameras and my alarm?"'),
    ('"Yes. MelvTech started as an expert in video surveillance and offers alarms and camera monitoring, so we can design everything as a single system. Compatibility with the equipment you already have is checked during the diagnosis."',
     '"Yes. MelvTech started as a video surveillance specialist and offers alarms and camera monitoring, so we can design everything as a single system. Compatibility with the equipment you already have is checked during the assessment."'),
    ('"q": "Do they offer support after installation?"', '"q": "Do you offer support after installation?"'),
    ('"Yes. Support and maintenance are part of our process. For businesses, we also offer technical support plans."', '"Yes. Support and maintenance are part of our process. For businesses we also offer technical support plans."'),
    ('"q": "In which areas do they install?"', '"q": "Where do you install?"'),
    ('"a": "In Monterrey and its metropolitan area."', '"a": "In Monterrey and its metropolitan area."'),
    ('"Amazon, Alexa and all related logos are trademarks of Amazon.com, Inc. or its affiliates."', '"Amazon, Alexa and all related logos are trademarks of Amazon.com, Inc. or its affiliates."'),
    ("// Generated with scripts/translate_landing.py (local model) and reviewed by hand.", "// First draft from scripts/translate_landing.py (local model); corrected by hand. This file is now the source of truth."),
]

missing = 0
for old, new in PAIRS:
    if old not in s:
        print("NO ENCONTRADO:", old[:80])
        missing += 1
        continue
    s = s.replace(old, new)
s = s.replace("diagnosis", "assessment")  # resto de usos (FAQ de precios, etc.)
open(P, "w", encoding="utf8", newline="\n").write(s)
print("pares:", len(PAIRS) - missing, "/", len(PAIRS), "| REVIEW restantes:", s.count("[[REVIEW]]"))
sys.exit(1 if missing else 0)

// English content of the landing /en/smart-home-monterrey/ (Spanish pair: /domotica-casas-inteligentes/).
// First draft from scripts/translate_landing.py (local model); corrected by hand. This file is now the source of truth.
// The visible FAQ and the JSON-LD are built from this same data.

export const SITE = "https://melvtech.com";
export const PATH = "/en/smart-home-monterrey/";
export const URL_PAGE = SITE + PATH;
export const UPDATED_ISO = "2026-11-03";
export const UPDATED_LABEL = "November 3, 2026";

export const meta = {
  "title": "Home Automation and Smart Homes in Monterrey | MelvTech",
  "description": "We install home automation and smart homes in Monterrey and its metropolitan area: lights, climate, locks and cameras with Amazon Alexa. Get a quote with no commitment.",
  "ogImage": "/images/og/smart-home-monterrey.jpg"
};

export const hero = {
  "eyebrow": "Home automation in Monterrey and its metropolitan area",
  "h1": "Home automation and smart homes in Monterrey",
  "sub": "Turn your home into a smart home and control it all with Amazon Alexa.",
  "ctaPrimary": {
    "label": "Get a quote for my smart home",
    "url": "/contacto/"
  },
  "ctaSecondary": {
    "label": "See how we work",
    "url": "#proceso"
  },
  "note": "Assessment, installation, Alexa setup and support."
};

export const sources = [
  {
    "id": 1,
    "label": "Amazon Developer: Understand Smart Home Zigbee Support (Alexa)",
    "url": "https://developer.amazon.com/en-US/docs/alexa/smarthome/zigbee-support.html"
  },
  {
    "id": 2,
    "label": "Amazon Developer: Connect Your Device to Alexa with Matter",
    "url": "https://developer.amazon.com/docs/alexaplus/smarthome/matter-support"
  }
];

export const whatIs = {
  "h2": "What is home automation and what is a smart home?",
  "answer": "Home automation is the set of systems that automate the functions of a home: lighting, climate, locks, blinds, cameras, and alarms. A smart home is a house with those systems connected to each other, controlled by voice or from your phone. With an Alexa routine, a single command can turn off all the lights in the house.",
  "more": [
    "Home automation and smart home are used almost interchangeably. Some specialists use home automation for an integrated installation, often wired and planned from the construction phase, and smart home for a set of wireless devices that are easier to expand.",
    "We start from your home as it is. If it is already built, almost everything can be done with wireless devices. If you are building or remodeling, it is best to plan wiring and outlets from the start."
  ]
};

export const controls = {
  "h2": "What can you control with Alexa in your home?",
  "intro": "Amazon lists as compatible with Alexa, among others, lights, switches, outlets, locks, blinds, thermostats, fans, air purifiers, and robot vacuums.",
  "items": [
    {
      "icon": "Lightbulb",
      "title": "Lighting",
      "text": "Turn lights on and off by room, by scene or with your voice."
    },
    {
      "icon": "Thermometer",
      "title": "Climate",
      "text": "Control compatible thermostats and fans from the app or with a command."
    },
    {
      "icon": "Lock",
      "title": "Locks",
      "text": "Close compatible locks with a command or from your phone."
    },
    {
      "icon": "Blinds",
      "title": "Blinds and curtains",
      "text": "Raise and lower compatible motorized blinds by time of day or by scene."
    },
    {
      "icon": "Plug",
      "title": "Outlets and devices",
      "text": "Program smart outlets and compatible devices such as air purifiers and robot vacuums."
    },
    {
      "icon": "ShieldCheck",
      "title": "Cameras and alarms",
      "text": "Integrate your video surveillance and alarms into the same system."
    }
  ],
  "routines": "A routine groups several actions into a single command. For example, \"Good night\" can turn off lights, lock the door, and lower the blinds."
};

export const compat = {
  "h2": "Alexa compatibility: Zigbee, Matter and Wi-Fi",
  "paragraphs": [
    "According to Amazon's official documentation, some Echo and eero devices include built-in smart home hubs that connect Zigbee devices such as switches, outlets, lights and locks [1].",
    "Alexa also supports Matter over Wi-Fi and over Thread, for lights, outlets, sensors, locks, blinds, thermostats, fans, air purifiers and robot vacuums [2]. Amazon also states that, with Matter devices, Alexa can control them locally, even during internet outages [2]."
  ],
  "table": {
    "head": [
      "",
      "Zigbee",
      "Matter",
      "Wi-Fi"
    ],
    "rows": [
      [
        "What you need",
        "An Echo with a built-in Zigbee hub",
        "An Echo that supports Matter. For Thread, an Echo with a Thread border router",
        "Your Wi-Fi network"
      ],
      [
        "Examples according to Amazon",
        "Switches, outlets, lights, and locks",
        "Lights, outlets, sensors, locks, blinds, and thermostats",
        "Devices that connect to Alexa through its app"
      ]
    ]
  },
  "note": "Not all Echo models include the same radios (Zigbee, Matter and Thread). Before buying each device, we check its model against Amazon's official list.",
  "checked": "Data checked in November 2026."
};

export const process = {
  "h2": "How we install your smart home in Monterrey, step by step",
  "steps": [
    {
      "title": "Assessment",
      "text": "We review your home, your Wi-Fi network and what you want to control."
    },
    {
      "title": "Proposal",
      "text": "We define what to install and with which compatible devices, based on your home and not on generic packages."
    },
    {
      "title": "Installation",
      "text": "We install and connect the devices."
    },
    {
      "title": "Alexa setup",
      "text": "We create the routines and scenes, and check with you that everything works."
    },
    {
      "title": "Support",
      "text": "We follow up and provide maintenance after the installation."
    }
  ]
};

export const wifi = {
  "h2": "A smart home starts with Wi-Fi",
  "text": "Lights, locks and cameras depend on a stable signal throughout the house. If your coverage has dead zones, we fix them with a mesh Wi-Fi network before installing the devices.",
  "link": {
    "label": "See networks and mesh Wi-Fi",
    "url": "/services/redes-wifi/"
  }
};

export const security = {
  "h2": "Smart home with integrated security",
  "text": "MelvTech started as a video surveillance specialist. That is why we design smart homes together with alarms, cameras and monitoring, so everything runs from one place.",
  "links": [
    {
      "label": "Video surveillance",
      "url": "/services/videovigilancia/"
    },
    {
      "label": "Alarms",
      "url": "/services/alarmas/"
    },
    {
      "label": "Camera monitoring",
      "url": "/services/monitoreo/"
    }
  ]
};

export const audience = {
  "h2": "For houses, apartments and businesses",
  "text": "We serve homes and businesses in Monterrey and its metropolitan area. For offices and branches, access control, structured cabling and network infrastructure have their own pages.",
  "link": {
    "label": "See solutions for businesses",
    "url": "/empresas/"
  }
};

export const pricing = {
  "h2": "How much does a smart home cost?",
  "text": "The cost depends on how many areas you automate, the devices you choose and the state of your network. That is why we quote after the assessment and do not publish fixed prices. You can start with one area or one function and expand later.",
  "link": {
    "label": "How we quote",
    "url": "/precios/"
  }
};

export const faq: { q: string; a: string }[] = [
  {
    "q": "What is home automation?",
    "a": "Home automation is the set of systems that automate the functions of a home, such as lights, climate, locks, blinds, cameras, and alarms, and control them from one place."
  },
  {
    "q": "What is the difference between home automation and a smart home?",
    "a": "They are used almost interchangeably. Some specialists use home automation for an integrated installation, often wired and planned from the construction phase, and smart home for a set of connected wireless devices that are easier to expand. In practice, the two concepts are getting closer together."
  },
  {
    "q": "What do I need to control my house with Alexa?",
    "a": "You need at least one Alexa device, such as an Echo, or the Alexa app on your phone, a stable Wi-Fi network and compatible devices. Some Echo models include a Zigbee hub or Matter support, which simplifies the installation. We check the model before you buy it."
  },
  {
    "q": "What devices can be controlled with Alexa?",
    "a": "Amazon mentions lights, outlets, switches, locks, blinds, thermostats, fans, air purifiers and robot vacuums, among others. Exact compatibility depends on each device."
  },
  {
    "q": "Can home automation be installed in a house that has already been built?",
    "a": "Yes, in many cases. Wireless devices (Wi-Fi, Zigbee and Thread) do not require construction work. Some functions, such as replacing switches or motorizing blinds, may need electrical work. We define that during the assessment."
  },
  {
    "q": "Does it work if the internet goes down?",
    "a": "It depends on the devices. Amazon states that, with Matter devices, Alexa can control them locally, even during internet outages. Control from outside the home does require internet. In our proposal we explain what will keep working in each case."
  },
  {
    "q": "How much does a smart home cost?",
    "a": "It depends on how many areas you automate, the devices you choose and the state of your network. We quote after the assessment and do not publish fixed prices. You can start with one area or one function and expand later."
  },
  {
    "q": "Is a smart home safe?",
    "a": "A smart home is only as secure as its network and passwords. We recommend a unique password for your Amazon account, two-step verification and keeping your devices updated."
  },
  {
    "q": "Can you integrate my cameras and my alarm?",
    "a": "Yes. MelvTech started as a video surveillance specialist and offers alarms and camera monitoring, so we can design everything as a single system. Compatibility with the equipment you already have is checked during the assessment."
  },
  {
    "q": "Do you offer support after installation?",
    "a": "Yes. Support and maintenance are part of our process. For businesses we also offer technical support plans."
  },
  {
    "q": "Where do you install?",
    "a": "In Monterrey and its metropolitan area."
  }
];

export const trademark = "Amazon, Alexa and all related logos are trademarks of Amazon.com, Inc. or its affiliates.";

export const ui = {
  "home": "Home",
  "services": "Services",
  "pageName": "Home automation and smart homes",
  "breadcrumbAria": "Breadcrumb",
  "heroAlt": "Person controlling the living room lighting from a smart home app on their phone",
  "sourceLabel": "Source",
  "midAria": "Wi-Fi, security and coverage",
  "quoteCta": "Get my quote",
  "orWrite": "You can also write to us at ",
  "faqH2": "Frequently asked questions about home automation and smart homes in Monterrey",
  "sourcesH2": "Sources and last update",
  "madeBy": "Prepared by the MelvTech team. Last updated: "
};

// JSON-LD (@graph). No LocalBusiness: there is no confirmed street address yet.
export function buildSchema() {
  const org = {
    "@type": "Organization",
    "@id": SITE + "/#organization",
    name: "MelvTech",
    url: SITE + "/",
    logo: SITE + "/images/logo-512.png",
    email: "atencion@melvtech.com",
    areaServed: { "@type": "AdministrativeArea", name: "Monterrey metropolitan area, Nuevo León, Mexico" },
    contactPoint: {
      "@type": "ContactPoint",
      contactType: "customer service",
      email: "atencion@melvtech.com",
      availableLanguage: ["es", "en"],
    },
  };
  return {
    "@context": "https://schema.org",
    "@graph": [
      org,
      {
        "@type": "Service",
        "@id": URL_PAGE + "#service",
        name: "Home automation and smart homes",
        serviceType: "Home automation and smart home installation",
        description: meta.description,
        url: URL_PAGE,
        provider: { "@id": SITE + "/#organization" },
        areaServed: [
          { "@type": "City", name: "Monterrey" },
          { "@type": "AdministrativeArea", name: "Monterrey metropolitan area, Nuevo León, Mexico" },
        ],
      },
      {
        "@type": "BreadcrumbList",
        "@id": URL_PAGE + "#breadcrumb",
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Home", item: SITE + "/en/" },
          { "@type": "ListItem", position: 2, name: "Services", item: SITE + "/en/services/" },
          { "@type": "ListItem", position: 3, name: "Home automation and smart homes", item: URL_PAGE },
        ],
      },
      {
        "@type": "FAQPage",
        "@id": URL_PAGE + "#faq",
        inLanguage: "en",
        dateModified: UPDATED_ISO,
        mainEntity: faq.map((f) => ({
          "@type": "Question",
          name: f.q,
          acceptedAnswer: { "@type": "Answer", text: f.a },
        })),
      },
    ],
  };
}

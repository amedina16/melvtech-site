// Contenido de la landing /domotica-casas-inteligentes/.
// El FAQ visible y el JSON-LD se generan desde estos mismos datos.

export const SITE = "https://melvtech.com";
export const PATH = "/domotica-casas-inteligentes/";
export const URL_PAGE = SITE + PATH;
export const UPDATED_ISO = "2026-11-03";
export const UPDATED_LABEL = "3 de noviembre de 2026";

export const meta = {
  title: "Domótica y casas inteligentes en Monterrey | MelvTech",
  description:
    "Instalamos domótica y casas inteligentes en Monterrey y su área metropolitana: luces, clima, cerraduras y cámaras con Amazon Alexa. Cotiza sin compromiso.",
  ogImage: "/images/og/domotica-casas-inteligentes.jpg",
};

export const hero = {
  eyebrow: "Domótica en Monterrey y su área metropolitana",
  h1: "Domótica y casas inteligentes en Monterrey",
  sub: "Transforma tu hogar con tecnología avanzada y control total desde Amazon Alexa.",
  ctaPrimary: { label: "Cotizar mi casa inteligente", url: "/contacto/" },
  ctaSecondary: { label: "Ver cómo trabajamos", url: "#proceso" },
  note: "Diagnóstico, instalación, configuración de Alexa y soporte.",
};

export const sources = [
  {
    id: 1,
    label: "Amazon Developer: Understand Smart Home Zigbee Support (Alexa)",
    url: "https://developer.amazon.com/en-US/docs/alexa/smarthome/zigbee-support.html",
  },
  {
    id: 2,
    label: "Amazon Developer: Connect Your Device to Alexa with Matter",
    url: "https://developer.amazon.com/docs/alexaplus/smarthome/matter-support",
  },
];

export const whatIs = {
  h2: "¿Qué es la domótica y qué es una casa inteligente?",
  answer:
    "La domótica es el conjunto de sistemas que automatizan las funciones de una vivienda: iluminación, clima, cerraduras, persianas, cámaras y alarmas. Una casa inteligente es una vivienda con esos sistemas conectados entre sí, que se controla por voz o desde el celular. Con una rutina de Alexa, un solo comando puede apagar las luces de toda la casa.",
  more: [
    "Domótica, casa inteligente y smart home se usan casi como sinónimos. Algunos especialistas llaman domótica a una instalación integrada, muchas veces cableada y planeada desde la obra, y smart home a un conjunto de dispositivos inalámbricos más fáciles de ampliar.",
    "Nosotros partimos de tu casa. Si ya está construida, casi todo se resuelve con dispositivos inalámbricos. Si estás construyendo o remodelando, conviene planear cableado y contactos desde el inicio.",
  ],
};

export const controls = {
  h2: "¿Qué puedes controlar con Alexa en tu casa?",
  intro:
    "Amazon lista como compatibles con Alexa, entre otros, focos, interruptores, enchufes, cerraduras, persianas, termostatos, ventiladores, purificadores de aire y aspiradoras robot.",
  items: [
    {
      icon: "Lightbulb",
      title: "Iluminación",
      text: "Enciende y apaga luces por cuarto, por escena o con la voz.",
    },
    {
      icon: "Thermometer",
      title: "Clima",
      text: "Controla termostatos y ventiladores compatibles desde la app o con un comando.",
    },
    {
      icon: "Lock",
      title: "Cerraduras",
      text: "Cierra cerraduras compatibles con un comando o desde el celular.",
    },
    {
      icon: "Blinds",
      title: "Persianas y cortinas",
      text: "Sube y baja persianas motorizadas compatibles según la hora o la escena.",
    },
    {
      icon: "Plug",
      title: "Enchufes y aparatos",
      text: "Programa enchufes inteligentes y aparatos compatibles, como purificadores de aire y aspiradoras robot.",
    },
    {
      icon: "ShieldCheck",
      title: "Cámaras y alarmas",
      text: "Integra tu videovigilancia y tus alarmas al mismo sistema.",
    },
  ],
  routines:
    "Una rutina agrupa varias acciones en un solo comando. Por ejemplo, \"Buenas noches\" puede apagar luces, cerrar la cerradura y bajar las persianas.",
};

export const compat = {
  h2: "Compatibilidad con Alexa: Zigbee, Matter y Wi-Fi",
  paragraphs: [
    "Según la documentación oficial de Amazon, algunos dispositivos Echo y eero incluyen hubs de casa inteligente integrados que conectan dispositivos Zigbee, como interruptores, enchufes, focos y cerraduras [1].",
    "Alexa también es compatible con Matter sobre Wi-Fi y sobre Thread, para luces, enchufes, sensores, cerraduras, persianas, termostatos, ventiladores, purificadores de aire y aspiradoras robot [2]. Amazon indica además que, con dispositivos Matter, Alexa puede controlarlos de forma local, incluso durante cortes de internet [2].",
  ],
  table: {
    head: ["", "Zigbee", "Matter", "Wi-Fi"],
    rows: [
      [
        "Qué necesita",
        "Un Echo con hub Zigbee integrado",
        "Un Echo compatible con Matter. Para Thread, un Echo con border router Thread",
        "Tu red Wi-Fi",
      ],
      [
        "Ejemplos según Amazon",
        "Interruptores, enchufes, focos y cerraduras",
        "Luces, enchufes, sensores, cerraduras, persianas y termostatos",
        "Dispositivos que se vinculan a Alexa desde su app",
      ],
    ],
  },
  note: "No todos los modelos de Echo incluyen los mismos radios (Zigbee, Matter y Thread). Antes de comprar cada dispositivo verificamos su modelo contra la lista oficial de Amazon.",
  checked: "Datos consultados en noviembre de 2026.",
};

export const process = {
  h2: "Cómo instalamos tu casa inteligente en Monterrey, paso a paso",
  steps: [
    {
      title: "Diagnóstico",
      text: "Revisamos tu casa, tu red Wi-Fi y lo que quieres controlar.",
    },
    {
      title: "Propuesta",
      text: "Definimos qué instalar y con qué dispositivos compatibles, según tu casa y no con paquetes genéricos.",
    },
    {
      title: "Instalación",
      text: "Instalamos y conectamos los dispositivos.",
    },
    {
      title: "Configuración de Alexa",
      text: "Creamos las rutinas y escenas, y revisamos contigo que todo funcione.",
    },
    {
      title: "Soporte",
      text: "Damos seguimiento y mantenimiento después de la instalación.",
    },
  ],
};

export const wifi = {
  h2: "Una casa inteligente empieza por el Wi-Fi",
  text: "Focos, cerraduras y cámaras dependen de una señal estable en toda la casa. Si tu cobertura tiene zonas muertas, la resolvemos con una red Wi-Fi mesh antes de instalar los dispositivos.",
  link: { label: "Ver redes y WiFi mesh", url: "/services/redes-wifi/" },
};

export const security = {
  h2: "Domótica con seguridad integrada",
  text: "MelvTech empezó como especialista en videovigilancia. Por eso diseñamos la casa inteligente junto con las alarmas, las cámaras y el monitoreo, para que todo opere desde el mismo lugar.",
  links: [
    { label: "Videovigilancia", url: "/services/videovigilancia/" },
    { label: "Alarmas", url: "/services/alarmas/" },
    { label: "Monitoreo de cámaras", url: "/services/monitoreo/" },
  ],
};

export const audience = {
  h2: "Para casas, departamentos y negocios",
  text: "Atendemos hogares y negocios en Monterrey y su área metropolitana. Para oficinas y sucursales, el control de accesos, el cableado estructurado y la infraestructura de red tienen su propia página.",
  link: { label: "Ver soluciones para empresas", url: "/empresas/" },
};

export const pricing = {
  h2: "¿Cuánto cuesta una casa inteligente?",
  text: "El costo depende de cuántas áreas automatizas, de los dispositivos que elijas y del estado de tu red. Por eso cotizamos después del diagnóstico y no publicamos precios cerrados. Puedes empezar por una zona o una función y ampliar después.",
  link: { label: "Cómo cotizamos", url: "/precios/" },
};

export const faq: { q: string; a: string }[] = [
  {
    q: "¿Qué es la domótica?",
    a: "La domótica es el conjunto de sistemas que automatizan las funciones de una vivienda, como las luces, el clima, las cerraduras, las persianas, las cámaras y las alarmas, y las controlan desde un solo lugar.",
  },
  {
    q: "¿Cuál es la diferencia entre domótica, casa inteligente y smart home?",
    a: "Se usan casi como sinónimos. Algunos especialistas llaman domótica a una instalación integrada, muchas veces cableada y planeada desde la obra, y smart home a un conjunto de dispositivos conectados e inalámbricos, más fáciles de ampliar. En la práctica, ambos conceptos se acercan cada vez más.",
  },
  {
    q: "¿Qué necesito para controlar mi casa con Alexa?",
    a: "Necesitas al menos un dispositivo con Alexa, como un Echo, o la app de Alexa en tu celular, una red Wi-Fi estable y dispositivos compatibles. Algunos Echo incluyen hub Zigbee o soporte Matter, lo que simplifica la instalación. Revisamos el modelo antes de comprarlo.",
  },
  {
    q: "¿Qué dispositivos se pueden controlar con Alexa?",
    a: "Amazon menciona luces, enchufes, interruptores, cerraduras, persianas, termostatos, ventiladores, purificadores de aire y aspiradoras robot, entre otros. La compatibilidad exacta depende de cada dispositivo.",
  },
  {
    q: "¿Se puede instalar domótica en una casa que ya está construida?",
    a: "Sí, en muchos casos. Los dispositivos inalámbricos (Wi-Fi, Zigbee y Thread) no requieren obra. Algunas funciones, como cambiar apagadores o motorizar persianas, pueden necesitar trabajo eléctrico. Lo definimos en el diagnóstico.",
  },
  {
    q: "¿Funciona si se va el internet?",
    a: "Depende de los dispositivos. Amazon indica que, con dispositivos Matter, Alexa puede controlarlos de forma local, incluso durante cortes de internet. El control desde fuera de casa sí necesita internet. En la propuesta te explicamos qué seguirá funcionando en cada caso.",
  },
  {
    q: "¿Cuánto cuesta una casa inteligente?",
    a: "Depende de cuántas áreas automatizas, de los dispositivos que elijas y del estado de tu red. Cotizamos después del diagnóstico y no publicamos precios cerrados. Puedes empezar por una zona o una función y ampliar después.",
  },
  {
    q: "¿Es segura una casa inteligente?",
    a: "Una casa inteligente es tan segura como su red y sus contraseñas. Recomendamos usar una contraseña única para tu cuenta de Amazon, activar la verificación en dos pasos y mantener actualizados tus dispositivos.",
  },
  {
    q: "¿Pueden integrar mis cámaras y mi alarma?",
    a: "Sí. MelvTech empezó como especialista en videovigilancia y ofrece alarmas y monitoreo de cámaras, así que podemos diseñar todo como un solo sistema. La compatibilidad con los equipos que ya tienes se revisa en el diagnóstico.",
  },
  {
    q: "¿Dan soporte después de la instalación?",
    a: "Sí. El soporte y el mantenimiento forman parte de nuestro proceso. Para negocios también ofrecemos pólizas de soporte técnico.",
  },
  {
    q: "¿En qué zonas instalan?",
    a: "En Monterrey y su área metropolitana.",
  },
];

export const trademark =
  "Amazon, Alexa y todos los logotipos relacionados son marcas de Amazon.com, Inc. o de sus afiliadas.";

// JSON-LD (@graph). Sin LocalBusiness: aún no hay dirección confirmada.
export function buildSchema() {
  const org = {
    "@type": "Organization",
    "@id": SITE + "/#organization",
    name: "MelvTech",
    url: SITE + "/",
    logo: SITE + "/images/logo-512.png",
    email: "atencion@melvtech.com",
    areaServed: { "@type": "AdministrativeArea", name: "Área metropolitana de Monterrey, Nuevo León, México" },
    contactPoint: {
      "@type": "ContactPoint",
      contactType: "customer service",
      email: "atencion@melvtech.com",
      availableLanguage: "es",
    },
  };
  return {
    "@context": "https://schema.org",
    "@graph": [
      org,
      {
        "@type": "Service",
        "@id": URL_PAGE + "#service",
        name: "Domótica y casas inteligentes",
        serviceType: "Instalación de domótica y casas inteligentes",
        description: meta.description,
        url: URL_PAGE,
        provider: { "@id": SITE + "/#organization" },
        areaServed: [
          { "@type": "City", name: "Monterrey" },
          { "@type": "AdministrativeArea", name: "Área metropolitana de Monterrey, Nuevo León, México" },
        ],
      },
      {
        "@type": "BreadcrumbList",
        "@id": URL_PAGE + "#breadcrumb",
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Inicio", item: SITE + "/" },
          { "@type": "ListItem", position: 2, name: "Servicios", item: SITE + "/services/" },
          { "@type": "ListItem", position: 3, name: "Domótica y casas inteligentes", item: URL_PAGE },
        ],
      },
      {
        "@type": "FAQPage",
        "@id": URL_PAGE + "#faq",
        inLanguage: "es-MX",
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

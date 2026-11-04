"""Correcciones manuales posteriores a scripts/translate_es_en.py (revisión humana del inglés).

Cada tupla: (archivo relativo a src/content/<coleccion>/english, texto viejo, texto nuevo).
Se aplica una vez sobre la salida del traductor. Falla en voz alta si algún texto viejo no existe.
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "content")

FIXES = [
    # ---- pages
    ("pages/nosotros.md", '[[REVIEW]] We', 'About us'),
    ("pages/nosotros.md", "## How do we start?", "## How we started"),
    ("pages/nosotros.md", "## Why we expand our services", "## Why we expanded our services"),
    ("pages/nosotros.md", "not as a change of focus, but as a natural expansion of what we were already doing well.", "not as a change of focus, but as a natural expansion of what we were already doing well."),
    ("pages/nosotros.md", "- We never lock in a price without first knowing your space, that's why we always invite you to get a quote.", "- We never set a price without first knowing your space, which is why we always invite you to request a quote."),
    ("pages/nosotros.md", "- Our services integrate seamlessly: cameras, alarms, home automation, and monitoring operate from the same place.", "- Our services work together: cameras, alarms, home automation and monitoring operate from the same place."),
    ("pages/nosotros.md", "Do you want to learn more about how we can help you? [Get a quote](/en/contacto/) and we'll tell you exactly what you need.", "Want to know how we can help? [Request a quote](/en/contacto/) and we will tell you exactly what you need."),
    ("pages/empresas.mdx", 'title: "Companies"', 'title: "Business"'),
    ("pages/empresas.mdx", "access control, a well-installed network, and an organized infrastructure that any technician can maintain.", "access control, a well-installed network and an organized infrastructure that any technician can maintain."),
    ("pages/empresas.mdx", "Confiable security cameras", "Reliable security cameras"),
    ("pages/empresas.mdx", "## Why MelvTech for your business?", "## Why MelvTech for your business"),
    ("pages/empresas.mdx", "- We never close a price without first knowing your space.", "- We never quote a price without first knowing your space."),
    ("pages/empresas.mdx", "- Our services integrate seamlessly—cameras, access control, network, and servers operate from the same infrastructure.", "- Our services work together: cameras, access control, network and servers run on the same infrastructure."),
    ("pages/empresas.mdx", "Ready to order security and network for your business? [Get a quote](/en/contacto/) and we'll tell you exactly what you need.", "Ready to secure and connect your business? [Request a quote](/en/contacto/) and we will tell you exactly what you need."),
    ("pages/empresas.mdx", 'title="Access Control"', 'title="Access control"'),
    ("pages/empresas.mdx", 'title="Structured Cabling"', 'title="Structured cabling"'),
    ("pages/empresas.mdx", 'title="Network Infrastructure"', 'title="Network infrastructure"'),
    ("pages/empresas.mdx", 'title="Server Administration"', 'title="Server administration"'),
    ("pages/empresas.mdx", 'title="Technical Support Plans"', 'title="Technical support plans"'),
    ("pages/precios.mdx", 'metaDescription: "To get a quote for our home automation, network, alarm, video surveillance, and monitoring services in Monterrey and its metropolitan area."', 'metaDescription: "How we quote home automation, network, alarm, video surveillance and monitoring services in Monterrey and its metropolitan area: after an assessment, with no fixed prices."'),
    ("pages/precios.mdx", "## Get a quote for service", "## Request a quote by service"),
    ("pages/precios.mdx", 'title="home automation"', 'title="Home automation"'),
    ("pages/precios.mdx", 'title="Mesh Wi-Fi Networks"', 'title="Mesh Wi-Fi networks"'),
    ("pages/precios.mdx", 'title="Camera Monitoring"', 'title="Camera monitoring"'),
    ("pages/precios.mdx", 'title="Access Control"', 'title="Access control"'),
    ("pages/precios.mdx", 'title="Structured Cabling"', 'title="Structured cabling"'),
    ("pages/precios.mdx", 'title="Network Infrastructure"', 'title="Network infrastructure"'),
    ("pages/precios.mdx", 'title="Server Administration"', 'title="Server administration"'),
    ("pages/precios.mdx", 'title="Technical Support Plans"', 'title="Technical support plans"'),
    ("pages/precios.mdx", "That's why we don't offer fixed prices — we quote after knowing your space so you pay exactly for what you need, without surprises or generic packages.", "That is why we do not publish fixed prices. We quote after getting to know your space, so you pay for what you need, without surprises or generic packages."),
    ("pages/precios.mdx", "3. We give you a clear price before installation — without any commitment.", "3. We give you a clear price before installation, with no commitment."),
    ("pages/precios.mdx", "Ready to get started? [Get a quote](/en/contacto/) and we'll tell you exactly what you need.", "Ready to get started? [Request a quote](/en/contacto/) and we will tell you exactly what you need."),
    # ---- services (home)
    ("services/domotica.mdx", 'title: "home automation"', 'title: "Home automation"'),
    ("services/domotica.mdx", "[Home Automation and Smart Homes in Monterrey](/en/domotica-casas-inteligentes/)", "[Home automation and smart homes in Monterrey](/en/smart-home-monterrey/)"),
    ("services/domotica.mdx", "Smart home doesn't work alone — it connects", "Home automation does not work alone: it connects"),
    ("services/videovigilancia.mdx", "**Interior and Exterior Coverage as You Need It**", "**Indoor and outdoor coverage, as you need it**"),
    ("services/monitoreo.mdx", "- [[REVIEW]] Active monitoring of your cameras, not just passive recording", "- **Active monitoring of your cameras, not just passive recording**"),
    # ---- services (business)
    ("services/control-accesos.mdx", "- Card reader or proximity sensor", "- Card or proximity reader"),
    ("services/control-accesos.mdx", "- Fingerprint scanner", "- Fingerprint reader"),
    ("services/control-accesos.mdx", "- Access code keyboard", "- Keypad with access code"),
    ("services/control-accesos.mdx", "## Where We Install", "## Where we install"),
    ("services/control-accesos.mdx", "- Parking and vehicle tags", "- Parking lots and vehicle barriers"),
    ("services/control-accesos.mdx", "(servers, storage, safe)", "(servers, storage, cash register)"),
    ("services/control-accesos.mdx", "- No longer rely on copying or recovering physical keys", "- You no longer depend on copying or recovering physical keys"),
    ("services/control-accesos.mdx", "- Person-by-person and door entry/exit logs", "- Entry and exit log by person and by door"),
    ("services/control-accesos.mdx", "- Restricts sensitive areas without constant surveillance", "- Restrict sensitive areas without constant supervision"),
    ("services/control-accesos.mdx", "Access control doesn't work alone – it connects", "Access control does not work alone: it connects"),
    ("services/control-accesos.mdx", 'title="Without physical keys"', 'title="No physical keys"'),
    ("services/control-accesos.mdx", 'description="Card, fingerprint or code – control access without copying keys."', 'description="Card, fingerprint or code: control access without copying keys."'),
    ("services/cableado-estructurado.mdx", "- Structured cabling Category 6 and 6a", "- Category 6 and 6A structured cabling"),
    ("services/cableado-estructurado.mdx", "- Visible or ducted wiring, depending on the space", "- Surface-mounted or conduit wiring, depending on the space"),
    ("services/cableado-estructurado.mdx", "- Patch panels and cable organizers labeled", "- Labeled patch panels and cable organizers"),
    ("services/cableado-estructurado.mdx", "## Custom installations", "## Installations for"),
    ("services/cableado-estructurado.mdx", "- Fewer connection failures with improvised wiring", "- Fewer connection failures than with improvised wiring"),
    ("services/cableado-estructurado.mdx", "- Installation ready to grow without redoing", "- An installation ready to grow without being redone"),
    ("services/cableado-estructurado.mdx", "Structured cabling is the foundation of your other systems—it connects to", "Structured cabling is the foundation of your other systems. It connects to"),
    ("services/cableado-estructurado.mdx", 'title="Growth foundation"', 'title="Room to grow"'),
    ("services/cableado-estructurado.mdx", 'description="A mesh Wi-Fi network to add more devices without redoing the installation."', 'description="A base that lets you add more devices without redoing the installation."'),
    ("services/infraestructura-redes.mdx", "Our network infrastructure is where we design how your entire business connects:", "With network infrastructure we design how your whole business connects:"),
    ("services/infraestructura-redes.mdx", "- Administrable switch configuration", "- Managed switch configuration"),
    ("services/infraestructura-redes.mdx", 'imageAlt="Administrable switch configured in a network rack"', 'imageAlt="Managed switch configured in a network rack"'),
    ("services/infraestructura-redes.mdx", "from manageable switches to VLAN segmentation", "from managed switches to VLAN segmentation"),
    ("services/infraestructura-redes.mdx", "The result is an ordered network by segments, where a problem in one area does not affect the others.", "The result is a network organized into segments, where a problem in one area does not affect the others."),
    ("services/infraestructura-redes.mdx", "- A safer network by separating sensitive traffic from the rest", "- A safer network, with sensitive traffic separated from the rest"),
    ("services/infraestructura-redes.mdx", "- Better performance by avoiding all competing for the same channel", "- Better performance, because not everything competes for the same channel"),
    ("services/infraestructura-redes.mdx", "- A single point of responsibility for making your entire network work together", "- A single point of responsibility for making your whole network work together"),
    ("services/infraestructura-redes.mdx", "The network infrastructure is the foundation of your other systems—cameras, access control, and Wi-Fi connect to it so everything operates in order.", "Network infrastructure is the foundation of your other systems: cameras, access control and Wi-Fi connect to it so everything runs in an orderly way."),
    ("services/infraestructura-redes.mdx", 'title="List to grow"', 'title="Ready to grow"'),
    ("services/administrador-servidores.mdx", "We monitor your business servers – updates, backups, and maintenance – for businesses in Monterrey and its metropolitan area.", "We look after your business servers (updates, backups and maintenance) for businesses in Monterrey and its metropolitan area."),
    ("services/administrador-servidores.mdx", "The result is a server you check less because someone else is already monitoring it for you.", "The result is a server you have to check less, because someone else is already watching it for you."),
    ("services/administrador-servidores.mdx", "- Information backed by errors or hardware failures", "- Your information protected against errors and hardware failures"),
    ("services/administrador-servidores.mdx", "- Updated and protected server", "- An updated and protected server"),
    ("services/polizas-soporte-tecnico.mdx", "## What this policy includes", "## What this plan includes"),
    ("services/polizas-soporte-tecnico.mdx", "- Priority of attention for customers without a support plan", "- Priority over customers without a support plan"),
    ("services/polizas-soporte-tecnico.mdx", "The result is a business that detects failures before you lose service, instead of waiting for something to break down.", "The result is a business that detects failures before it loses service, instead of waiting for something to break."),
    ("services/polizas-soporte-tecnico.mdx", "- We detect faults before you're left without service", "- We detect faults before you are left without service"),
    ("services/polizas-soporte-tecnico.mdx", "- Predictable maintenance budget, no surprises", "- A predictable maintenance budget, with no surprises"),
    ("services/polizas-soporte-tecnico.mdx", "- Less time waiting for someone to attend you", "- Less time waiting for someone to help you"),
    ("services/polizas-soporte-tecnico.mdx", "## What does this policy cover?", "## What does this plan cover?"),
    ("services/polizas-soporte-tecnico.mdx", 'description="Attention to defined response time when something fails."', 'description="A defined response time when something fails."'),
    # ---- sections
    ("sections/contact-section.md", '"[[REVIEW]] Email"', '"Email"'),
    ("sections/startup-skill-section.md", 'title: "professional installation"', 'title: "Professional installation"'),
]

bad = 0
for rel, old, new in FIXES:
    coll, name = rel.split("/", 1)
    path = os.path.join(ROOT, coll, "english", name)
    s = open(path, encoding="utf8").read()
    if old not in s:
        print("NO ENCONTRADO:", rel, "|", old[:70])
        bad += 1
        continue
    open(path, "w", encoding="utf8", newline="\n").write(s.replace(old, new))
print("aplicadas", len(FIXES) - bad, "de", len(FIXES))
sys.exit(1 if bad else 0)

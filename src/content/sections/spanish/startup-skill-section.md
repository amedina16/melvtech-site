---
enable: true
imagePosition: "left"

images:
  large: "/images/skill/skill-1.png"
  small: "/images/skill/skill-2.jpg"

title: |
  Soluciones completas para tu hogar o negocio
subtitle: |
  Te ayudamos a elegir exactamente lo que necesitas, sin equipo de más ni instalaciones complicadas.
description: |
  Diseñamos, instalamos y damos soporte a sistemas de domótica, redes, alarmas, videovigilancia y monitoreo, adaptados al tamaño real de tu propiedad.

# EXTRATYPE OPTIONS: "skills" | "list-x" | "list-y" | "stats" | "none"
extraType: "list-x"

# SHARED BUTTON CONFIGURATION (Applies to all section buttons)
buttons:
  - enable: false # Boolean: true | false
    label: "Descubre nuestros servicios"
    url: "/services/"
    tag: "a" # Enum: a | button
    variant: "fill" # Enum: fill | fill-white | outline | text | circle
    hoverEffect: "magnetic-text-flip" # Enum: text-flip | creative-fill | magnetic | magnetic-text-flip
    icon: # Object
      enable: true
      name: "ArrowUpRight" # String: Lucide Icon Name - https://lucide.de v/icons/?search=
      position: "right" # Enum: left | right (Note: text variant is always right)
    rel: "noopener"
    target: "_blank" # String: _blank | _self
    class: "" # String: Additional button Tailwind classes

listItems:
  - title: "Instalación<br />profesional"
    icon: "Settings"
  - title: "Soporte<br />cuando lo necesitas"
    icon: "Headphones"
---

---
enable: true # Boolean: true | false
imagePosition: "left" # Enum: left | right

images:
  large: "/images/about-us/about-1-a.jpg"
  small: "/images/about-us/about-1-b.jpg"

title: |
  Especialistas en videovigilancia, ahora en hogar conectado
subtitle: |
  Empezamos como especialistas en cámaras de seguridad, y con el tiempo ampliamos ese conocimiento a domótica, redes y alarmas para ofrecerte una solución completa.
description: |
  Ayudamos a familias y negocios en Monterrey y su área metropolitana a mejorar su seguridad y conectividad, con instalaciones claras, soporte cercano y sistemas fáciles de usar.

# EXTRATYPE OPTIONS: "skills" | "list-x" | "list-y" | "stats" | "none"
extraType: "none"

# SHARED BUTTON CONFIGURATION (Applies to all section buttons)
buttons:
  - enable: true # Boolean: true | false
    label: "Descubre nuestros servicios"
    url: "/services/"
    tag: "a" # Enum: a | button
    variant: "fill" # Enum: fill | fill-white | outline | text | circle
    hoverEffect: "magnetic-text-flip" # Enum: text-flip | creative-fill | magnetic | magnetic-text-flip
    icon: # Object
      enable: false
      name: "ArrowUpRight" # String: Lucide Icon Name - https://lucide.de v/icons/?search=
      position: "right" # Enum: left | right (Note: text variant is always right)
    rel: "noopener"
    target: "_blank" # String: _blank | _self
    class: "" # String: Additional button Tailwind classes


# extraType: "skills"
# skills: # Array of objects
#   - label: "IT Solution & Management"
#     value: "86" # String: Percentage value (0-100)
#   - label: "Website & App Development"
#     value: "72"

# extraType: "list-x"
# listItems: # Array of objects
#   - title: "Provide Skills Services"
#     icon: "Settings" # String: Lucide Icon Name
#   - title: "Urgent Support For Clients"
#     icon: "Headphones"

# extraType: "stats"
# stats: # Array of objects
#   - value: "1800" # String: Numeric value for animation
#     prependValue: "$" # String: Symbol before number
#     appendValue: "+" # String: Symbol after number
#     label: "Happy Clients"

# extraType: "list-y"
# listItems: # Array of objects
#   - title: "Quality Solution for Business"
#     description: "Customize almost anything in the appearance."
#     icon: "Trophy" # String: Lucide Icon Name
---

---
enable: true # Boolean: true | false
imagePosition: "left" # Enum: left | right

images:
  large: "/images/about-us/about-1-a.jpg"
  small: "/images/about-us/about-1-b.jpg"

title: |
  Experts in video surveillance, now for your connected home
subtitle: |
  We started as experts in security cameras and over time expanded our knowledge to include home automation, networks, and alarms, offering you a complete solution.
description: |
  We help families and businesses in Monterrey and its metropolitan area improve their security and connectivity with clear installations, close support, and easy-to-use systems.
# EXTRATYPE OPTIONS: "skills" | "list-x" | "list-y" | "stats" | "none"
extraType: "none"

# SHARED BUTTON CONFIGURATION (Applies to all section buttons)
buttons:
  - enable: true # Boolean: true | false
    label: "Discover our services"
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

---
# Default content for `src/layouts/components/ServicesSingle.astro`.
# The service sidebar list is generated from the services collection.
# `contact` feeds `src/layouts/components/widgets/ServicesSingleCta.astro`.
contact:
  icon: "Headset"
  title: "Ready to take the next step?"
  description: "At MelvTech, we commit to providing you with close service and reliable support at every installation."
  button:
    # Refer to the `sharedButton` schema in `src/sections.schema.ts` for all available configuration options
    enable: true
    label: "Contact us"
    url: "/contacto/"
    hoverEffect: "magnetic-text-flip"
    variant: "fill"
    rel: "" # Optional
    target: "" # Optional
    class: "rounded-md px-6 py-3.5 text-sm leading-6 font-semibold normal-case" # Optional
    icon: # Optional
      enable: false
      name: "ArrowUpRight"
      position: "right"
---

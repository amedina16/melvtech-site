---
enable: true # Control the visibility of this section across all pages where it is used
title: "¿Tienes un proyecto en mente?"
description: "¡Perfecto! Nos encanta escucharte, empecemos juntos"
officeHours: "Horario de atención: lun. - sáb.: 8:00 AM - 10:00 PM" # Optional; remove or set empty to hide this row.

# Check config.toml file for form action related settings
# this is also used in the footer of the personal portfolio homepage
formTitle: "Llena el formulario de contacto"
formDescription: "Cuéntanos qué necesitas y nuestro equipo te responderá con los siguientes pasos."

form:
  emailSubject: "Nueva solicitud de contacto desde tu sitio web" # Customized email subject (applicable when anyone submit form, form submission may receive by email depend on provider)
  submitButton:
    # Refer to the `sharedButton` schema in `src/sections.schema.ts` for all available configuration options (e.g., enable, label, url, hoverEffect, variant, icon, tag, rel, class, target, etc.)
    enable: true
    label: "Enviar mensaje"
    class: "w-full justify-center rounded-md"
    hoverEffect: "magnetic-text-flip" # Optional: text-flip | creative-fill | magnetic | magnetic-text-flip
    # variant: "" # Optional: fill | outline | text | circle
    # rel: "" # Optional
    # target: "" # Optional

  # This note will show at the end of form
  # note: |
  #   Your data is safe with us. We respect your privacy and never share your information. <br /> Read our [Privacy Policy](/privacy-policy/).
  inputs:
    - label: "Tu nombre"
      name: "Name"
      placeholder: "Tu nombre"
      required: true
      halfWidth: true
    - label: "Correo electrónico"
      name: "Email"
      placeholder: "Correo electrónico"
      type: "email"
      required: true
      halfWidth: true
    - label: "Presupuesto estimado"
      name: "Budget"
      placeholder: "Presupuesto estimado"
      type: "number"
      halfWidth: true
    - label: "Fecha de inicio deseada"
      name: "Start Date"
      placeholder: "Fecha de inicio deseada"
      type: "date"
      halfWidth: true
    - label: "Servicio que te interesa"
      name: "Service"
      placeholder: "Selecciona un servicio"
      required: true
      dropdown:
        type: "search"
        search:
          placeholder: "Buscar un servicio"
        items:
          - label: "Domótica"
            value: "Domótica"
          - label: "Redes y WiFi Mesh"
            value: "Redes y WiFi Mesh"
          - label: "Alarmas"
            value: "Alarmas"
          - label: "Videovigilancia"
            value: "Videovigilancia"
          - label: "Monitoreo de Cámaras"
            value: "Monitoreo de Cámaras"
    - label: "Proyecto nuevo"
      name: "Project Type"
      value: "New project"
      type: "radio"
      group: "Project Type"
      groupLabel: "Tipo de proyecto"
      checked: true
      halfWidth: true
    - label: "Mejorar un sistema existente"
      name: "Project Type"
      value: "Improve existing system"
      type: "radio"
      group: "Project Type"
      halfWidth: true
    - label: "Correo electrónico"
      name: "Preferred Contact"
      value: "Email"
      type: "checkbox"
      group: "Preferred Contact"
      groupLabel: "Medio de contacto preferido"
      checked: true
      halfWidth: true
    - label: "Teléfono"
      name: "Preferred Contact"
      value: "Phone"
      type: "checkbox"
      group: "Preferred Contact"
      halfWidth: true
    - label: "Escribe tu mensaje"
      name: "Message"
      placeholder: "Escribe tu mensaje"
      tag: "textarea"
      rows: "5"
      required: true
    - label: "Acepto ser contactado sobre esta solicitud."
      name: "Consent"
      value: true
      type: "checkbox"
      required: true
    - note: success
      parentClass: "hidden text-sm message success"
      content: "Gracias. Recibimos tu solicitud y te responderemos con los siguientes pasos."
    - note: deprecated
      parentClass: "hidden text-sm message error"
      content: "Ocurrió un error. Intenta de nuevo o contáctanos directamente."
---

---
enable: true # Control the visibility of this section across all pages where it is used
title: "Do you have a project in mind?"
description: "Great! We love hearing from you, let's get started together"
officeHours: "" # Optional; remove or set empty to hide this row.

# Check config.toml file for form action related settings
# this is also used in the footer of the personal portfolio homepage
formTitle: "Fill out the contact form"
formDescription: "Tell us what you need and our team will respond with the following steps."

form:
  emailSubject: "New contact request from your website" # Customized email subject (applicable when anyone submit form, form submission may receive by email depend on provider)
  submitButton:
    # Refer to the `sharedButton` schema in `src/sections.schema.ts` for all available configuration options (e.g., enable, label, url, hoverEffect, variant, icon, tag, rel, class, target, etc.)
    enable: true
    label: "Send message"
    class: "w-full justify-center rounded-md"
    hoverEffect: "magnetic-text-flip" # Optional: text-flip | creative-fill | magnetic | magnetic-text-flip
    # variant: "" # Optional: fill | outline | text | circle
    # rel: "" # Optional
    # target: "" # Optional

  # This note will show at the end of form
  # note: |
  #   Your data is safe with us. We respect your privacy and never share your information. <br /> Read our [Privacy Policy](/privacy-policy/).
  inputs:
    - label: "Your name"
      name: "Name"
      placeholder: "Your name"
      required: true
      halfWidth: true
    - label: "Email"
      name: "Email"
      placeholder: "Email"
      type: "email"
      required: true
      halfWidth: true
    - label: "Estimated budget"
      name: "Budget"
      placeholder: "Estimated budget"
      type: "number"
      halfWidth: true
    - label: "Desired start date"
      name: "Start Date"
      placeholder: "Desired start date"
      type: "date"
      halfWidth: true
    - label: "Service you are interested in"
      name: "Service"
      placeholder: "Select a service"
      required: true
      dropdown:
        type: "search"
        search:
          placeholder: "Search for a service"
        items:
          - label: "home automation"
            value: "Domótica"
          - label: "Mesh Wi-Fi Networks"
            value: "Redes y WiFi Mesh"
          - label: "Alarms"
            value: "Alarmas"
          - label: "Video surveillance"
            value: "Videovigilancia"
          - label: "Camera Monitoring"
            value: "Monitoreo de Cámaras"
    - label: "New Project"
      name: "Project Type"
      value: "New project"
      type: "radio"
      group: "Project Type"
      groupLabel: "Project Type"
      checked: true
      halfWidth: true
    - label: "Improve an existing system"
      name: "Project Type"
      value: "Improve existing system"
      type: "radio"
      group: "Project Type"
      halfWidth: true
    - label: "Email"
      name: "Preferred Contact"
      value: "Email"
      type: "checkbox"
      group: "Preferred Contact"
      groupLabel: "Preferred method of contact"
      checked: true
      halfWidth: true
    - label: "Phone"
      name: "Preferred Contact"
      value: "Phone"
      type: "checkbox"
      group: "Preferred Contact"
      halfWidth: true
    - label: "Write your message"
      name: "Message"
      placeholder: "Write your message"
      tag: "textarea"
      rows: "5"
      required: true
    - label: "I accept being contacted about this request."
      name: "Consent"
      value: true
      type: "checkbox"
      required: true
    - note: success
      parentClass: "hidden text-sm message success"
      content: "Thank you. We have received your request and will respond with the following steps."
    - note: deprecated
      parentClass: "hidden text-sm message error"
      content: "An error occurred. Try again or contact us directly."
---

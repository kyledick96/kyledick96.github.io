---
layout: project
project: elevator
permalink: /projects/elevator/
---
{% assign case_project = site.data.projects | where: "slug", page.project | first %}

## Overview

Steam Punk Elevator Project VI was a multi-processor embedded control project integrating STM32, Raspberry Pi, Arduino and motor-controller hardware. I developed STM32 firmware and worked on communication, safety behaviour and system testing.

## System Architecture

CAN connected the embedded devices across the system. A Raspberry Pi/Linux layer and user interface interacted with the control hardware, creating dependencies between device communication, application state and physical inputs.

## My Contribution

I developed STM32 firmware in C and integrated and debugged CAN communication. I also investigated faults that crossed embedded, Linux and UI layers and performed structured tests of emergency-call, floor-selection and input-lockout behaviour.

## STM32 Firmware

My firmware work covered device communication, control behaviour and safety logic. Testing required checking how the STM32 responded to inputs and how those responses interacted with the other processors and motor-controller hardware.

## CAN Network

I integrated and debugged communication across STM32, Raspberry Pi, Arduino and motor-controller hardware. The work involved following faults across device boundaries rather than testing each processor in isolation.

## Safety and Control Logic

I worked on control and safety behaviour involving emergency-call functionality, floor selection and button/input lockout. Testing examined the system's responses to these inputs and whether control and interface behaviour remained consistent.

This was an educational control project. The described safety logic is project functionality, with no claim of certified elevator safety compliance.

## System Integration

I coordinated dependencies between embedded firmware, Raspberry Pi/Linux services and the PHP/JSON user interface. Cross-layer debugging connected user-visible behaviour to communication and firmware responses.

## Testing

I performed structured system-level tests for emergency calls, floor selection and button/input lockout. These checks exercised behaviour across processors and the interface layer. The available portfolio record describes the testing scope without a complete published pass/fail matrix.

{% comment %}Add test records, CAN diagrams, screenshots, photographs, PDFs or a project GitHub URL when available. Keep any future artifact links alongside the relevant section.{% endcomment %}

## Technologies

{% include tags.html items=case_project.technologies %}

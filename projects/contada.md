---
layout: project
project: contada
permalink: /projects/contada/
---
{% assign case_project = site.data.projects | where: "slug", page.project | first %}

## Overview

CONTADA was an embedded telemetry, instrumentation and control platform for a wind-energy system, developed through the Conestoga SMART Research Centre collaboration with Purus Power. The project ran from September 2025 to August 2026. My contribution focused on embedded firmware, sensor integration, telemetry and validation.

## Engineering Problem

The platform needed to connect physical measurements, edge devices and Linux-hosted services into a system the engineering team could test and inspect. Sensor acquisition, communications and instrumentation choices had to be considered together because a fault anywhere along the path could affect the measurements available to the team.

## System Architecture

I contributed to architecture work involving embedded controllers, Raspberry Pi/Linux systems, DAQ hardware and communications. ESP32-S3 edge devices acquired sensor data, while Mosquitto MQTT and Node-RED supported telemetry and visualization on the Linux side.

The architecture work included evaluation of alternative interfaces and networking approaches. The technical summary describes the project at a high level rather than presenting a final production design.

## My Contribution

I developed and tested C firmware, integrated sensors and connected embedded targets to Linux services. I also performed hardware bring-up, diagnosed end-to-end telemetry faults and developed validation procedures.

I presented technical progress and engineering recommendations in client-facing reviews with Purus Power and the SMART Centre team. Architecture and equipment decisions were collaborative.

## Embedded Hardware and Firmware

My ESP32-S3 firmware work covered I2C, analog and digital sensor acquisition and telemetry. Documented sensor work includes BME680, BNO085 and ADXL335 devices.

During bring-up, I interpreted schematics, datasheets and interface documentation alongside serial output and bench measurements. This connected firmware behaviour to the wiring and electrical interfaces being tested.

## Instrumentation and DAQ

I contributed to DAQ evaluation and the integration of measurement hardware into the system architecture. Bench work used oscilloscopes, multimeters and power supplies to investigate hardware and sensor behaviour.

Sensor validation and serial diagnostics supported the transition from individual device checks to system integration. The public project documentation does not specify a final DAQ configuration or measured system accuracy.

## Communications

I integrated MQTT telemetry with Raspberry Pi/Linux, Mosquitto and Node-RED, and diagnosed faults across device firmware, the network and backend services.

I evaluated Wi-Fi versus Ethernet approaches and investigated CAN and RS485/Modbus interfaces. These were architecture and interface investigations; the available records do not establish that every evaluated protocol was deployed in the final platform.

## Testing and Validation

I developed repeatable bench procedures to check sensor readings, communication interfaces and end-to-end telemetry. Troubleshooting combined serial logs, network checks, Node-RED inspection and laboratory measurements to identify where data stopped matching expectations.

The work produced validation procedures and engineering recommendations for the team. No numerical reliability or performance result is claimed here.

## Engineering Decisions

Communications evaluation considered embedded interfaces alongside Linux services and measurement hardware. I contributed findings to the team's architecture discussions rather than selecting the entire system independently.

I also created MATLAB/Simulink models for sensor-driven control behaviour and validation. These models helped communicate control behaviour during development and technical reviews.

## Supporting Artifacts

{% include documents.html documents=case_project.documents %}

{% comment %}Add approved architecture diagrams, instrument screenshots, reports or repository links here. Keep client material within the scope of the existing public technical summary.{% endcomment %}

## Technologies

The list includes implemented tools and interfaces evaluated during architecture work.

{% include tags.html items=case_project.technologies %}

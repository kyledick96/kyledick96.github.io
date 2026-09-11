---
layout: project
project: sdacs
permalink: /projects/sdacs/
---
{% assign case_project = site.data.projects | where: "slug", page.project | first %}

## Overview

SDACS connects multiple acoustic sensor nodes to a common backend for room-acoustic measurement and analysis. The capstone combined embedded acquisition and processing with Linux services, telemetry storage and engineering validation. I worked primarily on node firmware, hardware interfaces and integration with the backend.

## Engineering Problem

Measurements from several locations need a consistent acquisition and reporting path before they can support room-level analysis. The project required microphone and environmental data to move from embedded hardware into a shared system where the team could inspect, compare and record it. Calibration differences between nodes also needed investigation.

## System Architecture

Each recording node uses an ESP32-S3 and an I2S microphone. Firmware calculates acoustic features locally and publishes them alongside sensor telemetry using MQTT over Wi-Fi. A Raspberry Pi/Linux backend hosts Mosquitto and Node-RED, with SQLite and CSV storage workflows for later analysis.

The diagrams document the team's system design. Some blocks describe broader project scope and development-stage features beyond my individual firmware contribution.

![SDACS firmware, backend and user-interface process flow]({{ '/Diagrams/SDACS%20Two-Process%20Flow%20Chart.png' | relative_url }})

The system separates embedded sensing from backend processing and the user interface. ESP32-S3 nodes publish measurements and status through MQTT to the Raspberry Pi backend, while higher-level services expose system data to the application.

<details>
<summary>View detailed subsystem diagrams</summary>

![Recording node functional block diagram]({{ '/Diagrams/SDACS_RecordingNodes_FunctionalBlockDiagram.png' | relative_url }})

![Raspberry Pi server functional block diagram]({{ '/Diagrams/SDACS_Server_FunctionalBlockDiagram.png' | relative_url }})

[View conceptual node placement]({{ '/Diagrams/SDACS_Conceptual_Diagram.png' | relative_url }})

</details>

## My Contribution

I developed ESP-IDF firmware in C, integrated acoustic and environmental acquisition, and implemented feature publication. I also diagnosed faults across the hardware, firmware, Wi-Fi connection and MQTT path, and developed calibration and hardware-interface validation procedures.

The project used Git/GitHub branches for team development and integration. My work connected the embedded nodes to shared backend services; the diagrams and reports include contributions from the wider team.

## Embedded Hardware

Each SDACS recording node combines an ESP32-S3 development platform with custom hardware for acoustic sensing, environmental measurement and system status.

![SDACS custom PCB]({{ '/Diagrams/SDACS_PCB.png' | relative_url }})

*Custom PCB used to integrate the sensing and status hardware for each recording node.*

![Assembled SDACS recording node]({{ '/Diagrams/SDACS_Node.png' | relative_url }})

*Assembled recording node showing the embedded hardware integrated into the physical enclosure.*

## Embedded Firmware

I worked in a FreeRTOS-based environment, with firmware handling I2S acquisition, I2C sensors, configuration and network communication. I implemented continuous audio acquisition and added/configured SD-card credential loading. My configuration work also included calibration-offset persistence concepts using NVS.

![SDACS firmware audio-processing pipeline]({{ '/Diagrams/SDACS%20Firmware%20Audio%20Processing%20Flow.png' | relative_url }})

*Audio moves from I2S acquisition through buffering, signal conditioning and feature extraction before measurements are packaged for MQTT publication.*

The supporting reports capture earlier firmware stages, including timed recording runs and header-based network configuration. Pin assignments also changed between tested hardware configurations, so wiring checks were part of firmware bring-up.

## Signal Processing

I implemented RMS and dBFS calculations and 2048-point FFT feature processing on the ESP32-S3. Local feature calculation allowed the nodes to publish acoustic measurements for inspection and analysis through the telemetry system.

The calibration workflow related digital measurements to reference readings. The case study does not treat dBFS readings alone as calibrated sound-pressure measurements.

<details>
<summary>View additional audio-processing detail</summary>

![SDACS audio acquisition detail]({{ '/Diagrams/SDACS_Audio_Acquisition.png' | relative_url }})

</details>

## Networking and Backend

I published acoustic and environmental telemetry through MQTT over Wi-Fi and integrated nodes with Raspberry Pi/Linux, Mosquitto, Node-RED and SQLite workflows. Serial logs, broker monitoring and Node-RED debug views helped trace missing or unexpected data through the system.

The linked Node-RED export contains a labelled dataset-capture workflow. It is one part of the backend; it does not contain the complete SQLite integration described in the broader design documentation.

### User Interface

The Flutter interface consumes backend data and presents node status, capture controls and acoustic results. It demonstrates the full path from embedded measurement through backend services to a user-facing application.

![SDACS Flutter user interface]({{ '/Diagrams/SDACS_Flutter_UI.png' | relative_url }})

## Calibration and Validation

I developed procedures using controlled acoustic inputs, reference measurements, serial diagnostics and laboratory equipment. Hardware-interface checks included sensor visibility, pin mapping and the path from acquisition to published telemetry.

### Physical test setup

![Four assembled SDACS recording nodes]({{ '/Diagrams/SDACS_Nodes.png' | relative_url }})

*Four assembled nodes used for multi-node system testing.*

![SDACS nodes deployed in the recording environment]({{ '/Diagrams/SDACS_Node_Recording_Environment.jpg' | relative_url }})

*Representative indoor test environment used for acoustic and system-level validation.*

The functional test report records network connection, data logging, acoustic and temperature checks. Its results tables, checklist and later summary do not give a consistent blanket pass: temperature measurement remained a concern, and the observations recommend further acoustic testing in a stricter lab environment. These records document a development-stage test campaign.

The related dataset review also identifies node-to-node response differences and overlapping feature classes. Its offline Random Forest checks are separate from Edge Impulse deployment results.

## Engineering Challenges

Wi-Fi reconnect behaviour, dropped MQTT publications, serial-port conflicts and I2S pin naming made faults appear at different layers of the system. I used firmware logs, I2C scans, broker monitoring and physical pin checks to narrow those faults to the relevant interface.

Calibration and configuration also changed as the system developed. Repeatable input conditions and clear records of firmware and wiring configurations were needed to compare measurements across tests.

## Supporting Artifacts

### Final Project Documentation

- [Capstone II Final Report (PDF)]({{ '/Documents/Capstone_II_SDACS_FinalReport.pdf' | relative_url }})
- [Engineering Design and Test Plan (PDF)]({{ '/Documents/SDACS_EngineeringDesign%26TestPlan.pdf' | relative_url }})
- [Functional Test Report (PDF)]({{ '/Documents/SDACS_Test_Report.pdf' | relative_url }})
- [Firmware Architecture Overview (PDF)]({{ '/Documents/Kyle_Dick_SDACS_Firmware_Architecture_README.pdf' | relative_url }})
- [Summary of Work (PDF)]({{ '/Documents/SDACS_SummaryofWork.pdf' | relative_url }})
- [Design and Testing Presentation (PDF)]({{ '/Presentations/SDACS_Design%26Testing_Presentation.pdf' | relative_url }})
- [Node-RED dataset-capture flow (JSON)]({{ '/Node-RED%20Flow/SDACS_flow.json' | relative_url }})
- [Remote Flutter Access and Tailscale Guide (PDF)]({{ '/Documents/SDACS_Remote_Flutter_Access_Tailscale_Guide.pdf' | relative_url }})

### Data and analysis

- [Dataset cleaning and quality report (Markdown)]({{ '/SDACS%20Datasets/SDACS_Edge_Impulse_Ready_Dataset/SDACS_CLEANING_AND_FINALIZATION_REPORT.md' | relative_url }})
- [Feature dictionary (CSV)]({{ '/SDACS%20Datasets/SDACS_Edge_Impulse_Ready_Dataset/feature_dictionary.csv' | relative_url }})
- [Node-level training data (CSV)]({{ '/SDACS%20Datasets/SDACS_Edge_Impulse_Ready_Dataset/sdacs_ei_node_training.csv' | relative_url }}) and [testing data (CSV)]({{ '/SDACS%20Datasets/SDACS_Edge_Impulse_Ready_Dataset/sdacs_ei_node_testing.csv' | relative_url }})
- [Room-fused training data (CSV)]({{ '/SDACS%20Datasets/SDACS_Edge_Impulse_Ready_Dataset/sdacs_ei_room_fused_training.csv' | relative_url }}) and [testing data (CSV)]({{ '/SDACS%20Datasets/SDACS_Edge_Impulse_Ready_Dataset/sdacs_ei_room_fused_testing.csv' | relative_url }})
- [Cleaning audit (CSV)]({{ '/SDACS%20Datasets/SDACS_Edge_Impulse_Ready_Dataset/cleaning_audit.csv' | relative_url }})
- [MATLAB telemetry dataset (CSV)]({{ '/SDACS%20Datasets/MATLAB_Node04_For_Amy/sdacs_matlab_relevant_telemetry.csv' | relative_url }})
- [MATLAB capture summary (CSV)]({{ '/SDACS%20Datasets/MATLAB_Node04_For_Amy/sdacs_capture_summary_for_matlab.csv' | relative_url }})
- [MATLAB dataset guide (PDF)]({{ '/SDACS%20Datasets/MATLAB_Node04_For_Amy/SDACS_MATLAB_Guide_for_Amy_v2.pdf' | relative_url }})

### Related FreqEasy-ML work

These artifacts cover the related acoustic classification extension, including proposals and interim investigations. They do not establish completion of the final trained model or its deployment.

- [FreqEasy-ML proposal (PDF)]({{ '/Documents/Group2_ProjectProposal_updated.pdf' | relative_url }})
- [FreqEasy-ML interim status report (PDF)]({{ '/Documents/KD_Interim_Status_Report.pdf' | relative_url }})
- [FreqEasy machine-learning pipeline diagram]({{ '/Diagrams/FreqEasy_AI-ML_SystemBlockDiagram.png' | relative_url }})
- [TinyML presentation (PDF)]({{ '/Presentations/TINYML%20Presentation.pdf' | relative_url }})

{% comment %}Add reviewed photographs, screenshots or a current project GitHub URL when available. Metadata lives in _data/projects.yml.{% endcomment %}

## Technologies

{% include tags.html items=case_project.technologies %}

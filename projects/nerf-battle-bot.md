---
layout: project
project: nerf-battle-bot
permalink: /projects/nerf-battle-bot/
---
{% assign case_project = site.data.projects | where: "slug", page.project | first %}

## Overview

The Nerf Battle Bot project combined custom electronic hardware, embedded motor control and a Raspberry Pi interface in a mobile robot platform. I designed schematics and PCBs in Altium Designer, assembled boards and developed C firmware. The hardware reports document both functional tests and faults that required rework or an alternative board.

## Design Requirements

The electronics needed to support power distribution, microcontroller interfaces, motor control and communications. DC, stepper and servo motors brought different interface requirements, while the board arrangement needed to accommodate connections between electrical and mechanical subsystems.

## System Architecture

The platform connected embedded control hardware to motors and a Raspberry Pi 3 running Linux. My work spanned the custom boards, firmware and RS232/UART communication between the controller and Raspberry Pi.

The supplied reports cover an early hardware stage. They distinguish the original board design from the configuration used to continue testing after power-board faults.

## PCB Architecture

PCB1 combined power circuitry and motor drivers. PCB2 provided microcontroller and peripheral interfaces, including communications and connections for inputs and outputs.

Separating these functions allowed PCB2 testing to continue using a classmate's PCB1 when my original power board remained faulty. That substitution is part of the documented integration history.

## Schematic Design

I designed power, motor-control, microcontroller and communications circuitry in Altium Designer. The hardware report includes regulator and motor-driver test plans and records checks on power connections and peripheral interfaces.

The debugging work exposed differences between the intended circuit and the assembled board. Missing connections and regulator routing problems required tracing the design through to the physical hardware.

## PCB Layout

I laid out the custom boards and investigated placement and routing issues during assembly and testing. One header arrangement placed keypad and limit-switch connections beneath the STM32 board, obstructing access. The report proposed reversing those headers to restore access.

A missing MCU power connection on PCB2 was bridged with a jumper wire. The reports also record recommendations to revise component placement, routing and via locations in a future PCB1 revision.

## Embedded Firmware

I developed C firmware for DC, stepper and servo motor control and debugged hardware interfaces and motion behaviour. Firmware and hardware testing progressed together as the board configuration changed.

The early hardware report predates completion of the DC-motor and encoder code. Its observations describe that stage of development, while my broader project work also included DC-motor firmware and Raspberry Pi communication.

## Motor Control

The hardware report records successful servo movement with PCB2 connected to the substitute power board. Stepper testing produced shaft twitching, with correction of the motor wiring proposed as the next action.

The original PCB1 motor-driver and power faults prevented a complete successful test of that board. These results guided further debugging rather than establishing that every motor subsystem had passed.

## Raspberry Pi Communication

I implemented RS232/UART communication with a Raspberry Pi 3 running Linux. This work connected the embedded controller to the higher-level system interface.

The linked early reports defer RS232 testing to a later semester. They support the board design and bring-up history, but do not document the later communication validation.

## Board Bring-up and Debugging

Assembly included solder-paste application, SMD placement, reflow and through-hole soldering. I used laboratory test equipment to check continuity, power connections and interface behaviour. X-ray and thermal images helped investigate assembly and regulator problems, with support from classmates and lab staff.

The completed-PCB report records initial success on the 5 V tests and failure on the 3.3 V tests. The later hardware report records continued regulator faults after rework, including trace modifications and a jumper connection. PCB1 remained unsuitable for the intended operation at that stage.

PCB2 testing continued with another student's power board. This allowed parts of the microcontroller and motor interface to be exercised while the original power-board problems remained unresolved.

## System Integration

I worked across electrical, firmware and mechanical interfaces, including board connections, motor wiring and controller communication. The early tests produced a working servo demonstration and identified outstanding power, stepper and DC-motor work.

The reports separate observed behaviour from proposed fixes. They also document where collaboration and substitute hardware were needed to continue testing.

## Supporting Artifacts

{% include documents.html documents=case_project.documents %}

The reports contain assembly photographs, schematic and Altium routing excerpts, X-ray images, thermal inspection evidence and test setups. They are retained as dated engineering records, including unresolved issues.

{% comment %}Add selected PCB photos, schematic exports, board-layout images, later motor/RS232 results and a project GitHub URL when supplied. Avoid treating proposed fixes in the early reports as verified outcomes.{% endcomment %}

## Technologies

{% include tags.html items=case_project.technologies %}

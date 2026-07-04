# Forensic USB Triage Collector

## Overview
The **Forensic USB Triage Collector** is a lightweight, automated Python script designed for Digital Forensics and Incident Response (DFIR) investigations. It automates the extraction of historical USB connection data from a live Windows system by securely querying the Windows Registry.

## Forensic Value
During an incident response engagement or digital investigation, identifying unauthorized data exfiltration or malware introduction via removable media is critical. This tool specifically targets the `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR` registry hive to enumerate all USB mass storage devices that have historically been connected to the machine.

**Investigative Integrity:** This script operates in a strict **read-only** capacity. It safely queries the live registry using Python's built-in `winreg` library without making any modifications, preserving the integrity of the digital evidence and adhering to basic Chain of Custody principles.

## Prerequisites
* **Operating System:** Windows 10 / Windows 11 (Requires a local Windows environment to access the registry).
* **Environment:** Python 3.x

## Usage
1. Download or clone this repository to your local Windows forensic environment.
2. Open a Command Prompt or PowerShell terminal.
3. Execute the script:
```bash
python usb_triage.py

```
## Example Output

The script will output an indexed list of every USB storage device historically connected to the machine, including court-ready timestamps, plain-English friendly names, and exact serial numbers.

```text
Extracting Court-Ready USB Evidence...

---------------------------------------------------------------------------
Timestamp    : 2026-05-31 18:10:59
Device Name  : Generic MassStorageClass USB Device
Make/Model   : Disk&Ven_Generic&Prod_MassStorageClass&Rev_1539
Serial Number: 000000001539&0
---------------------------------------------------------------------------
Timestamp    : 2026-05-31 17:26:29
Device Name  : SDXC Card
Make/Model   : Disk&Ven_RSUER&Prod_RTSUERLUN0&Rev_1.00
Serial Number: 0000
---------------------------------------------------------------------------

Finished reading all USB devices.
```

**Robert Turley (Liton)** *Cybersecurity & DFIR Student*

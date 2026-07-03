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

The script will output an indexed list of the Device/Vendor IDs for every USB storage device historically connected to the machine.

```text
[0] Found USB Device: Disk&Ven_SanDisk&Prod_Cruzer_Glide&Rev_1.00
[1] Found USB Device: Disk&Ven_Kingston&Prod_DataTraveler_3.0&Rev_PMAP
[2] Found USB Device: Disk&Ven_WD&Prod_Elements_25A2&Rev_1014

Finished reading all USB devices.
```

## Author

**Liton** *Cybersecurity & DFIR Student*

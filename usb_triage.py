import winreg

# 1. Point to the USBSTOR file
registry_path = "SYSTEM\\CurrentControlSet\\Enum\\USBSTOR"

# 2. Connect to the local machine and open the USB folder
usb_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)

# 3. Start loop for every device logged
i = 0
while True:
    try:
        subkey_name = winreg.EnumKey(usb_key, i)
        print(f"[{i}] Found USB Device: {subkey_name}")
        i += 1
        
    # 4. Stop loop when there are no more devices
    except OSError:
        print("\nFinished reading all USB devices.")
        break
        
# Best practice: close the registry key when done
winreg.CloseKey(usb_key)

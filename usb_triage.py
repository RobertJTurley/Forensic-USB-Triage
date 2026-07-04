import winreg
import datetime

# 1. Point to the master USBSTOR filing cabinet
registry_path = "SYSTEM\\CurrentControlSet\\Enum\\USBSTOR"
usb_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)

print("Extracting Court-Ready USB Evidence...\n")
print("-" * 75)

i = 0
while True:
    try:
        # 2. Grab the Make/Model (The Drawer)
        make_model = winreg.EnumKey(usb_key, i)
        
        # Open the Drawer
        drawer_path = f"{registry_path}\\{make_model}"
        drawer_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, drawer_path)
        
        # --- THE NEW MINI-LOOP (Looking inside the Drawer) ---
        # We use a try/except here because sometimes a device is weird and doesn't have a serial number folder
        try:
            # 3. Grab the Serial Number (The Folder)
            # We use index 0 because it's usually the first and only folder inside
            serial_number = winreg.EnumKey(drawer_key, 0)
            
            # Open the Folder to read its contents
            folder_path = f"{drawer_path}\\{serial_number}"
            folder_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, folder_path)
            
            # 4. Grab the Timestamp (When was the folder last updated?)
            key_info = winreg.QueryInfoKey(folder_key)
            windows_timestamp = key_info[2]
            unix_time = (windows_timestamp / 10000000) - 11644473600
            readable_date = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')

            # 5. Grab the Friendly Name (The Paper inside)
            # We use QueryValueEx to read a specific text value inside the folder
            friendly_name, _ = winreg.QueryValueEx(folder_key, "FriendlyName")
            
            # Close the folder when done
            winreg.CloseKey(folder_key)
            
        except OSError:
            # If there's no serial number or friendly name, just use placeholders
            serial_number = "UNKNOWN_SERIAL"
            friendly_name = "Unknown Device Type"
            readable_date = "UNKNOWN_TIME"
        # -----------------------------------------------------

        # 6. Print the completely bulletproof evidence
        print(f"Timestamp    : {readable_date}")
        print(f"Device Name  : {friendly_name}")
        print(f"Make/Model   : {make_model}")
        print(f"Serial Number: {serial_number}")
        print("-" * 75)
        
        # Close the drawer and move to the next one
        winreg.CloseKey(drawer_key)
        i += 1
        
    except OSError:
        print("\nFinished reading all USB devices.")
        break
        
winreg.CloseKey(usb_key)
input("\nPress Enter to exit...")

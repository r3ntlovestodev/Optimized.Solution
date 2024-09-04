import os
import urllib.request
import shutil

def resize_console():
    try:
        os.system('mode con: cols=80 lines=20')
        os.system('title Optimized.Solution')
    except Exception as e:
        print(f"Error resizing console: {e}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_roblox_installed():
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        if 'RobloxPlayerBeta.exe' in files:
            return True, root
    return False, None

def download_and_replace_json(version_path):
    client_settings_path = os.path.join(version_path, 'ClientSettings')
    if not os.path.exists(client_settings_path):
        os.makedirs(client_settings_path)

    json_url = 'https://raw.githubusercontent.com/r3ntlovestodev/Optimized.Solution/main/ClientAppSettings.json'
    json_path = os.path.join(client_settings_path, 'ClientAppSettings.json')

    try:
        urllib.request.urlretrieve(json_url, json_path)
        print("\n[INFO] ClientAppSettings.json has been successfully installed/replaced.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred while downloading the file: {e}")

def potato_and_replace_json(version_path):
    client_settings_path = os.path.join(version_path, 'ClientSettings')
    if not os.path.exists(client_settings_path):
        os.makedirs(client_settings_path)

    json_url = 'https://raw.githubusercontent.com/r3ntlovestodev/Optimized.Solution/main/ClientStuff/ClientAppSettings.json'
    json_path = os.path.join(client_settings_path, 'ClientAppSettings.json')

    try:
        urllib.request.urlretrieve(json_url, json_path)
        print("\n[INFO] ClientAppSettings.json has been successfully installed/replaced.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred while downloading the file: {e}")

def display_menu():
    clear_console()
    print("\n" + "="*40)
    print(" " * 5 + "Optimized.Solution")
    print("="*40)
    print("[1] Install/Replace ClientAppSettings.json - [Darkgraphics]")
    print("[2] Install/Replace ClientAppSettings.json - [Potatographics]")
    print("[0] Exit")
    print("="*40)

def main():
    resize_console()
    installed, version_path = check_roblox_installed()
    if not installed:
        print("[ERROR] Roblox is not installed on this system.")
        return

    while True:
        display_menu()
        choice = input("type ").strip()

        if choice == '1':
            download_and_replace_json(version_path)
        elif choice == '2':
            potato_and_replace_json(version_path)
        elif choice == '0':
            break
        else:
            print("[WARNING] Invalid option, please try again.")

if __name__ == "__main__":
    main()

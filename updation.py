#!/usr/bin/python3.9

try:
    from pyfiglet import figlet_format
    import os
    import distro

except ImportError:
    print('please install the necessary packages')

""" little script for linux automation using python"""


class Details():

    """ details about the system"""

    def __init__(self):
        print(figlet_format("Welcome to linux script"))
        self.details = input(
        "Do you want to know about your system details (Y/N)")

    def detail_for_user(self):
        """ check user input using if/else"""

        if self.details.lower() == "y":
            return os.uname()
            """ returned details from os.uname() if you want to experience with the module type in linux terminal python3 thn import os ,then type os.name"""
        else:
            print("ok")

    def __str__(self):
        """ strings returning to terminaldata received from detail_for_user return statement"""
        info = self.detail_for_user()
        if info:
            return f"System name = {info.sysname}\n"\
            f"Node name: {info.nodename}\n" \
            f"Release: {info.release}\n" \
            f"Version: {info.version}\n" \
            f"Machine: {info.machine}\n"
        else:
            return "System info is not provided"

class Update():
    """ update script"""

    def __init__(self):
        self.user_input_update = input(
            f"Do You want to update your system Y/N")

    def detect_package_manager(self):
        if self.user_input_update.lower() == "y":
            class SystemUpdater:
                self.dist = distro.id()
                if self.dist in ("ubuntu", "debian"):
                    self.package_manager = "apt"
                elif self.dist in ("centos", "fedora", "rhel"):
                    self.package_manager = "yum"
                elif self.dist in ("arch"):
                    self.package_manager = "pacman"
                else:
                    print("Unsupported Linux distribution.")

    def update_system(self):
        self.detect_package_manager()
        if self.package_manager is None:
            return

        # Update package manager
        if self.package_manager == "apt":
            os.system("sudo apt update")
        elif self.package_manager == "yum":
            os.system("sudo yum update")
        elif self.package_manager == "pacman":
            os.system("sudo pacman -Syu")

        # Upgrade installed packages
        if self.package_manager == "apt":
            os.system("sudo apt upgrade -y")
        elif self.package_manager == "yum":
            os.system("sudo yum upgrade -y")
        elif self.package_manager == "pacman":
            os.system("sudo pacman -Syu")

class Flatpak():
    """ flatpak script """

    def __init__(self):
        pass

class Timer():
    "Chron tab automation for updates"
    pass

def main():
    user_details = Details()
    print(str(user_details))
    linuxupdate = Update()
    linuxupdate.update_system()


if __name__ == "__main__":
    main()
   
    

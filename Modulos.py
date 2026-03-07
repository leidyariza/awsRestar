import os
import subprocess
iOrR = "install"
defaultPackages = "htop curl git"
print("Enter a list of packages to install")
print("The list should be separated by spaces, for example:")
print(" package1 package2 package3")
print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")
packages = input().lower()
if packages == "default":
    packages= defaultPackages
if iOrR == "install":
    os.system("sudo apt-get install " + packages)
    subprocess.run(["sudo", "apt-get", "install"] + packages.split())

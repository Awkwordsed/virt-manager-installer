#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

passwd = input("Enter your password: ")

print("Installing necessary files")
subprocess.call(
    f"echo '{passwd}\n' | sudo -S pacman -S qemu-full libvirt virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat libguestfs --noconfirm",
    shell=True
)

print("enabling and starting libvirtd")
subprocess.call(
    f"echo '{passwd}\n' | sudo -S systemctl enable --now libvirtd && sudo -S systemctl start libvirtd",
    shell=True
)

print("adding you to libvirt group")
subprocess.call(
    f"echo '{passwd}\n' | sudo -S usermod -a -G libvirt $(whoami) && newgrp libvirt",
    shell=True
)

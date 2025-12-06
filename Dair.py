import os
import platform
import socket
import subprocess
import sys
from colorama import init, Fore, Style


init()

def dair_logo_buyuk():
    logo = """
    ██████╗  █████╗ ██╗██████╗ 
    ██╔══██╗██╔══██╗██║██╔══██╗
    ██║  ██║███████║██║██████╔╝
    ██║  ██║██╔══██║██║██╔══██╗
    ██████╔╝██║  ██║██║██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
    """
    print(Fore.YELLOW + Style.BRIGHT + logo + Style.RESET_ALL)
    print(Fore.YELLOW + " " * 15 + "Dijital Arşiv ve İşlem Sistemi" + Style.RESET_ALL)
    print(Fore.RED + "═" * 65 + Style.RESET_ALL)

def ping_target(target):
    # İşletim sisteminin belirlenmesi
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', target]
    
    # Ping komutunu çalıştırma
    return subprocess.call(command) == 0

def scan_tcp_ports(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    
    dair_logo_buyuk()
    
    target = input("Tarama yapmak istediğiniz IP adresini girin: ")
    
    print(f"{target} için ICMP kontrolü yapılıyor...")
    if ping_target(target):
        print(f"{target} aktif.")
    else:
        print(f"{target} aktif değil.")

    # TCP port taraması
    ports = [22, 80, 443]  
    print(f"\n{target} için TCP port taraması yapılıyor...")
    open_ports = scan_tcp_ports(target, ports)

    if open_ports:
        print(f"Açık TCP portları: {open_ports}")
    else:
        print("Hiçbir açık TCP portu bulunamadı.")

if __name__ == "__main__":
    main()

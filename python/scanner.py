import subprocess
import platform
import ipaddress

# Ustaw swoją podsieć (np. 192.168.1.0/24)
network = ipaddress.ip_network("192.168.1.0/24", strict=False)


param = "-n" if platform.system().lower() == "windows" else "-c"

print(f"Skanowanie sieci {network}...\n")

for ip in network.hosts():
    result = subprocess.run(["ping", param, "1", str(ip)],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"🟢 Odpowiada: {ip}")

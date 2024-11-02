import os
import sys

# Set the interface name (e.g., wlan0, eth0)
interface = "wlan0"

# Set the DNS server IP addresses
dns_servers = ["8.8.8.8", "1.1.1.1"]
subnet_mask = "255.255.255.0"
gateway_ip = "192.168.254.254"
# Set the game server IP address (replace with the actual IP address)
game_server_ip = "161.202.206.59"
game_server_port = "10003"  # Fixed typo in variable name

# Set the MTU value (default is 1500)
mtu = 1400

# Set the TCP optimization settings
tcp_optimization_enabled = True
tcp_window_size = "65535"
tcp_mtu_probing = "1"

# Define the IP address (replace with the actual IP address)
ip_address = "192.168.254.10"  # Example IP address, change as needed

# Apply the changes
os.system(f"ip link set {interface} mtu {mtu}")

# Clear the contents of /etc/resolv.conf
os.system("sudo truncate -s 0 /etc/resolv.conf")

# Write new DNS server entries
os.system(f"ip addr add {ip_address}/{subnet_mask} dev {interface}")
os.system(f"ip route add default via {gateway_ip} dev {interface}")
os.system(f"echo 'nameserver {dns_servers[0]}' | sudo tee -a /etc/resolv.conf")
os.system(f"echo 'nameserver {dns_servers[1]}' | sudo tee -a /etc/resolv.conf")

print("Changes applied. Please restart your device and try playing Mobile Legends again.")

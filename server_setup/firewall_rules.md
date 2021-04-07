# Firewall Rules
## IP Table
Check if you can connect to destination first using `telnet`
```bash
telnet dest_ip dest_port
# example: telnet 127.0.0.1. 8080
```

If you cannot connect, you can added the firewall rule to allow the port
```bash
iptables -I INPUT -s <source ip>/16 -p tcp --dport <dest port> -j ACCEPT
# example: iptables -I INPUT -s 192.168.0.0/16 -p tcp --dport 8182 -j ACCEPT
```

For the config to persist after a server restart, you can directly edit the `/etc/sysconfig/iptables` with the following 
```bash
-A INPUT -s 192.168.0.0/16  -p tcp --dport 8182 -j ACCEPT
```
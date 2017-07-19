# mongo
iptables -I INPUT -p tcp --dport 27017 -j DROP
iptables -I INPUT -p tcp --dport 27017 -s 127.0.0.1 -j ACCEPT

# flower
iptables -I INPUT -p tcp --dport 5555 -j DROP
iptables -I INPUT -p tcp --dport 5555 -s 127.0.0.1 -j ACCEPT

# rabbitmq
iptables -I INPUT -p tcp --dport 5672 -j DROP
iptables -I INPUT -p tcp --dport 5672 -s 127.0.0.1 -j ACCEPT

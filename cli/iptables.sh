# mongo
iptables -I INPUT -p tcp --dport 27017 -j DROP
iptables -I INPUT -p tcp --dport 27017 -s 127.0.0.1 -j ACCEPT

# flower
sudo iptables -I INPUT -p tcp --dport 5555 -j DROP
sudo iptables -I INPUT -p tcp --dport 5555 -s 127.0.0.1 -j ACCEPT

# rabbitmq
sudo iptables -I INPUT -p tcp --dport 4369 -j DROP
sudo iptables -I INPUT -p tcp --dport 4369 -s 127.0.0.1 -j ACCEPT

sudo iptables -I INPUT -p tcp --dport 5672 -j DROP
sudo iptables -I INPUT -p tcp --dport 5672 -s 127.0.0.1 -j ACCEPT

sudo iptables -I INPUT -p tcp --dport 25672 -j DROP
sudo iptables -I INPUT -p tcp --dport 25672 -s 127.0.0.1 -j ACCEPT

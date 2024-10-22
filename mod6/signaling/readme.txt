myvenv(myvenv) parjinder@PARJINDERs-MacBook-Pro signaling % ping www.example.com
PING www.example.com (93.184.215.14): 56 data bytes
64 bytes from 93.184.215.14: icmp_seq=0 ttl=55 time=15.745 ms
64 bytes from 93.184.215.14: icmp_seq=1 ttl=55 time=16.082 ms
64 bytes from 93.184.215.14: icmp_seq=2 ttl=55 time=17.185 ms
64 bytes from 93.184.215.14: icmp_seq=3 ttl=55 time=19.140 ms
64 bytes from 93.184.215.14: icmp_seq=4 ttl=55 time=83.122 ms
64 bytes from 93.184.215.14: icmp_seq=5 ttl=55 time=47.061 ms
^C
--- www.example.com ping statistics ---
6 packets transmitted, 6 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 15.745/33.056/83.122/24.954 ms

SIGNINT = ctrl c

myvenv(myvenv) parjinder@PARJINDERs-MacBook-Pro signaling % ping www.example.com
PING www.example.com (93.184.215.14): 56 data bytes
64 bytes from 93.184.215.14: icmp_seq=0 ttl=55 time=17.123 ms
64 bytes from 93.184.215.14: icmp_seq=1 ttl=55 time=22.206 ms
64 bytes from 93.184.215.14: icmp_seq=2 ttl=55 time=20.434 ms
64 bytes from 93.184.215.14: icmp_seq=3 ttl=55 time=16.071 ms
64 bytes from 93.184.215.14: icmp_seq=4 ttl=55 time=17.022 ms
^Z
zsh: suspended  ping www.example.com

SIGSTOP = ctrl z

myvenv(myvenv) parjinder@PARJINDERs-MacBook-Pro signaling % fg
[1]  + continued  ping www.example.com
64 bytes from 93.184.215.14: icmp_seq=5 ttl=55 time=28.229 ms
64 bytes from 93.184.215.14: icmp_seq=6 ttl=55 time=20.533 ms
64 bytes from 93.184.215.14: icmp_seq=7 ttl=55 time=14.546 ms
64 bytes from 93.184.215.14: icmp_seq=8 ttl=55 time=17.783 ms
64 bytes from 93.184.215.14: icmp_seq=9 ttl=55 time=27.901 ms
^C
--- www.example.com ping statistics ---
10 packets transmitted, 10 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 14.546/20.185/28.229/4.499 ms

SIGTERM = kill
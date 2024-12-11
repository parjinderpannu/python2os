import csv

hosts = [['workstation.local', '192.168.0.23'], ['workstation.cloud', '10.2.2.3']]
with open("python/mod2/hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
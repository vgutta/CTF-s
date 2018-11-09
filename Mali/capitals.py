import sys
import socket
import csv
with open('country-list.csv', 'rb') as f:
    reader = csv.reader(f)
    capitals = list(reader)

host = "ec2-18-216-96-228.us-east-2.compute.amazonaws.com"
port = 8000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    country = s.recv(1024).strip()
    print country
    country = country[23:-1]
    if(not country):
        print "failed"
        break
    for i in capitals:
        if(i[0] == country):
            print i[1]
            s.send(i[1])


s.close()


"""
text = sys.stdin.readline()
text1 = 'What is the capital of Palau?'
cuntry = text[23:-1]
print cuntry

#cuntry = "Brunei"
for i in capitals:
    if(i[0] == cuntry):
        print i[1]
    
#print capitals
"""
#python script to look up host names from a file full of IP addresses using socket.gethostbyaddr
#output is a csv file with ip,hostname

import socket
#increase timeout
socket.setdefaulttimeout(5)

outfile = open("full_iplist.csv", 'w')

fname= raw_input("Enter file name containing IP addresses:")

#try to open the file
try:
    fh = open(fname)
except:
   	print 'File not found'
   	exit()

for line in fh:
    #get host name
    ip = line.rstrip()
    #print ip
    try:
        ais = socket.gethostbyaddr(ip.rstrip())
        #print ip, ",", ais[0]
        ippair = ip,",",ais[0]
        str1 = ''.join(ippair)
        print str1
        outfile.write(str1+ "\n")
        
        
    except socket.herror:
        
        noip = ip,",","host uknown"
        str2 = ''.join(noip)
        print str2
        outfile.write(str2+ "\n")
        
outfile.close()
import getpass
import sys
import telnetlib
import socket
from time import gmtime, strftime


def changeTime(ips,usr,passwd):
    tn = telnetlib.Telnet(ips)
    
    tn.read_until("login: ")
    tn.write(usr + "\n")
    
    #if PASSWORD:
    tn.read_until("Password: ")
    tn.write(passwd + "\n")
    
    #tn.write("ls\n")
    #tn.read_until("root> ")
    tn.write("clish"+"\n")
    tn.read_until("root> ")
    
    tn.write("platform management time-services utc set date-and-time "+strftime("%d-%m-%Y,%H:%M:%S", gmtime())+"\n")
    print "-->Time set!"
    #tn.write("platform management time-services utc set offset hours-offset %s minutes-offset %s", offseth, offsetm)
    #tn.write("platform management time-services daylight-savings-time set start-date-month %s start-date-day %s end-date-month %s end-date-day %s offset %s", dst_s_m, dst_s_d, dst_e_m, dst_e_d, dst_offset)

    tn.write("quit\n")
    tn.write("exit\n")
    

    #tn.set_debuglevel(9)
    #print tn.read_all()


#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()
user = ""
password = ""
iplist = open("iplist.txt","r")
for ips in iplist: 
    ip = ips.rstrip('\n')
    print ip
    changeTime(ip,user,password)
    print "->Done!"
    #socket.getaddrinfo(ips[:-1], 21)

#with open('iplist.txt') as temp_file:
 # ips = line.rstrip('\n') for line in temp_file
#for ip in ips: 
 #   changeTime(ip,user,password)

#!/usr/bin/python3
from boofuzz import *
import argparse

def test_connection(target, logger, session, *args, **kwargs):
    try:
        banner = target.recv(1024)
    except:
        exit(1)


def main(ip,port):
    session = Session(
        target=Target(
            connection=SocketConnection(ip, port, proto='tcp')
        ),
    )
    s_initialize(name="Request")
   
    	# This is where we start fuzzing and adjusting parameters
    s_static("LTER")
    s_delim(" ",fuzzable=False)
    s_string("FUZZ",fuzzable=True) 
    s_delim("\r\n",fuzzable=False)
    session.connect(s_get("Request"), callback=test_connection)
    session.fuzz()


if __name__ == "__main__":
    main("192.168.1.116", 9999) 

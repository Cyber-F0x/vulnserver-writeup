#!/usr/bin/python3
from boofuzz import *
import argparse

def test_connection(target, logger, session, *args, **kwargs):
    try:
        banner = target.recv(1024)
    except:
        exit(1)

def main(ip,port,cmd):
    session = Session(
	sleep_time=1,
        target=Target(
            connection=SocketConnection(ip, port, proto='tcp')
        ),
    )
    s_initialize(name="Request")
    with s_block("exploit"): 
        s_static(cmd.upper())
        s_delim(" ",fuzzable=False)
        s_string("FUZZ",fuzzable=True) 
        s_delim("\r\n",fuzzable=False)
    session.connect(s_get("Request"), callback=test_connection)
    session.fuzz()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', required=True, type=int)
    parser.add_argument('--cmd',required=True)
    args = parser.parse_args()
    main(args.host,args.port,args.cmd)   

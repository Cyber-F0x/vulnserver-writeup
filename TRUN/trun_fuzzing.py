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
	sleep_time=1,
        target=Target(
            connection=SocketConnection(ip, port, proto='tcp')
        ),
    )
    s_initialize(name="Request")
    with s_block("exploit"): #Starts a new block for our request
        s_static("TRUN") #s_static tells boofuzz that this value dose not change and to not fuzz it
        s_delim(" ",fuzzable=False)
        s_string("FUZZ",fuzzable=True) #s_string informs boofuzz that this value on the stack can be changed
        s_delim("\r\n",fuzzable=False)

    # Start fuzzing
    session.connect(s_get("Request"), callback=test_connection)
    session.fuzz()


if __name__ == "__main__":
    #Pullin Arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', required=True, type=int)
    args = parser.parse_args()
    main(args.host,args.port)   

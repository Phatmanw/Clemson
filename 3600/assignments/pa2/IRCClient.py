from optparse import OptionParser
from socket import *
import os, sys, threading
import selectors
import logging
import types
from IRCServer import Channel


class IRCClient(object):
    
    def __init__(self, options, run_on_localhost=False):
        # TODO: Initialize any required code here

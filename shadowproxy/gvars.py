import sys
import logging

PACKET_SIZE = 8192
logger = logging.getLogger(__package__)
logger.addHandler(logging.StreamHandler(sys.stdout))
default_ports = {"http": 80, "https": 443, "socks": 8527, "httponly": 80}

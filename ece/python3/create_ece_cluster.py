"""This Python module defines ECE cluster functions

Note:
    All the functions can be invoked from tasks.py (fabric)
    
    Reference:
        - https://www.elastic.co/guide/en/cloud-enterprise/current/create-es-cluster.html
"""
from credentials import get_credentials

import argparse
import requests
import json
import time

# Global vars
user_name = ''
user_token = ''

# Your cluster url
url = "http://ece.cluster.com"
cert = "./certs/cert.pem"

# Define command line parser options
parser = argparse.ArgumentParser()
parser.add_argument("name", help="The cluster name")
parser.add_argument("size", nargs='?', default="dev", help="The cluster size")
parser.add_argument("owner", help="The owner of the cluster")
parser.add_argument("elasversion", help="Elastic search cluster version")


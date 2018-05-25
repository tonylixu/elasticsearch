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
# Optional arguments
parser.add_argument("--debug", help="Debugging mode")
parser.add_argument("--dryrun",
                    help="Do a test run without sending emails",
                    type=int,
                    choices=[0,1])

def get_root_token():
    """Retrieve the user_name and token for a given ECE env
    
    Args:
        N/A
    
    Returns:
        user_name (str): ECE root username
        user_token (str): ECE root token
    """"
    user = get_credentials('ece', 'user')
    token = get_credentials('ece', 'token')
    
    return (user, token)

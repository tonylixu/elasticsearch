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


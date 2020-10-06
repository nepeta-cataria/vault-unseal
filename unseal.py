import json
import logging
import requests
import urllib3
from yaenv.core import Env

env = Env('.env')
VAULT_NODES = json.loads(env['VAULT_NODES'])
KEYS = json.loads(env['KEYS'])

LOG_LEVEL = env['LOG_LEVEL']
logging.basicConfig(
    format=u'%(levelname)-8s [%(asctime)s] %(message)s',
    level=LOG_LEVEL,
    )
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Disable cert check warnings

def unseal(node, keys):
    """ Unseal Vault node """
    for key in keys:
        body = json.dumps({"key": key})
        r = requests.post('{}/v1/sys/unseal'.format(node), data=body, verify=False)
        logging.info(" Unsealing {}".format(node))
        if r.status_code == 200:
            logging.info(" OK ")
        else:
            logging.error(" FAILED ")
            logging.error(r.text)

def check(nodes, keys):
    """ Check Vault seal status """
    for node in nodes:
        logging.debug(" --- Checking {} ---".format(node))
        r = requests.get('{}/v1/sys/health'.format(node), verify=False)
        if r.status_code == 503:
            logging.debug(r.text)
            unseal(node, keys)
        else:
            logging.debug(r.text)

if __name__ == '__main__':
    check(VAULT_NODES, KEYS)

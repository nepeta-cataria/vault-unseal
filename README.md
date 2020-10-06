# Hashicorp Vault Unsealing script

Python script will check if Vault node is sealed, then unseal it.

Makes a request to `/health` page, if node is sealed, then try to unseal it using unseal keys.

## Requirements

- Python 3
- pip3

## Usage

Install python modules

```
$ pip3 install -r requirements.txt
```

Set **Vault node** addresses and **Unseal keys** in `.env` file (as list).

```
VAULT_NODES = '["https://vault-01:8200","https://vault-02:8200"]'
KEYS = '["XXXXXX","XXXXXX"]'
```

Run script

```
$ python3 unseal.py
```
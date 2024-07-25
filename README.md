# onetimesecret-cli

A simple python client to use the onetimesecret API https://onetimesecret.com/docs/api


## Ussage

```
from onetimesecret import OneTimeSecretCli

cli = OneTimeSecretCli(ONETIMESECRET_USER, ONETIMESECRET_KEY)
cli.create_link("secret",  passphrase="yourPassphrase") # return a link like https://onetimesecret.com/secret/xxxxxxxxxxx
print(f"Secret URL: {secret_url}")
```

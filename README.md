# sfu-upass
A utility script for an SFU student to automatically renew their monthly TransLink U-Pass, updated to accommodate SFU's MFA requirements. Written with the Selenium framework.

Currently limited to Chrome, Firefox or Safari browser support.

## Instructions
### 1. Create a config.json file on your machine with your SFU username, password and MFA key.
```json
{
  "username": "username",
  "password": "password",
  "secret_key": "MFA key"
}
```

### 2. Running the script
```shell
python sfu-upass.py [OPTIONS] (Windows)
python-3 sfu-pass.py [OPTIONS] (Unix)

  --browser (chrome, firefox, safari)
     Toggle a specific browser driver for Selenium to use. Defaults to Chrome.
```

# SFUpass
A Selenium application for an SFU student to automatically renew their monthly TransLink U-Pass.
Currently limited to Chrome, Firefox or Safari browser support.

## Instructions
### 1. Create a config.json file on your machine 
Fill in your SFU username, password and MFA secret key, using the format shown in `config.example.json`.
```json
{
  "username": "username",
  "password": "password",
  "secret_key": "MFA key"
}
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```


### 3. Run the U-Pass request automation
```shell
python -m upass --browser BROWSER

  --browser (chrome, firefox, safari)
     Toggle a specific browser driver for Selenium to use. Defaults to Chrome.
```

## Run the tests
### 1. Install dependencies
```bash
pip install -r requirements-dev.txt
```

### 2. Run
```bash
python -m pytest tests
```

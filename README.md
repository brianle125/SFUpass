# SFUpass
Renewing TransLink's U-Pass each month can be a repetitive manual process for full-time SFU students. SFUpass automates the renewal workflow using Python and Selenium, reducing the need for students to navigate the TransLink website and complete the same steps manually. 

Currently limited to Chrome, Firefox and Safari browser support.

## Instructions
### 1. Create a config.json file on your machine in the project root directory 
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
python -m sfupass --browser BROWSER

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

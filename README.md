### Installation
First setup virtual environment
```
virtualenv venv
```
Next, activate virtual environment
```
source venv/bin/activate # For Linux
```
```
.\venv\Script\activate # For Windows
```
Install rasa
```
pip install rasa
```
Install rasa x
```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```
Start project
```
rasa init --no-prompt
```
Start interactive rasa
```
rasa x
```
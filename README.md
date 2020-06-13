![](assets/demo.gif)


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
.\venv\Scripts\activate # For Windows
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

### Run the ChatBot with API
Run the following commands to start the chat api
```
rasa run actions -vv
```
```
rasa run -m models --enable-api --cors "*" -p 5021
```
#### Open the ``home.html`` file to view the Chat UI

## Donation

If this page helps you reduce time to develop, you can buy me a cup of coffee :coffee:

  

[![paypal](https://cdn-images-1.medium.com/max/738/1*G95uyokAH4JC5Ppvx4LmoQ@2x.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZJM97M6KBLHZY)
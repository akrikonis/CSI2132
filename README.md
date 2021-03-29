# CSI2132

Section B04 Group 57 <br>


## Requirements

pip3 install flask <br>
pip3 install psycopg2

## Account Connection (if using PG Admin)

Create .env file in project root <br>
Add the following lines with your credentials: <br>

```
[ACCOUNT] 
user=YOUR USERNAME (the part before @uottawa.ca)
password=YOUR PASSWORD
```

## Running Flask Option 1

export FLASK_APP=app.py <br>
python3 -m flask run         (Or alternatively: flask run)

## Running Flask Option 2

python3 app.py

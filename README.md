# raspberry-pi-bme680-logger
# Bme-680 sensor logger based on raspberry pi 4 with data upload to google sheets using API or to PostgreSQL database





Create table - sql query:

```
CREATE TABLE dane (

id BIGSERIAL NOT NULL PRIMARY KEY,

date TIMESTAMP,

temp REAL,

press REAL,

hum REAL,

gas_res REAL,

CPU REAL);

```

### python 3.7.3
### libs:
- bme680
- google.oauth2 
- psycopg2



Recommended links:
- https://developers.google.com/sheets/api/quickstart/python
- https://developers.google.com/identity/protocols/oauth2/service-account#python

sudo pip3 install bme680

from datetime import datetime,timedelta
from flask import request, json
import jwt

datetimeInt = datetime.utcnow() + timedelta(hours=1)
SECRECT_KEY = 'secret'
ISS = "jobapp.com"
AUD = "webkit"

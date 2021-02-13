import requests
from requests.auth import HTTPBasicAuth
import json



class Mpesa:
    def __init__(self, consumer_key, consumer_secret,callback_url):
        self._consumer_key=consumer_key
        self._consumer_secret=consumer_secret
        self._callback_url=callback_url
        self._accountBalance_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
        self._auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        self._stk_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        self._stkCheck_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query'
        self._c2bRegister_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        self._c2bSimulate_url = " https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
        self._b2c_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
 

    def _getAuthToken(self):
        response= requests.get(self._auth_url, auth=HTTPBasicAuth(self._consumer_key, self._consumer_secret))
        dictionary_response = json.loads(response.text)
        print(dictionary_response["access_token"])
        return dictionary_response["access_token"]


   

    def sktPush(self): 
        _access_token = self._getAuthToken()
        headers = { "Authorization": "Bearer %s" % _access_token }
        request = {
"BusinessShortCode": " ",
"Password": " ",
"Timestamp": " ",
"TransactionType": "CustomerPayBillOnline",
"Amount": " ",
"PartyA": " ",
"PartyB": " ",
"PhoneNumber": " ",
"CallBackURL": self._callback_url,
"AccountReference": " ",
"TransactionDesc": " "
}
        response = requests.post(self._stk_url , json = request, headers=headers)

        print(response.text)
    
    # def stkCheck():


    # def c2bRegister():

    # def c2bTransact():

    # def checkAccountBalance():

    # def b2c():



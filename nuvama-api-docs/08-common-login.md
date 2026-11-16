# Common-Login

User's Phone and Email API

**Create a successful login flow from code would require three things –**

- a. API key – provided by Nuvama
- b. API secret – provided by Nuvama
- c. Request id – Token to be collected post redirection from Login URL using Nuvama credentials. On
  successful authentication, the Request id will be mentioned in the address bar after redirection to the
  Redirect URL (default - https://127.0.0.1/)

## To validate vendor id and password & generate session

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "source": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://emtuat.edelweiss.in/edelmw-eq-uat/accounts/loginvendor/{vendorID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`POST /accounts/loginvendor/{vendorID}`

> Body parameter

```json
{
  "pwd": "string"
}
```

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| vendorID | path | string | true | vendor id of the client (api Key) |
| source | header | string | true | none |
| body | body | [ValidateUidPwdRequest](27-schemas.md#validateuidpwdrequest) | true | none |

> Example responses

> 200 Response

```json
{
  "msg": "string",
  "success": false
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [GnrResDao](27-schemas.md#gnrresdao) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

This operation does not require authentication

## Returns login data for requested request id

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.GetAuthorization(reqId)
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{

}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.GetLoginData()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
JSONObject data = connect.getLoginData();
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "SourceToken": []string{"string"},
        "AppIdKey": []string{"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOjAsImZmIjoiVyIsImJkIjoid2ViLXBjIiwibmJmIjoxNjE2Mzk3NDQxLCJzcmMiOiJlbXRtdyIsImF2IjoiMS4wLjAiLCJhcHBpZCI6IjE2OTExYTA1ZDU4ZTI5YjVmNTMyZTE3MzRkYzQyMjI2IiwiaXNzIjoiZW10IiwiZXhwIjoxNjE2NDM3ODAwLCJpYXQiOjE2MTYzOTc3NDF9.X2L9kMZjK2yzK5wLiOk2gnF73j5q4WnQtAq26W9XFM4"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://emtuat.edelweiss.in/edelmw-eq-uat/accounts/logindata", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`POST /accounts/logindata`

> Body parameter

```json
{
  "reqId": "string"
}
```

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| SourceToken | header | string | true | key obtained from the generate sesion. |
| AppIdKey | header | string | true | key obtained from the generate sesion. |
| body | body | [LoginAuthDataRequestDto](27-schemas.md#loginauthdatarequestdto) | false | none |

> Example responses

> 200 Response

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "auth": "string",
    "lgnData": {
      "accTyp": "EQ",
      "mrgSts": "COMPLETED",
      "othAccDts": {
        "accTyp": "string",
        "isAct": false,
        "isOnline": false,
        "uid": "string"
      },
      "mrgPopUp": false,
      "mrgAccDts": {
        "uids": [
          {
            "accTyp": "string",
            "uid": "string",
            "alwd": false
          }
        ],
        "phNos": [
          "string"
        ],
        "emIds": [
          "string"
        ]
      },
      "prefAccTyp": "string",
      "excs": [
        "string"
      ],
      "dfPrds": {
        "nse": {
          "by": "string",
          "sl": "string"
        },
        "bse": {
          "by": "string",
          "sl": "string"
        },
        "nfo": {
          "by": "string",
          "sl": "string"
        },
        "bfo": {
          "by": "string",
          "sl": "string"
        },
        "cds": {
          "by": "string",
          "sl": "string"
        },
        "mcx": {
          "by": "string",
          "sl": "string"
        },
        "ncdex": {
          "by": "string",
          "sl": "string"
        }
      },
      "dfPrdsMTF": {
        "nse": {
          "by": "string",
          "sl": "string"
        },
        "bse": {
          "by": "string",
          "sl": "string"
        },
        "nfo": {
          "by": "string",
          "sl": "string"
        },
        "bfo": {
          "by": "string",
          "sl": "string"
        },
        "cds": {
          "by": "string",
          "sl": "string"
        },
        "mcx": {
          "by": "string",
          "sl": "string"
        },
        "ncdex": {
          "by": "string",
          "sl": "string"
        }
      },
      "ordTypes": [
        {
          "key": "string",
          "value": "string"
        }
      ],
      "sts": "OK",
      "accs": {
        "eqBrkCode": "string",
        "coBrkCode": "string",
        "eqBrId": "string",
        "coBrId": "string",
        "llt": "string",
        "eqAccID": "string",
        "eqAccName": "string",
        "coAccID": "string",
        "coAccName": "string",
        "uid": "string",
        "eqBrk": "string",
        "coBrk": "string",
        "rstpwd": false,
        "rstusr": false,
        "eqstwt": false,
        "costwt": false,
        "bseMfstwt": false,
        "eqRmRt": "N",
        "eqEmpCat": "string",
        "coEmpCat": "string",
        "eqAlgoClnt": "string",
        "prfId": "string",
        "ucmCd": "string",
        "eqDob": "string",
        "coDob": "string",
        "wtspCnsnt": "string",
        "eml": "string",
        "mfInf": false,
        "cdslEsFlg": false
      },
      "qlist": [
        {
          "idx": "string",
          "ques": "string"
        }
      ],
      "mtf": {
        "sts": "string",
        "popFl": "string"
      },
      "comOpCnst": {
        "sts": "string",
        "popFl": "string"
      },
      "adhrEQ": {
        "rlEDt": "string",
        "rlFl": "string",
        "sts": "string",
        "popFl": "string"
      },
      "adhrCOM": {
        "rlEDt": "string",
        "rlFl": "string",
        "sts": "string",
        "popFl": "string"
      },
      "cnsntLst": [
        {
          "name": "string",
          "accType": "string",
          "mdtry": false
        }
      ],
      "prdcts": {
        "property1": {
          "property1": [
            "string"
          ],
          "property2": [
            "string"
          ]
        },
        "property2": {
          "property1": [
            "string"
          ],
          "property2": [
            "string"
          ]
        }
      },
      "prds": [
        {
          "exc": "string",
          "prd": [
            {
              "prdDpNm": "string",
              "prdVal": "string",
              "validity": [
                {
                  "dpNm": "string",
                  "vaVal": "string"
                }
              ]
            }
          ]
        }
      ],
      "val": [
        {
          "exc": "string",
          "validity": [
            {
              "dpNm": "string",
              "vaVal": "string"
            }
          ]
        }
      ],
      "gtdGtcValDays": "string",
      "mndtryCnsts": [
        {
          "name": "string",
          "accType": "string",
          "mdtry": false
        }
      ],
      "optCnsts": [
        {
          "name": "string",
          "accType": "string",
          "mdtry": false
        }
      ],
      "srcVendor": "string",
      "vndSrc": "string",
      "reqId": "string",
      "url": "string",
      "jsessionId": "string",
      "vndCnstPopUp": false
    },
    "time": "string"
  }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [LoginAuthDataResponse](27-schemas.md#loginauthdataresponse) |
| 222 | Unknown | Request id expired | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

This operation does not require authentication

## logs out user

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.Logout();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
const logout = apiConnect.logout().then(function(result) {

}).catch((err) => {console.log("Error logout",err);throw err});
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
logout = api_connect.Logout()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String logOutResp=connect.logout();
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://emtuat.edelweiss.in/edelmw-eq-uat/accounts/{userID}/logout", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`PUT /account/logoff/{userID}`

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | none |

> Example responses

> 200 Response

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {
    "app": 1,
    "exp": 1624409130279,
    "info": 14,
    "prmBndExp": 1620977715264
  },
  "data": {
    "type": "simpleStatusDao",
    "msg": "You have been logged out successfully."
  },
  "msgID": "060eb842-5bcc-467c-91ba-0fc6b5f9c009",
  "srvTm": 1624421670371
}
```

> default Response

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "error": {
    "actCd": "string",
    "errCd": "string",
    "errMsg": "string"
  }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [LogOutDao](27-schemas.md#logoutdao) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

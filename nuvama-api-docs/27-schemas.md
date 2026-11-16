# Schemas

## Rtype

```json
"PAYOUT"
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | string | false | none | none |

#### Enumerated Values

| Property | Value |
| --- | --- |
| *anonymous* | PAYOUT |
| *anonymous* | PAYIN |

## Action

```json
"BUY"
```

Action to be performed, BUY/SELL

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | string | false | none | Action to be performed, BUY/SELL |

#### Enumerated Values

| Property | Value |
| --- | --- |
| *anonymous* | BUY |
| *anonymous* | SELL |

## OrderType

```json
"LIMIT"
```

Order Type

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | string | false | none | Order Type |

#### Enumerated Values

| Property | Value |
| --- | --- |
| *anonymous* | LIMIT |
| *anonymous* | SL-M |
| *anonymous* | SL |
| *anonymous* | MARKET |

## PrdCode

```json
"CNC"
```

Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | string | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |

#### Enumerated Values

| Property | Value |
| --- | --- |
| *anonymous* | CNC |
| *anonymous* | MIS |
| *anonymous* | NRML |
| *anonymous* | MTF |
| *anonymous* | CO |
| *anonymous* | BO |

## Duration

```json
"DAY"
```

Order validity, DAY/IOC/EOS(for BSE)

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | string | false | none | Order validity, DAY/IOC/EOS(for BSE) |

#### Enumerated Values

| Property | Value |
| --- | --- |
| *anonymous* | DAY |
| *anonymous* | IOC |
| *anonymous* | EOS |

## ValidateUidPwdRequest

```json
{
  "pwd": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| pwd | string | true | none | API secret (password) |

## GnrResDao

```json
{
  "msg": "string",
  "success": false
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| msg | string | false | none | none |
| success | boolean | false | none | none |

## LoginAuthDataRequestDto

```json
{
  "reqId": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| reqId | string | false | none | Request Id (Requests id obtained manually from weblogin) |

## LoginAuthDataResponse

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

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» auth | string | false | none | none |
| »» lgnData | [VerifyAnswersResponseDao](#verifyanswersresponsedao) | false | none | none |
| »» time | string | false | none | none |

## LogOutDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |

## VerifyAnswersResponseDao

```json
{
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
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| accTyp | string | false | none | Account types for which user is logged in to |
| mrgSts | string | false | none | merge status of userID |
| othAccDts | [OtherAccountDetailsResponseObject](#otheraccountdetailsresponseobject) | false | none | none |
| mrgPopUp | boolean | false | none | none |
| mrgAccDts | [MergeAccountDetailsResponseObject](#mergeaccountdetailsresponseobject) | false | none | none |
| prefAccTyp | string | false | none | Field will be sent only when mrg status is completed/Processed. Note : This might be null when status is processed (when userid's are same before merging) |
| excs | [string] | false | none | list of exchanges enabled for the user |
| dfPrds | [DefaultProductTypesObject](#defaultproducttypesobject) | false | none | none |
| dfPrdsMTF | [DefaultProductTypesObject](#defaultproducttypesobject) | false | none | none |
| ordTypes | [[KeyValueResponseObject](#keyvalueresponseobject)] | false | none | List of Order types enabled for the user |
| sts | string | false | none | Is user successfully logged in then status is ok, else if status is invalid_answers then new 2fa questions should be displayed |
| accs | [AccountDetailsResponeObject](#accountdetailsresponeobject) | false | none | none |
| qlist | [[Questions_Response](#questions_response)] | false | none | If user enters invalid answers to 2fa questions. then new set of questions comes under this field |
| mtf | [CommonConsentStatusDao](#commonconsentstatusdao) | false | none | none |
| comOpCnst | [CommonConsentStatusDao](#commonconsentstatusdao) | false | none | none |
| adhrEQ | [AadharStatusDao](#aadharstatusdao) | false | none | none |
| adhrCOM | [AadharStatusDao](#aadharstatusdao) | false | none | none |
| cnsntLst | [[ConsentStatusDao](#consentstatusdao)] | false | none | consent priority List |
| prdcts | object | false | none | none |
| » **additionalProperties** | object | false | none | none |
| »» **additionalProperties** | [string] | false | none | none |
| prds | [[ValidityProductsResponseObject](#validityproductsresponseobject)] | false | none | For every exchange it will give the list of validity based on product |
| val | [[ValidityExchangeObject](#validityexchangeobject)] | false | none | List of validity corresponding to exchange |
| gtdGtcValDays | string | false | none | Validity days for GTC/GTD product |
| mndtryCnsts | [[ConsentStatusDao](#consentstatusdao)] | false | none | Mandatory consent priority List --> Won't be available if there is no mandatory consents (null check required) |
| optCnsts | [[ConsentStatusDao](#consentstatusdao)] | false | none | Optional consent priority List --> Won't be available if there is a mandatory consent and no optional consents (null check required) |
| srcVendor | string | false | none | vendor name |
| vndSrc | string | false | none | vendor source |
| reqId | string | false | none | Toc Login data request id |
| url | string | false | none | Redirect Url |
| jsessionId | string | false | none | none |
| vndCnstPopUp | boolean | false | none | none |

#### Enumerated Values

| Property | Value |
| --- | --- |
| accTyp | EQ |
| accTyp | CO |
| accTyp | COMEQ |
| mrgSts | COMPLETED |
| mrgSts | REQUESTED |
| mrgSts | ONE_ACCOUNT |
| mrgSts | PROCESSED |
| mrgSts | NOT_REQUESTED |
| mrgSts | NOT_ENABLED |
| sts | OK |
| sts | INVALID_ANSWERS |

## OtherAccountDetailsResponseObject

```json
{
  "accTyp": "string",
  "isAct": false,
  "isOnline": false,
  "uid": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| accTyp | string | false | none | none |
| isAct | boolean | false | none | none |
| isOnline | boolean | false | none | none |
| uid | string | false | none | required for activating an account |

## MergeAccountDetailsResponseObject

```json
{
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
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| uids | [[SegmentType](#segmenttype)] | false | none | none |
| phNos | [string] | false | none | none |
| emIds | [string] | false | none | none |

## DefaultProductTypesObject

```json
{
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
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| nse | [BuySellObject](#buysellobject) | false | none | none |
| bse | [BuySellObject](#buysellobject) | false | none | none |
| nfo | [BuySellObject](#buysellobject) | false | none | none |
| bfo | [BuySellObject](#buysellobject) | false | none | none |
| cds | [BuySellObject](#buysellobject) | false | none | none |
| mcx | [BuySellObject](#buysellobject) | false | none | none |
| ncdex | [BuySellObject](#buysellobject) | false | none | none |

## KeyValueResponseObject

```json
{
  "key": "string",
  "value": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| key | string | false | none | none |
| value | string | false | none | none |

## AccountDetailsResponeObject

```json
{
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
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| eqBrkCode | string | false | none | Equity Broker Code of the user |
| coBrkCode | string | false | none | Commodity Broker Code of the user |
| eqBrId | string | false | none | Equity Branch Id of the user |
| coBrId | string | false | none | Commodity Branch Id of the user |
| llt | string | false | none | Last Successful login time |
| eqAccID | string | false | none | Equity Account ID |
| eqAccName | string | false | none | Equity Account name of the user. |
| coAccID | string | false | none | Commodity Account ID |
| coAccName | string | false | none | Equity Account name of the user. |
| uid | string | false | none | User ID |
| eqBrk | string | false | none | Equity Account Broker of the user |
| coBrk | string | false | none | Commodity Account Broker of the user |
| rstpwd | boolean | false | none | reset password flag. If true then user needs to change password. |
| rstusr | boolean | false | none | Change userID flag. If true then user needs to change userid. |
| eqstwt | boolean | false | none | if user accepted Equity consent then it will come as true |
| costwt | boolean | false | none | if user accepted Commodity consent then it will come as true |
| bseMfstwt | boolean | false | none | if user accepted BSE MF Start consent then it will come as true |
| eqRmRt | string | false | none | Equity RM Rating Setting,NA - RM Rating is not enabled, Y - RM Rating is enabled and Show popup just after login, N - RM Rating is enabled and donot show pop up |
| eqEmpCat | string | false | none | Employee Category, if eq account is for employee, otherwise NA |
| coEmpCat | string | false | none | Employee Category, if co account is for employee, otherwise NA |
| eqAlgoClnt | string | false | none | If the client is Algo client |
| prfId | string | false | none | client's profile id |
| ucmCd | string | false | none | client's ucm code |
| eqDob | string | false | none | Client's DOB recorded in Equity Account |
| coDob | string | false | none | Client's DOB recorded in Commodity Account |
| wtspCnsnt | string | false | none | Client's WhatsApp Consent exists or not, true if exists |
| eml | string | false | none | E-mail |
| mfInf | boolean | false | none | MF Infinity flag |
| cdslEsFlg | boolean | false | none | CDSL Easy flag |

#### Enumerated Values

| Property | Value |
| --- | --- |
| eqRmRt | N |
| eqRmRt | Y |
| eqRmRt | NA |

## Questions_Response

```json
{
  "idx": "string",
  "ques": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| idx | string | false | none | Index of the question |
| ques | string | false | none | Question |

## CommonConsentStatusDao

```json
{
  "sts": "string",
  "popFl": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| sts | string | false | none | Status of client's consent |
| popFl | string | false | none | Flag to determine if client's consent is needed |

## AadharStatusDao

```json
{
  "rlEDt": "string",
  "rlFl": "string",
  "sts": "string",
  "popFl": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| rlEDt | string | false | none | Last date of aadhar validation |
| rlFl | string | false | none | To enable remind me later button on popup |
| sts | string | false | none | Status of client's Aadhar validation |
| popFl | string | false | none | Flag to determine if client's Aadhar validation is needed |

## ConsentStatusDao

```json
{
  "name": "string",
  "accType": "string",
  "mdtry": false
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| name | string | false | none | none |
| accType | string | false | none | none |
| mdtry | boolean | false | none | none |

## ValidityProductsResponseObject

```json
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
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | Exchange |
| prd | [[ProductValueResponseObject](#productvalueresponseobject)] | false | none | List of validity based on product |

## ValidityExchangeObject

```json
{
  "exc": "string",
  "validity": [
    {
      "dpNm": "string",
      "vaVal": "string"
    }
  ]
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | none |
| validity | [[ValidityObject](#validityobject)] | false | none | List of validity |

## SegmentType

```json
{
  "accTyp": "string",
  "uid": "string",
  "alwd": false
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| accTyp | string | false | none | none |
| uid | string | false | none | none |
| alwd | boolean | false | none | True -> Allowed to choose as Merge UserID. |

## BuySellObject

```json
{
  "by": "string",
  "sl": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| by | string | false | none | none |
| sl | string | false | none | none |

## ProductValueResponseObject

```json
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
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| prdDpNm | string | false | none | Product Display Name |
| prdVal | string | false | none | Product Value |
| validity | [[ValidityObject](#validityobject)] | false | none | List will contain validity |

## ValidityObject

```json
{
  "dpNm": "string",
  "vaVal": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| dpNm | string | false | none | Validity display name |
| vaVal | string | false | none | Validity value |

## EQBracketExitRequestDao

```json
{
  "nstOrdNo": "string",
  "syomID": "string",
  "sts": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| nstOrdNo | string | false | none | NestOrderNumber |
| syomID | string | false | none | SyOmOrderId for leg orders |
| sts | string | false | none | Status of the Bracket Order |

## CancelTradeDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |
| »» oid | string | false | none | none |

## CancelTradeCoverDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |

## EqOrderDetailsDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "ord": [
      {
        "exc": "string",
        "ordID": "string",
        "nstReqID": "string",
        "trsTyp": "string",
        "symName": "string",
        "scName": "string",
        "prcTF": "string",
        "avgPrc": "string",
        "trgPrc": "string",
        "qtyTF": "string",
        "unFlSz": "string",
        "dsQty": "string",
        "exOID": "string",
        "sts": "string",
        "tim": "string",
        "txt": "string",
        "prcTyp": "string",
        "dur": "string",
        "prdCode": "CNC"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» ord | [[OrderDetailsResponseObject](#orderdetailsresponseobject)] | false | none | none |

## OrderDetailsResponseObject

```json
{
  "exc": "string",
  "ordID": "string",
  "nstReqID": "string",
  "trsTyp": "string",
  "symName": "string",
  "scName": "string",
  "prcTF": "string",
  "avgPrc": "string",
  "trgPrc": "string",
  "qtyTF": "string",
  "unFlSz": "string",
  "dsQty": "string",
  "exOID": "string",
  "sts": "string",
  "tim": "string",
  "txt": "string",
  "prcTyp": "string",
  "dur": "string",
  "prdCode": "CNC"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | Name of the exchange, BSE/NSE/MCX/NCDEX |
| ordID | string | false | none | Order Id |
| nstReqID | string | false | none | none |
| trsTyp | string | false | none | none |
| symName | string | false | none | none |
| scName | string | false | none | none |
| prcTF | string | false | none | none |
| avgPrc | string | false | none | none |
| trgPrc | string | false | none | none |
| qtyTF | string | false | none | none |
| unFlSz | string | false | none | none |
| dsQty | string | false | none | none |
| exOID | string | false | none | none |
| sts | string | false | none | none |
| tim | string | false | none | none |
| txt | string | false | none | none |
| prcTyp | string | false | none | none |
| dur | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |

## EqOrderHistoryDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "hstOrdBk": [
      {
        "exc": "string",
        "ordID": "string",
        "nstReqID": "string",
        "trsTyp": "string",
        "symName": "string",
        "prcTF": "string",
        "avgPrc": "string",
        "trgPrc": "string",
        "qtyTF": "string",
        "unFlSz": "string",
        "dsQty": "string",
        "exOID": "string",
        "sts": "string",
        "rjRsn": "string",
        "ordTyp": "string",
        "dur": "string",
        "prdCode": "CNC",
        "rpTyp": "string",
        "trdSym": "string",
        "cstFirm": "string",
        "flQty": "string",
        "exTimStm": "string",
        "ordSrc": "string",
        "flDtTim": "string",
        "ordGenTyp": "string",
        "ordEntTyp": "string",
        "cta": "string"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» hstOrdBk | [[EqOrderHistoryResponseObject](#eqorderhistoryresponseobject)] | false | none | none |

## EqOrderHistoryResponseObject

```json
{
  "exc": "string",
  "ordID": "string",
  "nstReqID": "string",
  "trsTyp": "string",
  "symName": "string",
  "prcTF": "string",
  "avgPrc": "string",
  "trgPrc": "string",
  "qtyTF": "string",
  "unFlSz": "string",
  "dsQty": "string",
  "exOID": "string",
  "sts": "string",
  "rjRsn": "string",
  "ordTyp": "string",
  "dur": "string",
  "prdCode": "CNC",
  "rpTyp": "string",
  "trdSym": "string",
  "cstFirm": "string",
  "flQty": "string",
  "exTimStm": "string",
  "ordSrc": "string",
  "flDtTim": "string",
  "ordGenTyp": "string",
  "ordEntTyp": "string",
  "cta": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | none |
| ordID | string | false | none | none |
| nstReqID | string | false | none | none |
| trsTyp | string | false | none | none |
| symName | string | false | none | none |
| prcTF | string | false | none | none |
| avgPrc | string | false | none | none |
| trgPrc | string | false | none | none |
| qtyTF | string | false | none | none |
| unFlSz | string | false | none | none |
| dsQty | string | false | none | none |
| exOID | string | false | none | none |
| sts | string | false | none | none |
| rjRsn | string | false | none | none |
| ordTyp | string | false | none | none |
| dur | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| rpTyp | string | false | none | none |
| trdSym | string | false | none | none |
| cstFirm | string | false | none | none |
| flQty | string | false | none | none |
| exTimStm | string | false | none | none |
| ordSrc | string | false | none | none |
| flDtTim | string | false | none | none |
| ordGenTyp | string | false | none | none |
| ordEntTyp | string | false | none | none |
| cta | string | false | none | none |

## EQModifyTradeRequestDao

```json
{
  "trdSym": "string",
  "exc": "string",
  "action": "BUY",
  "dur": "DAY",
  "flQty": "string",
  "ordTyp": "LIMIT",
  "qty": "string",
  "dscQty": "string",
  "mktPro": "string",
  "lmPrc": "string",
  "trgPrc": "string",
  "prdCode": "CNC",
  "dtDays": "string",
  "nstOID": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| trdSym | string | false | none | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| exc | string | false | none | Name of the exchange, BSE/NSE |
| action | [Action](#action) | false | none | Action to be performed, BUY/SELL |
| dur | [Duration](#duration) | false | none | Order validity, DAY/IOC/EOS(for BSE) |
| flQty | string | false | none | Filled Quantity or filled shares. It is mandatory for order modification |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| qty | string | false | none | Quantity of the scrip to transact in multiple of Lot size/Board lot qty |
| dscQty | string | false | none | Disclosed Quantity. |
| mktPro | string | false | none | Market Protection |
| lmPrc | string | false | none | Limit price of scrip in multiple of tick size |
| trgPrc | string | false | none | Trigger Price applicable for SL/SL-M Orders (default 0) |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| dtDays | string | false | none | date in dd/MM/yyyy format |
| nstOID | string | false | none | Nest Order ID .Order number received from Orderbook response. It is mandatory for modifying/cancelling an order |

## ModifyTradeDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |
| »» oid | string | false | none | none |

## EQCancelTradeReq

```json
{
  "nstOID": "string",
  "exc": "string",
  "ordTyp": "LIMIT",
  "prdCode": "CNC"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| nstOID | string | true | none | Nest Order ID .Order number received from Order book response. |
| exc | string | false | none | Name of the exchange, BSE/NSE |
| ordTyp | [OrderType](#ordertype) | true | none | Order Type |
| prdCode | [PrdCode](#prdcode) | true | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |

## HoldingsRMSDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "eqHv": "string",
    "rmsHdg": [
      {
        "asTyp": "string",
        "cpName": "string",
        "dpName": "string",
        "exc": "string",
        "isin": "string",
        "ltSz": "string",
        "ltp": "string",
        "tkSz": "string",
        "trdSym": "string",
        "totalQty": "string",
        "totalVal": "string",
        "sym": "string",
        "cncRmsHdg": {
          "td": "string",
          "hdgVl": "string",
          "clUQty": "string",
          "hdgUQty": "string",
          "usdQty": "string",
          "t1HQty": "string",
          "clQty": "string",
          "qty": "string",
          "pdQty": "string",
          "pdCnt": "string",
          "sym": "string",
          "totQty": "string"
        },
        "mtfRmsHdg": {
          "td": "string",
          "hdgVl": "string",
          "clUQty": "string",
          "hdgUQty": "string",
          "usdQty": "string",
          "t1HQty": "string",
          "clQty": "string",
          "qty": "string",
          "pdQty": "string",
          "pdCnt": "string",
          "sym": "string",
          "totQty": "string"
        }
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» eqHv | string | false | none | none |
| »» rmsHdg | [[CNCMTFHoldingBlock](#cncmtfholdingblock)] | false | none | none |

## CNCMTFHoldingBlock

```json
{
  "asTyp": "string",
  "cpName": "string",
  "dpName": "string",
  "exc": "string",
  "isin": "string",
  "ltSz": "string",
  "ltp": "string",
  "tkSz": "string",
  "trdSym": "string",
  "totalQty": "string",
  "totalVal": "string",
  "sym": "string",
  "cncRmsHdg": {
    "td": "string",
    "hdgVl": "string",
    "clUQty": "string",
    "hdgUQty": "string",
    "usdQty": "string",
    "t1HQty": "string",
    "clQty": "string",
    "qty": "string",
    "pdQty": "string",
    "pdCnt": "string",
    "sym": "string",
    "totQty": "string"
  },
  "mtfRmsHdg": {
    "td": "string",
    "hdgVl": "string",
    "clUQty": "string",
    "hdgUQty": "string",
    "usdQty": "string",
    "t1HQty": "string",
    "clQty": "string",
    "qty": "string",
    "pdQty": "string",
    "pdCnt": "string",
    "sym": "string",
    "totQty": "string"
  }
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| asTyp | string | false | none | none |
| cpName | string | false | none | none |
| dpName | string | false | none | none |
| exc | string | false | none | none |
| isin | string | false | none | none |
| ltSz | string | false | none | none |
| ltp | string | false | none | none |
| tkSz | string | false | none | none |
| trdSym | string | false | none | none |
| totalQty | string | false | none | none |
| totalVal | string | false | none | none |
| sym | string | false | none | none |
| cncRmsHdg | [HoldingRMSObject](#holdingrmsobject) | false | none | none |
| mtfRmsHdg | [HoldingRMSObject](#holdingrmsobject) | false | none | none |

## HoldingRMSObject

```json
{
  "td": "string",
  "hdgVl": "string",
  "clUQty": "string",
  "hdgUQty": "string",
  "usdQty": "string",
  "t1HQty": "string",
  "clQty": "string",
  "qty": "string",
  "pdQty": "string",
  "pdCnt": "string",
  "sym": "string",
  "totQty": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| td | string | false | none | none |
| hdgVl | string | false | none | none |
| clUQty | string | false | none | none |
| hdgUQty | string | false | none | none |
| usdQty | string | false | none | none |
| t1HQty | string | false | none | none |
| clQty | string | false | none | none |
| qty | string | false | none | none |
| pdQty | string | false | none | none |
| pdCnt | string | false | none | none |
| sym | string | false | none | none |
| totQty | string | false | none | none |

## EQLimitsDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "cshAvl": "string",
    "mtmMg": "string",
    "nvl": "string",
    "nvlPer": "string",
    "exp": "string",
    "srtFall": {
      "srtFall": "string",
      "spnSrtFall": "string"
    },
    "mrgAvl": {
      "mrgAvl": "string",
      "dayOpenBal": "string",
      "stkColVal": "string",
      "mfOthColVal": "string",
      "fndAdd": "string",
      "adMrg": "string",
      "notMrg": "string"
    },
    "mrgUtd": {
      "mrgUtd": "string",
      "blkRelDlvry": "string",
      "lvPrdMrg": "string",
      "fnoSpnMrg": "string",
      "fnoExpMrg": "string",
      "spnExpMrg": "string",
      "prmPdRcd": "string",
      "rlPnl": "string",
      "unRlMtm": "string",
      "mf": "string",
      "ipoAmt": "string",
      "fndWthdrwn": "string",
      "ttpv": "string"
    },
    "unPstdChrgs": {
      "ntChrg": "string",
      "ntUnPstdChrg": {
        "subaccode": "string",
        "recorddate": "2019-08-24T14:15:22Z",
        "dpdues": "string",
        "dpcharges": "string",
        "ist": "string",
        "comoshortfall": "string",
        "fnopenality": "string",
        "pisbankbal": "string",
        "wealthpoabal": "string",
        "mtfbal": "string",
        "oth4amt": "string",
        "oth5amt": "string",
        "accode": "string"
      }
    }
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» cshAvl | string | false | none | Cash available |
| »» mtmMg | string | false | none | MtoM Margin |
| »» nvl | string | false | none | nvl value |
| »» nvlPer | string | false | none | nvl Percentage |
| »» exp | string | false | none | Exposure |
| »» srtFall | [ShortFallDao](#shortfalldao) | false | none | Short fall |
| »» mrgAvl | [MarginAvailableDao](#marginavailabledao) | false | none | Margin Available |
| »» mrgUtd | [MarginUtilized](#marginutilized) | false | none | Margin Utilized |
| »» unPstdChrgs | [UnpostedObject](#unpostedobject) | false | none | Unposted Charges |

## ShortFallDao

```json
{
  "srtFall": "string",
  "spnSrtFall": "string"
}
```

Short fall

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| srtFall | string | false | none | Short Fall |
| spnSrtFall | string | false | none | Span Short Fall |

## MarginAvailableDao

```json
{
  "mrgAvl": "string",
  "dayOpenBal": "string",
  "stkColVal": "string",
  "mfOthColVal": "string",
  "fndAdd": "string",
  "adMrg": "string",
  "notMrg": "string"
}
```

Margin Available

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| mrgAvl | string | false | none | Margin Available |
| dayOpenBal | string | false | none | Day Opening Balance (Cash) |
| stkColVal | string | false | none | Stocks Collateral Value |
| mfOthColVal | string | false | none | MF with Other Collateral Value |
| fndAdd | string | false | none | Funds Added |
| adMrg | string | false | none | Adhoc Margin |
| notMrg | string | false | none | Notional Margin |

## MarginUtilized

```json
{
  "mrgUtd": "string",
  "blkRelDlvry": "string",
  "lvPrdMrg": "string",
  "fnoSpnMrg": "string",
  "fnoExpMrg": "string",
  "spnExpMrg": "string",
  "prmPdRcd": "string",
  "rlPnl": "string",
  "unRlMtm": "string",
  "mf": "string",
  "ipoAmt": "string",
  "fndWthdrwn": "string",
  "ttpv": "string"
}
```

Margin Utilized

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| mrgUtd | string | false | none | Margin Utilized |
| blkRelDlvry | string | false | none | Blocked (+) / Released (-) For Delivery |
| lvPrdMrg | string | false | none | Leveraged Product Margin (Cash Segment) |
| fnoSpnMrg | string | false | none | Span Margin |
| fnoExpMrg | string | false | none | Exposure Margin |
| spnExpMrg | string | false | none | Spand and Exposure Margin |
| prmPdRcd | string | false | none | Premium Paid (+) / Received (-) |
| rlPnl | string | false | none | Realized PnL Value |
| unRlMtm | string | false | none | Unrealized Mark to Market |
| mf | string | false | none | Mutual Funds |
| ipoAmt | string | false | none | IPO / Bonds / NCDs / ETC.. |
| fndWthdrwn | string | false | none | Funds Withdrawn |
| ttpv | string | false | none | Total Third party value |

## UnpostedObject

```json
{
  "ntChrg": "string",
  "ntUnPstdChrg": {
    "subaccode": "string",
    "recorddate": "2019-08-24T14:15:22Z",
    "dpdues": "string",
    "dpcharges": "string",
    "ist": "string",
    "comoshortfall": "string",
    "fnopenality": "string",
    "pisbankbal": "string",
    "wealthpoabal": "string",
    "mtfbal": "string",
    "oth4amt": "string",
    "oth5amt": "string",
    "accode": "string"
  }
}
```

Unposted Charges

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| ntChrg | string | false | none | none |
| ntUnPstdChrg | [UnpostedCollectionDao](#unpostedcollectiondao) | false | none | none |

## UnpostedCollectionDao

```json
{
  "subaccode": "string",
  "recorddate": "2019-08-24T14:15:22Z",
  "dpdues": "string",
  "dpcharges": "string",
  "ist": "string",
  "comoshortfall": "string",
  "fnopenality": "string",
  "pisbankbal": "string",
  "wealthpoabal": "string",
  "mtfbal": "string",
  "oth4amt": "string",
  "oth5amt": "string",
  "accode": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| subaccode | string | false | none | none |
| recorddate | string(date-time) | false | none | none |
| dpdues | string | false | none | none |
| dpcharges | string | false | none | none |
| ist | string | false | none | none |
| comoshortfall | string | false | none | none |
| fnopenality | string | false | none | none |
| pisbankbal | string | false | none | none |
| wealthpoabal | string | false | none | none |
| mtfbal | string | false | none | none |
| oth4amt | string | false | none | none |
| oth5amt | string | false | none | none |
| accode | string | false | none | none |

## PositionSquareOffRequestDto

```json
{
  "trdSym": "string",
  "exc": "string",
  "action": "BUY",
  "dur": "DAY",
  "flQty": "string",
  "ordTyp": "LIMIT",
  "qty": "string",
  "dscQty": "string",
  "sym": "string",
  "mktPro": "string",
  "lmPrc": "string",
  "trgPrc": "string",
  "prdCode": "CNC",
  "dtDays": "string",
  "posSqr": "string",
  "minQty": "string",
  "ordSrc": "MOB",
  "vnCode": "string",
  "rmk": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| trdSym | string | false | none | Trading Symbol |
| exc | string | false | none | Exchange |
| action | [Action](#action) | false | none | Action to be performed, BUY/SELL |
| dur | [Duration](#duration) | false | none | Order validity, DAY/IOC/EOS(for BSE) |
| flQty | string | false | none | Filled Quantity or filled shares. It is mandatory for order modification |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| qty | string | false | none | Quantity. |
| dscQty | string | false | none | Disclosed Quantity. |
| sym | string | false | none | Symbol of the contract that is being traded.SYMBOL_EXCHANGE From MW |
| mktPro | string | false | none | Market Protection |
| lmPrc | string | false | none | Limit Price. |
| trgPrc | string | false | none | Trigger Price. |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| dtDays | string | false | none | Date Days |
| posSqr | string | false | none | Position Square Flag |
| minQty | string | false | none | Minimum Quantity |
| ordSrc | string | false | none | Location Indicator |
| vnCode | string | false | none | Vendor Code |
| rmk | string | false | none | Remarks |

#### Enumerated Values

| Property | Value |
| --- | --- |
| ordSrc | MOB |
| ordSrc | WEB |
| ordSrc | XMLAPI |
| ordSrc | TOC |

## PositionSquareOffResponseDto

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "posSqrOffs": [
      {
        "errMsg": "string",
        "errCd": "string",
        "actCd": "string",
        "msg": "string",
        "oid": "string"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» posSqrOffs | [[PositionSquareOffResponseObject](#positionsquareoffresponseobject)] | false | none | none |

## PositionSquareOffResponseObject

```json
{
  "errMsg": "string",
  "errCd": "string",
  "actCd": "string",
  "msg": "string",
  "oid": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| errMsg | string | false | none | none |
| errCd | string | false | none | none |
| actCd | string | false | none | none |
| msg | string | false | none | none |
| oid | string | false | none | none |

## ErrorResponseDao

```json
{
  "errMsg": "string",
  "errCd": "string",
  "actCd": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| errMsg | string | false | none | none |
| errCd | string | false | none | none |
| actCd | string | false | none | none |

## OrderBookResponse

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "ord": [
      {
        "lstPos": 0,
        "stkPrc": "string",
        "isCOSecLeg": "string",
        "dur": "string",
        "vlDt": "string",
        "rcvTim": "string",
        "rcvEpTim": "string",
        "sym": "string",
        "cpName": "string",
        "exit": "string",
        "syomID": "string",
        "exc": "string",
        "ntQty": "string",
        "dpName": "string",
        "cancel": "string",
        "sipID": "string",
        "nstReqID": "string",
        "ordTyp": "LIMIT",
        "qtyUnits": "string",
        "opTyp": "string",
        "trsTyp": "string",
        "srs": "string",
        "reqQty": "string",
        "prdCode": "CNC",
        "ogt": "string",
        "flQty": "string",
        "trdSym": "string",
        "edit": "string",
        "asTyp": "string",
        "trgPrc": "string",
        "avgPrc": "string",
        "dsQty": "string",
        "ordID": "string",
        "sts": "string",
        "dpInsTyp": "string",
        "rjRsn": "string",
        "userID": "string",
        "dpExpDt": "string",
        "ltSz": "string",
        "tkSz": "string",
        "desc": "string",
        "prc": "string",
        "exONo": "string",
        "exp": "string",
        "rcvDt": "string",
        "pdQty": "string",
        "userCmnt": "string",
        "isSL": false,
        "isTgt": false,
        "flId": "string",
        "rmk": "string",
        "boSeqId": "string",
        "epochTim": "string",
        "ordTim": "string",
        "trgId": "string",
        "dpVal": "string",
        "cta": "string",
        "ltp": "string",
        "vndSrc": "string",
        "bsktOrdId": "string",
        "bsktEpch": "string",
        "brkOrd": [
          {
            "flLg": {
              "lstPos": 0,
              "stkPrc": "string",
              "isCOSecLeg": "string",
              "dur": "DAY",
              "vlDt": "string",
              "rcvTim": "string",
              "rcvEpTim": "string",
              "sym": "string",
              "cpName": "string",
              "exit": "string",
              "syomID": "string",
              "exc": "string",
              "ntQty": "string",
              "dpName": "string",
              "cancel": "string",
              "sipID": "string",
              "nstReqID": "string",
              "ordTyp": "LIMIT",
              "qtyUnits": "string",
              "opTyp": "string",
              "trsTyp": "string",
              "srs": "string",
              "reqQty": "string",
              "prdCode": "CNC",
              "ogt": "string",
              "flQty": "string",
              "trdSym": "string",
              "edit": "string",
              "asTyp": "string",
              "trgPrc": "string",
              "avgPrc": "string",
              "dsQty": "string",
              "ordID": "string",
              "sts": "string",
              "dpInsTyp": "string",
              "rjRsn": "string",
              "userID": "string",
              "dpExpDt": "string",
              "ltSz": "string",
              "tkSz": "string",
              "desc": "string",
              "prc": "string",
              "exONo": "string",
              "exp": "string",
              "rcvDt": "string",
              "pdQty": "string",
              "userCmnt": "string",
              "isSL": false,
              "isTgt": false,
              "flId": "string",
              "rmk": "string",
              "boSeqId": "string",
              "epochTim": "string",
              "ordTim": "string",
              "trgId": "string",
              "dpVal": "string",
              "cta": "string",
              "ltp": "string",
              "vndSrc": "string",
              "bsktOrdId": "string",
              "bsktEpch": "string"
            },
            "slLg": {
              "lstPos": 0,
              "stkPrc": "string",
              "isCOSecLeg": "string",
              "dur": "DAY",
              "vlDt": "string",
              "rcvTim": "string",
              "rcvEpTim": "string",
              "sym": "string",
              "cpName": "string",
              "exit": "string",
              "syomID": "string",
              "exc": "string",
              "ntQty": "string",
              "dpName": "string",
              "cancel": "string",
              "sipID": "string",
              "nstReqID": "string",
              "ordTyp": "LIMIT",
              "qtyUnits": "string",
              "opTyp": "string",
              "trsTyp": "string",
              "srs": "string",
              "reqQty": "string",
              "prdCode": "CNC",
              "ogt": "string",
              "flQty": "string",
              "trdSym": "string",
              "edit": "string",
              "asTyp": "string",
              "trgPrc": "string",
              "avgPrc": "string",
              "dsQty": "string",
              "ordID": "string",
              "sts": "string",
              "dpInsTyp": "string",
              "rjRsn": "string",
              "userID": "string",
              "dpExpDt": "string",
              "ltSz": "string",
              "tkSz": "string",
              "desc": "string",
              "prc": "string",
              "exONo": "string",
              "exp": "string",
              "rcvDt": "string",
              "pdQty": "string",
              "userCmnt": "string",
              "isSL": false,
              "isTgt": false,
              "flId": "string",
              "rmk": "string",
              "boSeqId": "string",
              "epochTim": "string",
              "ordTim": "string",
              "trgId": "string",
              "dpVal": "string",
              "cta": "string",
              "ltp": "string",
              "vndSrc": "string",
              "bsktOrdId": "string",
              "bsktEpch": "string"
            },
            "tgtLg": {
              "lstPos": 0,
              "stkPrc": "string",
              "isCOSecLeg": "string",
              "dur": "DAY",
              "vlDt": "string",
              "rcvTim": "string",
              "rcvEpTim": "string",
              "sym": "string",
              "cpName": "string",
              "exit": "string",
              "syomID": "string",
              "exc": "string",
              "ntQty": "string",
              "dpName": "string",
              "cancel": "string",
              "sipID": "string",
              "nstReqID": "string",
              "ordTyp": "LIMIT",
              "qtyUnits": "string",
              "opTyp": "string",
              "trsTyp": "string",
              "srs": "string",
              "reqQty": "string",
              "prdCode": "CNC",
              "ogt": "string",
              "flQty": "string",
              "trdSym": "string",
              "edit": "string",
              "asTyp": "string",
              "trgPrc": "string",
              "avgPrc": "string",
              "dsQty": "string",
              "ordID": "string",
              "sts": "string",
              "dpInsTyp": "string",
              "rjRsn": "string",
              "userID": "string",
              "dpExpDt": "string",
              "ltSz": "string",
              "tkSz": "string",
              "desc": "string",
              "prc": "string",
              "exONo": "string",
              "exp": "string",
              "rcvDt": "string",
              "pdQty": "string",
              "userCmnt": "string",
              "isSL": false,
              "isTgt": false,
              "flId": "string",
              "rmk": "string",
              "boSeqId": "string",
              "epochTim": "string",
              "ordTim": "string",
              "trgId": "string",
              "dpVal": "string",
              "cta": "string",
              "ltp": "string",
              "vndSrc": "string",
              "bsktOrdId": "string",
              "bsktEpch": "string"
            }
          }
        ]
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» ord | [[OrderBookResponseObject](#orderbookresponseobject)] | false | none | none |

## EqTradeBookDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "trade": [
      {
        "ordTim": "string",
        "trdSym": "string",
        "exONo": "string",
        "dpInsTyp": "string",
        "ntPrc": "string",
        "rmk": "string",
        "dpExpDt": "string",
        "ltSz": "string",
        "cpName": "string",
        "prdCode": "CNC",
        "flTim": "string",
        "flDt": "string",
        "flLeg": "string",
        "flID": "string",
        "fldQty": "string",
        "psCnv": "string",
        "qty": "string",
        "rjRsn": "string",
        "opTyp": "string",
        "sym": "string",
        "dpName": "string",
        "ordID": "string",
        "trsTyp": "string",
        "stkPrc": "string",
        "exc": "string",
        "chgP": "string",
        "sts": "string",
        "asTyp": "string",
        "tkSz": "string",
        "ordType": "string",
        "trdID": "string",
        "ltp": "string",
        "flQty": "string",
        "chg": "string",
        "srs": "string",
        "rcvTim": "string",
        "nstReqID": "string",
        "flPrc": "string",
        "exp": "string",
        "qtyUnits": "string",
        "epochTim": "string"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» trade | [[EqTradeBookResponseObject](#eqtradebookresponseobject)] | false | none | none |

## AddPayOutRequest

```json
{
  "seg": "string",
  "bnkName": "string",
  "bnkAccNo": "string",
  "brcName": "string",
  "ifsc": "string",
  "trnsAmt": "string",
  "rmk": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| seg | string | false | none | Segment Name |
| bnkName | string | false | none | Bank Name |
| bnkAccNo | string | false | none | Bank Account Number |
| brcName | string | false | none | Bank Branch Name |
| ifsc | string | false | none | Bank IFSC code |
| trnsAmt | string | false | none | Transaction Ammount |
| rmk | string | false | none | Remarks |

## AddPayOutDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "sts": "string",
    "msg": "string",
    "trnSt": {
      "reqTyp": "string",
      "seg": "string",
      "instNo": "string",
      "dt": "string",
      "tm": "string",
      "trnsAmt": "string",
      "refNo": "string",
      "rmk": "string",
      "bnkName": "string",
      "sts": "string",
      "brcName": "string",
      "bnkAccNo": "string",
      "edit": "string",
      "cancel": "string",
      "verify": "string",
      "ldgrNm": "string",
      "upi": "string",
      "payMd": "string"
    }
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» sts | string | false | none | none |
| »» msg | string | false | none | none |
| »» trnSt | [TransferStatusObject](#transferstatusobject) | false | none | none |

## NetPositionsDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "pos": [
      {
        "sym": "string",
        "ltp": "string",
        "ltt": "string",
        "chg": "string",
        "chgP": "string",
        "exc": "string",
        "vol": "string",
        "dpName": "string",
        "trdSym": "string",
        "asTyp": "string",
        "ltSz": "string",
        "tkSz": "string",
        "dpInsTyp": "string",
        "desc": "string",
        "dpVal": "string",
        "stkPrc": "string",
        "opTyp": "string",
        "exp": "string",
        "dpExpDt": "string",
        "opInt": "string",
        "opIntChg": "string",
        "opIntChgP": "string",
        "spot": "string",
        "rlOvrP": "string",
        "rlCAbs": "string",
        "trsTyp": "string",
        "prdCode": "CNC",
        "avgSlPrc": "string",
        "avgByPrc": "string",
        "byAmt": "string",
        "byQty": "string",
        "slAmt": "string",
        "slQty": "string",
        "ntQty": "string",
        "ntAmt": "string",
        "rlzPL": "string",
        "urlzPL": "string",
        "ntPL": "string",
        "mtm": "string",
        "prc": "string",
        "sqOff": "string",
        "mul": "string",
        "cpName": "string",
        "rchFlg": "string",
        "nwsFlg": "string",
        "cfAvgSlPrc": "string",
        "cfAvgByPrc": "string",
        "cfSlQty": "string",
        "cfByQty": "string",
        "cfSlAmt": "string",
        "cfByAmt": "string",
        "ntSlQty": "string",
        "ntByQty": "string",
        "ntSlAmt": "string",
        "ntByAmt": "string",
        "brkEvnPrc": "string",
        "uniqKey": "string",
        "pn": "string",
        "gn": "string",
        "gd": "string",
        "pd": "string"
      }
    ],
    "ntMTM": "string",
    "tdyMtm": "string",
    "urlMtm": "string",
    "npos": "string",
    "opn": "string",
    "cls": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» pos | [[NetPositionsObject](#netpositionsobject)] | false | none | none |
| »» ntMTM | string | false | none | none |
| »» tdyMtm | string | false | none | none |
| »» urlMtm | string | false | none | none |
| »» npos | string | false | none | none |
| »» opn | string | false | none | none |
| »» cls | string | false | none | none |

## EQPlaceTradeRequestDao

```json
{
  "trdSym": "string",
  "exc": "BSE",
  "action": "BUY",
  "dur": "DAY",
  "flQty": "string",
  "ordTyp": "LIMIT",
  "qty": "string",
  "dscQty": "string",
  "sym": "string",
  "mktPro": "string",
  "lmPrc": "string",
  "trgPrc": "string",
  "prdCode": "CNC",
  "dtDays": "string",
  "posSqr": "string",
  "minQty": "string",
  "ordSrc": "MOB",
  "vnCode": "string",
  "rmk": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| trdSym | string | false | none | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| exc | string | false | none | Name of the exchange, BSE/NSE |
| action | [Action](#action) | false | none | Action to be performed, BUY/SELL |
| dur | [Duration](#duration) | false | none | Order validity, DAY/IOC/EOS(for BSE) |
| flQty | string | false | none | Filled Quantity or filled shares. It is mandatory for order modification |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| qty | string | false | none | Quantity in multiple of Lot size/Board lot qty |
| dscQty | string | false | none | Disclosed Quantity. Quantity to be disclosed publicly while order placement (default 0) |
| sym | string | false | none | Symbol of the contract that is being traded.SYMBOL_EXCHANGE From MW |
| mktPro | string | false | none | Market Protection |
| lmPrc | string | false | none | Limit price of scrip in multiple of tick size |
| trgPrc | string | false | none | Trigger Price applicable for SL/SL-M Orders (default 0) |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| dtDays | string | false | none | Date Days |
| posSqr | string | false | none | Position Square Flag |
| minQty | string | false | none | Minimum Quantity |
| ordSrc | string | false | none | Location Indicator |
| vnCode | string | false | none | Vendor Code |
| rmk | string | false | none | Remarks |

#### Enumerated Values

| Property | Value |
| --- | --- |
| exc | BSE |
| exc | NSE |
| ordSrc | MOB |
| ordSrc | WEB |
| ordSrc | XMLAPI |
| ordSrc | TOC |

## PlaceTradeDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |
| »» oid | string | false | none | none |

## PlaceTradeBaseketDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |

## EQBracketTradeRequestDao

```json
{
  "exc": "string",
  "sym": "string",
  "trnsTyp": "BUY",
  "qty": "string",
  "dur": "DAY",
  "dsQty": "string",
  "prc": "string",
  "trdBsdOn": "LTP",
  "sqOffBsdOn": "Absolute",
  "sqOffVal": "string",
  "slBsdOn": "Absolute",
  "slVal": "string",
  "trlSl": "Y",
  "trlSlVal": "string",
  "ordSrc": "EMT"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | Name of the exchange, BSE/NSE |
| sym | string | false | none | Symbol |
| trnsTyp | [Action](#action) | false | none | Action to be performed, BUY/SELL |
| qty | string | false | none | Quantity of the scrip to transact |
| dur | [Duration](#duration) | false | none | Order validity, DAY/IOC/EOS(for BSE) |
| dsQty | string | false | none | Quantity to be disclosed publicly while order placement (default 0) |
| prc | string | false | none | Price |
| trdBsdOn | string | false | none | Trade Based On, (ATP is optional) |
| sqOffBsdOn | string | false | none | Square Off Based On, (Ticks is optional) |
| sqOffVal | string | false | none | Square Off Value |
| slBsdOn | string | false | none | Stop Loss Based On Absolute/Ticks ,(Ticks is optional) |
| slVal | string | false | none | Stop Loss Value |
| trlSl | string | false | none | Trailing Stop Loss Flag, Y/N (default Y) |
| trlSlVal | string | false | none | Trailing Stop Loss Value, Number (default 1) |
| ordSrc | string | false | none | Location Indicator |

#### Enumerated Values

| Property | Value |
| --- | --- |
| trdBsdOn | LTP |
| trdBsdOn | ATP |
| sqOffBsdOn | Absolute |
| sqOffBsdOn | Ticks |
| slBsdOn | Absolute |
| slBsdOn | Ticks |
| trlSl | Y |
| trlSl | N |
| ordSrc | EMT |
| ordSrc | WEB |
| ordSrc | XMLAPI |
| ordSrc | TOC |
| ordSrc | TX3 |

## EQCancelTradeRequestDao

```json
{
  "nstOID": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| nstOID | string | false | none | Nest Order ID.Order number received from Order book response. It is mandatory for modifying/cancelling an order. |

## BasketOrderRequestDao

```json
{
  "ordLst": [
    {
      "exc": "string",
      "trdSym": "string",
      "action": "BUY",
      "prdCode": "CNC",
      "ordTyp": "LIMIT",
      "dur": "DAY",
      "price": "string",
      "trgPrc": "string",
      "qty": "string",
      "dscQty": "string",
      "gtdDt": "string",
      "rmk": "string",
      "vnCode": "string"
    }
  ],
  "ordSrc": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| ordLst | [[BasketOrder](#basketorder)] | false | none | List of Basket Orders |
| ordSrc | string | false | none | Order Source |

## OrderBookResponseObject

```json
{
  "lstPos": 0,
  "stkPrc": "string",
  "isCOSecLeg": "string",
  "dur": "string",
  "vlDt": "string",
  "rcvTim": "string",
  "rcvEpTim": "string",
  "sym": "string",
  "cpName": "string",
  "exit": "string",
  "syomID": "string",
  "exc": "string",
  "ntQty": "string",
  "dpName": "string",
  "cancel": "string",
  "sipID": "string",
  "nstReqID": "string",
  "ordTyp": "LIMIT",
  "qtyUnits": "string",
  "opTyp": "string",
  "trsTyp": "string",
  "srs": "string",
  "reqQty": "string",
  "prdCode": "CNC",
  "ogt": "string",
  "flQty": "string",
  "trdSym": "string",
  "edit": "string",
  "asTyp": "string",
  "trgPrc": "string",
  "avgPrc": "string",
  "dsQty": "string",
  "ordID": "string",
  "sts": "string",
  "dpInsTyp": "string",
  "rjRsn": "string",
  "userID": "string",
  "dpExpDt": "string",
  "ltSz": "string",
  "tkSz": "string",
  "desc": "string",
  "prc": "string",
  "exONo": "string",
  "exp": "string",
  "rcvDt": "string",
  "pdQty": "string",
  "userCmnt": "string",
  "isSL": false,
  "isTgt": false,
  "flId": "string",
  "rmk": "string",
  "boSeqId": "string",
  "epochTim": "string",
  "ordTim": "string",
  "trgId": "string",
  "dpVal": "string",
  "cta": "string",
  "ltp": "string",
  "vndSrc": "string",
  "bsktOrdId": "string",
  "bsktEpch": "string",
  "brkOrd": [
    {
      "flLg": {
        "lstPos": 0,
        "stkPrc": "string",
        "isCOSecLeg": "string",
        "dur": "DAY",
        "vlDt": "string",
        "rcvTim": "string",
        "rcvEpTim": "string",
        "sym": "string",
        "cpName": "string",
        "exit": "string",
        "syomID": "string",
        "exc": "string",
        "ntQty": "string",
        "dpName": "string",
        "cancel": "string",
        "sipID": "string",
        "nstReqID": "string",
        "ordTyp": "LIMIT",
        "qtyUnits": "string",
        "opTyp": "string",
        "trsTyp": "string",
        "srs": "string",
        "reqQty": "string",
        "prdCode": "CNC",
        "ogt": "string",
        "flQty": "string",
        "trdSym": "string",
        "edit": "string",
        "asTyp": "string",
        "trgPrc": "string",
        "avgPrc": "string",
        "dsQty": "string",
        "ordID": "string",
        "sts": "string",
        "dpInsTyp": "string",
        "rjRsn": "string",
        "userID": "string",
        "dpExpDt": "string",
        "ltSz": "string",
        "tkSz": "string",
        "desc": "string",
        "prc": "string",
        "exONo": "string",
        "exp": "string",
        "rcvDt": "string",
        "pdQty": "string",
        "userCmnt": "string",
        "isSL": false,
        "isTgt": false,
        "flId": "string",
        "rmk": "string",
        "boSeqId": "string",
        "epochTim": "string",
        "ordTim": "string",
        "trgId": "string",
        "dpVal": "string",
        "cta": "string",
        "ltp": "string",
        "vndSrc": "string",
        "bsktOrdId": "string",
        "bsktEpch": "string"
      },
      "slLg": {
        "lstPos": 0,
        "stkPrc": "string",
        "isCOSecLeg": "string",
        "dur": "DAY",
        "vlDt": "string",
        "rcvTim": "string",
        "rcvEpTim": "string",
        "sym": "string",
        "cpName": "string",
        "exit": "string",
        "syomID": "string",
        "exc": "string",
        "ntQty": "string",
        "dpName": "string",
        "cancel": "string",
        "sipID": "string",
        "nstReqID": "string",
        "ordTyp": "LIMIT",
        "qtyUnits": "string",
        "opTyp": "string",
        "trsTyp": "string",
        "srs": "string",
        "reqQty": "string",
        "prdCode": "CNC",
        "ogt": "string",
        "flQty": "string",
        "trdSym": "string",
        "edit": "string",
        "asTyp": "string",
        "trgPrc": "string",
        "avgPrc": "string",
        "dsQty": "string",
        "ordID": "string",
        "sts": "string",
        "dpInsTyp": "string",
        "rjRsn": "string",
        "userID": "string",
        "dpExpDt": "string",
        "ltSz": "string",
        "tkSz": "string",
        "desc": "string",
        "prc": "string",
        "exONo": "string",
        "exp": "string",
        "rcvDt": "string",
        "pdQty": "string",
        "userCmnt": "string",
        "isSL": false,
        "isTgt": false,
        "flId": "string",
        "rmk": "string",
        "boSeqId": "string",
        "epochTim": "string",
        "ordTim": "string",
        "trgId": "string",
        "dpVal": "string",
        "cta": "string",
        "ltp": "string",
        "vndSrc": "string",
        "bsktOrdId": "string",
        "bsktEpch": "string"
      },
      "tgtLg": {
        "lstPos": 0,
        "stkPrc": "string",
        "isCOSecLeg": "string",
        "dur": "DAY",
        "vlDt": "string",
        "rcvTim": "string",
        "rcvEpTim": "string",
        "sym": "string",
        "cpName": "string",
        "exit": "string",
        "syomID": "string",
        "exc": "string",
        "ntQty": "string",
        "dpName": "string",
        "cancel": "string",
        "sipID": "string",
        "nstReqID": "string",
        "ordTyp": "LIMIT",
        "qtyUnits": "string",
        "opTyp": "string",
        "trsTyp": "string",
        "srs": "string",
        "reqQty": "string",
        "prdCode": "CNC",
        "ogt": "string",
        "flQty": "string",
        "trdSym": "string",
        "edit": "string",
        "asTyp": "string",
        "trgPrc": "string",
        "avgPrc": "string",
        "dsQty": "string",
        "ordID": "string",
        "sts": "string",
        "dpInsTyp": "string",
        "rjRsn": "string",
        "userID": "string",
        "dpExpDt": "string",
        "ltSz": "string",
        "tkSz": "string",
        "desc": "string",
        "prc": "string",
        "exONo": "string",
        "exp": "string",
        "rcvDt": "string",
        "pdQty": "string",
        "userCmnt": "string",
        "isSL": false,
        "isTgt": false,
        "flId": "string",
        "rmk": "string",
        "boSeqId": "string",
        "epochTim": "string",
        "ordTim": "string",
        "trgId": "string",
        "dpVal": "string",
        "cta": "string",
        "ltp": "string",
        "vndSrc": "string",
        "bsktOrdId": "string",
        "bsktEpch": "string"
      }
    }
  ]
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| lstPos | integer(int32) | false | none | none |
| stkPrc | string | false | none | Strike price |
| isCOSecLeg | string | false | none | Cover Order second leg flag |
| dur | string | false | none | Order Duration DAY/IOC/EOS etc |
| vlDt | string | false | none | Order validity data -GTC/GTD |
| rcvTim | string | false | none | Time |
| rcvEpTim | string | false | none | Epoch time |
| sym | string | false | none | Streaming symbol |
| cpName | string | false | none | Company name |
| exit | string | false | none | Exit flag |
| syomID | string | false | none | Traded order id |
| exc | string | false | none | Exchange |
| ntQty | string | false | none | Net quantity |
| dpName | string | false | none | Display scrip name |
| cancel | string | false | none | Order Cancellatiion flag |
| sipID | string | false | none | SIP Indicator |
| nstReqID | string | false | none | Nest request id |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| qtyUnits | string | false | none | Quantity -- commodity |
| opTyp | string | false | none | Option type |
| trsTyp | string | false | none | Transaction type |
| srs | string | false | none | Series |
| reqQty | string | false | none | Requested quantity - not using |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| ogt | string | false | none | Order generation type |
| flQty | string | false | none | Quantity traded |
| trdSym | string | false | none | Trading symbol |
| edit | string | false | none | Order modification flag |
| asTyp | string | false | none | Asset type |
| trgPrc | string | false | none | Trigger price |
| avgPrc | string | false | none | Average price |
| dsQty | string | false | none | Disclosed quantity |
| ordID | string | false | none | Order number |
| sts | string | false | none | Order Status |
| dpInsTyp | string | false | none | Display instrument type |
| rjRsn | string | false | none | Rejection reason |
| userID | string | false | none | User id |
| dpExpDt | string | false | none | Display expiry date |
| ltSz | string | false | none | Lot size |
| tkSz | string | false | none | Tick size |
| desc | string | false | none | Order description |
| prc | string | false | none | Price |
| exONo | string | false | none | Exchange order number |
| exp | string | false | none | Scrip expiry |
| rcvDt | string | false | none | Order recieved date |
| pdQty | string | false | none | Pending quantity |
| userCmnt | string | false | none | Comment added by user while placing the order |
| isSL | boolean | false | none | Bracket order SL leg flag |
| isTgt | boolean | false | none | Flag for target leg of bracket order |
| flId | string | false | none | Fill id comes when order is traded (fully or partially) |
| rmk | string | false | none | Remark added by the small case user while placing the order |
| boSeqId | string | false | none | Sequence id for bracket order legs |
| epochTim | string | false | none | none |
| ordTim | string | false | none | Time stamp |
| trgId | string | false | none | Trigger ID |
| dpVal | string | false | none | display real scrip name |
| cta | string | false | none | Call to action based on rejection reason |
| ltp | string | false | none | Last Traded Price |
| vndSrc | string | false | none | Order source vendor (value may be null if unavailable) |
| bsktOrdId | string | false | none | Basket Order Id |
| bsktEpch | string | false | none | Basket Order Placement Time |
| brkOrd | [[BracketOrderObject](#bracketorderobject)] | false | none | none |

## EqTradeBookResponseObject

```json
{
  "ordTim": "string",
  "trdSym": "string",
  "exONo": "string",
  "dpInsTyp": "string",
  "ntPrc": "string",
  "rmk": "string",
  "dpExpDt": "string",
  "ltSz": "string",
  "cpName": "string",
  "prdCode": "CNC",
  "flTim": "string",
  "flDt": "string",
  "flLeg": "string",
  "flID": "string",
  "fldQty": "string",
  "psCnv": "string",
  "qty": "string",
  "rjRsn": "string",
  "opTyp": "string",
  "sym": "string",
  "dpName": "string",
  "ordID": "string",
  "trsTyp": "string",
  "stkPrc": "string",
  "exc": "string",
  "chgP": "string",
  "sts": "string",
  "asTyp": "string",
  "tkSz": "string",
  "ordType": "string",
  "trdID": "string",
  "ltp": "string",
  "flQty": "string",
  "chg": "string",
  "srs": "string",
  "rcvTim": "string",
  "nstReqID": "string",
  "flPrc": "string",
  "exp": "string",
  "qtyUnits": "string",
  "epochTim": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| ordTim | string | false | none | none |
| trdSym | string | false | none | none |
| exONo | string | false | none | none |
| dpInsTyp | string | false | none | none |
| ntPrc | string | false | none | none |
| rmk | string | false | none | none |
| dpExpDt | string | false | none | none |
| ltSz | string | false | none | none |
| cpName | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| flTim | string | false | none | none |
| flDt | string | false | none | none |
| flLeg | string | false | none | none |
| flID | string | false | none | none |
| fldQty | string | false | none | none |
| psCnv | string | false | none | none |
| qty | string | false | none | none |
| rjRsn | string | false | none | none |
| opTyp | string | false | none | none |
| sym | string | false | none | none |
| dpName | string | false | none | none |
| ordID | string | false | none | none |
| trsTyp | string | false | none | none |
| stkPrc | string | false | none | none |
| exc | string | false | none | none |
| chgP | string | false | none | none |
| sts | string | false | none | none |
| asTyp | string | false | none | none |
| tkSz | string | false | none | none |
| ordType | string | false | none | none |
| trdID | string | false | none | none |
| ltp | string | false | none | none |
| flQty | string | false | none | none |
| chg | string | false | none | none |
| srs | string | false | none | none |
| rcvTim | string | false | none | none |
| nstReqID | string | false | none | none |
| flPrc | string | false | none | none |
| exp | string | false | none | none |
| qtyUnits | string | false | none | none |
| epochTim | string | false | none | none |

## TransferStatusObject

```json
{
  "reqTyp": "string",
  "seg": "string",
  "instNo": "string",
  "dt": "string",
  "tm": "string",
  "trnsAmt": "string",
  "refNo": "string",
  "rmk": "string",
  "bnkName": "string",
  "sts": "string",
  "brcName": "string",
  "bnkAccNo": "string",
  "edit": "string",
  "cancel": "string",
  "verify": "string",
  "ldgrNm": "string",
  "upi": "string",
  "payMd": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| reqTyp | string | false | none | none |
| seg | string | false | none | none |
| instNo | string | false | none | none |
| dt | string | false | none | none |
| tm | string | false | none | none |
| trnsAmt | string | false | none | none |
| refNo | string | false | none | none |
| rmk | string | false | none | none |
| bnkName | string | false | none | none |
| sts | string | false | none | none |
| brcName | string | false | none | none |
| bnkAccNo | string | false | none | none |
| edit | string | false | none | none |
| cancel | string | false | none | none |
| verify | string | false | none | none |
| ldgrNm | string | false | none | Ledger Name |
| upi | string | false | none | upi used for transfer |
| payMd | string | false | none | Payment Mode - Internet Banking/UPI |

## NetPositionsObject

```json
{
  "sym": "string",
  "ltp": "string",
  "ltt": "string",
  "chg": "string",
  "chgP": "string",
  "exc": "string",
  "vol": "string",
  "dpName": "string",
  "trdSym": "string",
  "asTyp": "string",
  "ltSz": "string",
  "tkSz": "string",
  "dpInsTyp": "string",
  "desc": "string",
  "dpVal": "string",
  "stkPrc": "string",
  "opTyp": "string",
  "exp": "string",
  "dpExpDt": "string",
  "opInt": "string",
  "opIntChg": "string",
  "opIntChgP": "string",
  "spot": "string",
  "rlOvrP": "string",
  "rlCAbs": "string",
  "trsTyp": "string",
  "prdCode": "CNC",
  "avgSlPrc": "string",
  "avgByPrc": "string",
  "byAmt": "string",
  "byQty": "string",
  "slAmt": "string",
  "slQty": "string",
  "ntQty": "string",
  "ntAmt": "string",
  "rlzPL": "string",
  "urlzPL": "string",
  "ntPL": "string",
  "mtm": "string",
  "prc": "string",
  "sqOff": "string",
  "mul": "string",
  "cpName": "string",
  "rchFlg": "string",
  "nwsFlg": "string",
  "cfAvgSlPrc": "string",
  "cfAvgByPrc": "string",
  "cfSlQty": "string",
  "cfByQty": "string",
  "cfSlAmt": "string",
  "cfByAmt": "string",
  "ntSlQty": "string",
  "ntByQty": "string",
  "ntSlAmt": "string",
  "ntByAmt": "string",
  "brkEvnPrc": "string",
  "uniqKey": "string",
  "pn": "string",
  "gn": "string",
  "gd": "string",
  "pd": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| sym | string | false | none | none |
| ltp | string | false | none | none |
| ltt | string | false | none | none |
| chg | string | false | none | none |
| chgP | string | false | none | none |
| exc | string | false | none | none |
| vol | string | false | none | none |
| dpName | string | false | none | none |
| trdSym | string | false | none | none |
| asTyp | string | false | none | none |
| ltSz | string | false | none | none |
| tkSz | string | false | none | none |
| dpInsTyp | string | false | none | none |
| desc | string | false | none | none |
| dpVal | string | false | none | none |
| stkPrc | string | false | none | none |
| opTyp | string | false | none | none |
| exp | string | false | none | none |
| dpExpDt | string | false | none | none |
| opInt | string | false | none | none |
| opIntChg | string | false | none | none |
| opIntChgP | string | false | none | none |
| spot | string | false | none | none |
| rlOvrP | string | false | none | none |
| rlCAbs | string | false | none | none |
| trsTyp | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| avgSlPrc | string | false | none | none |
| avgByPrc | string | false | none | none |
| byAmt | string | false | none | none |
| byQty | string | false | none | none |
| slAmt | string | false | none | none |
| slQty | string | false | none | none |
| ntQty | string | false | none | none |
| ntAmt | string | false | none | none |
| rlzPL | string | false | none | none |
| urlzPL | string | false | none | none |
| ntPL | string | false | none | none |
| mtm | string | false | none | none |
| prc | string | false | none | none |
| sqOff | string | false | none | none |
| mul | string | false | none | none |
| cpName | string | false | none | none |
| rchFlg | string | false | none | none |
| nwsFlg | string | false | none | none |
| cfAvgSlPrc | string | false | none | none |
| cfAvgByPrc | string | false | none | none |
| cfSlQty | string | false | none | none |
| cfByQty | string | false | none | none |
| cfSlAmt | string | false | none | none |
| cfByAmt | string | false | none | none |
| ntSlQty | string | false | none | none |
| ntByQty | string | false | none | none |
| ntSlAmt | string | false | none | none |
| ntByAmt | string | false | none | none |
| brkEvnPrc | string | false | none | none |
| uniqKey | string | false | none | none |
| pn | string | false | none | none |
| gn | string | false | none | none |
| gd | string | false | none | none |
| pd | string | false | none | none |

## BasketOrder

```json
{
  "exc": "string",
  "trdSym": "string",
  "action": "BUY",
  "prdCode": "CNC",
  "ordTyp": "LIMIT",
  "dur": "DAY",
  "price": "string",
  "trgPrc": "string",
  "qty": "string",
  "dscQty": "string",
  "gtdDt": "string",
  "rmk": "string",
  "vnCode": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | Exchange |
| trdSym | string | false | none | Trading Symbol |
| action | [Action](#action) | false | none | Action to be performed, BUY/SELL |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| dur | string | false | none | Order duration / Retention |
| price | string | false | none | Price to fill |
| trgPrc | string | false | none | Trigger Price |
| qty | string | false | none | Quantity |
| dscQty | string | false | none | Disclosed Quantity |
| gtdDt | string | false | none | GTD Date in dd-MM-yyyy Format |
| rmk | string | false | none | Remark |
| vnCode | string | false | none | Vendor code |

#### Enumerated Values

| Property | Value |
| --- | --- |
| dur | DAY |
| dur | IOC |

## BracketOrderObject

```json
{
  "flLg": {
    "lstPos": 0,
    "stkPrc": "string",
    "isCOSecLeg": "string",
    "dur": "DAY",
    "vlDt": "string",
    "rcvTim": "string",
    "rcvEpTim": "string",
    "sym": "string",
    "cpName": "string",
    "exit": "string",
    "syomID": "string",
    "exc": "string",
    "ntQty": "string",
    "dpName": "string",
    "cancel": "string",
    "sipID": "string",
    "nstReqID": "string",
    "ordTyp": "LIMIT",
    "qtyUnits": "string",
    "opTyp": "string",
    "trsTyp": "string",
    "srs": "string",
    "reqQty": "string",
    "prdCode": "CNC",
    "ogt": "string",
    "flQty": "string",
    "trdSym": "string",
    "edit": "string",
    "asTyp": "string",
    "trgPrc": "string",
    "avgPrc": "string",
    "dsQty": "string",
    "ordID": "string",
    "sts": "string",
    "dpInsTyp": "string",
    "rjRsn": "string",
    "userID": "string",
    "dpExpDt": "string",
    "ltSz": "string",
    "tkSz": "string",
    "desc": "string",
    "prc": "string",
    "exONo": "string",
    "exp": "string",
    "rcvDt": "string",
    "pdQty": "string",
    "userCmnt": "string",
    "isSL": false,
    "isTgt": false,
    "flId": "string",
    "rmk": "string",
    "boSeqId": "string",
    "epochTim": "string",
    "ordTim": "string",
    "trgId": "string",
    "dpVal": "string",
    "cta": "string",
    "ltp": "string",
    "vndSrc": "string",
    "bsktOrdId": "string",
    "bsktEpch": "string"
  },
  "slLg": {
    "lstPos": 0,
    "stkPrc": "string",
    "isCOSecLeg": "string",
    "dur": "DAY",
    "vlDt": "string",
    "rcvTim": "string",
    "rcvEpTim": "string",
    "sym": "string",
    "cpName": "string",
    "exit": "string",
    "syomID": "string",
    "exc": "string",
    "ntQty": "string",
    "dpName": "string",
    "cancel": "string",
    "sipID": "string",
    "nstReqID": "string",
    "ordTyp": "LIMIT",
    "qtyUnits": "string",
    "opTyp": "string",
    "trsTyp": "string",
    "srs": "string",
    "reqQty": "string",
    "prdCode": "CNC",
    "ogt": "string",
    "flQty": "string",
    "trdSym": "string",
    "edit": "string",
    "asTyp": "string",
    "trgPrc": "string",
    "avgPrc": "string",
    "dsQty": "string",
    "ordID": "string",
    "sts": "string",
    "dpInsTyp": "string",
    "rjRsn": "string",
    "userID": "string",
    "dpExpDt": "string",
    "ltSz": "string",
    "tkSz": "string",
    "desc": "string",
    "prc": "string",
    "exONo": "string",
    "exp": "string",
    "rcvDt": "string",
    "pdQty": "string",
    "userCmnt": "string",
    "isSL": false,
    "isTgt": false,
    "flId": "string",
    "rmk": "string",
    "boSeqId": "string",
    "epochTim": "string",
    "ordTim": "string",
    "trgId": "string",
    "dpVal": "string",
    "cta": "string",
    "ltp": "string",
    "vndSrc": "string",
    "bsktOrdId": "string",
    "bsktEpch": "string"
  },
  "tgtLg": {
    "lstPos": 0,
    "stkPrc": "string",
    "isCOSecLeg": "string",
    "dur": "DAY",
    "vlDt": "string",
    "rcvTim": "string",
    "rcvEpTim": "string",
    "sym": "string",
    "cpName": "string",
    "exit": "string",
    "syomID": "string",
    "exc": "string",
    "ntQty": "string",
    "dpName": "string",
    "cancel": "string",
    "sipID": "string",
    "nstReqID": "string",
    "ordTyp": "LIMIT",
    "qtyUnits": "string",
    "opTyp": "string",
    "trsTyp": "string",
    "srs": "string",
    "reqQty": "string",
    "prdCode": "CNC",
    "ogt": "string",
    "flQty": "string",
    "trdSym": "string",
    "edit": "string",
    "asTyp": "string",
    "trgPrc": "string",
    "avgPrc": "string",
    "dsQty": "string",
    "ordID": "string",
    "sts": "string",
    "dpInsTyp": "string",
    "rjRsn": "string",
    "userID": "string",
    "dpExpDt": "string",
    "ltSz": "string",
    "tkSz": "string",
    "desc": "string",
    "prc": "string",
    "exONo": "string",
    "exp": "string",
    "rcvDt": "string",
    "pdQty": "string",
    "userCmnt": "string",
    "isSL": false,
    "isTgt": false,
    "flId": "string",
    "rmk": "string",
    "boSeqId": "string",
    "epochTim": "string",
    "ordTim": "string",
    "trgId": "string",
    "dpVal": "string",
    "cta": "string",
    "ltp": "string",
    "vndSrc": "string",
    "bsktOrdId": "string",
    "bsktEpch": "string"
  }
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| flLg | [OrderBookCommonResponseObject](#orderbookcommonresponseobject) | false | none | none |
| slLg | [OrderBookCommonResponseObject](#orderbookcommonresponseobject) | false | none | none |
| tgtLg | [OrderBookCommonResponseObject](#orderbookcommonresponseobject) | false | none | none |

## OrderBookCommonResponseObject

```json
{
  "lstPos": 0,
  "stkPrc": "string",
  "isCOSecLeg": "string",
  "dur": "DAY",
  "vlDt": "string",
  "rcvTim": "string",
  "rcvEpTim": "string",
  "sym": "string",
  "cpName": "string",
  "exit": "string",
  "syomID": "string",
  "exc": "string",
  "ntQty": "string",
  "dpName": "string",
  "cancel": "string",
  "sipID": "string",
  "nstReqID": "string",
  "ordTyp": "LIMIT",
  "qtyUnits": "string",
  "opTyp": "string",
  "trsTyp": "string",
  "srs": "string",
  "reqQty": "string",
  "prdCode": "CNC",
  "ogt": "string",
  "flQty": "string",
  "trdSym": "string",
  "edit": "string",
  "asTyp": "string",
  "trgPrc": "string",
  "avgPrc": "string",
  "dsQty": "string",
  "ordID": "string",
  "sts": "string",
  "dpInsTyp": "string",
  "rjRsn": "string",
  "userID": "string",
  "dpExpDt": "string",
  "ltSz": "string",
  "tkSz": "string",
  "desc": "string",
  "prc": "string",
  "exONo": "string",
  "exp": "string",
  "rcvDt": "string",
  "pdQty": "string",
  "userCmnt": "string",
  "isSL": false,
  "isTgt": false,
  "flId": "string",
  "rmk": "string",
  "boSeqId": "string",
  "epochTim": "string",
  "ordTim": "string",
  "trgId": "string",
  "dpVal": "string",
  "cta": "string",
  "ltp": "string",
  "vndSrc": "string",
  "bsktOrdId": "string",
  "bsktEpch": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| lstPos | integer(int32) | false | none | none |
| stkPrc | string | false | none | Strike price |
| isCOSecLeg | string | false | none | Cover Order second leg flag |
| dur | [Duration](#duration) | false | none | Order validity, DAY/IOC/EOS(for BSE) |
| vlDt | string | false | none | Order validity data -GTC/GTD |
| rcvTim | string | false | none | Time |
| rcvEpTim | string | false | none | Epoch time |
| sym | string | false | none | Streaming symbol |
| cpName | string | false | none | Company name |
| exit | string | false | none | Exit flag |
| syomID | string | false | none | Traded order id |
| exc | string | false | none | Exchange |
| ntQty | string | false | none | Net quantity |
| dpName | string | false | none | Display scrip name |
| cancel | string | false | none | Order Cancellatiion flag |
| sipID | string | false | none | SIP Indicator |
| nstReqID | string | false | none | Nest request id |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| qtyUnits | string | false | none | Quantity -- commodity |
| opTyp | string | false | none | Option type |
| trsTyp | string | false | none | Transaction type |
| srs | string | false | none | Series |
| reqQty | string | false | none | Requested quantity - not using |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| ogt | string | false | none | Order generation type |
| flQty | string | false | none | Quantity traded |
| trdSym | string | false | none | Trading symbol |
| edit | string | false | none | Order modification flag |
| asTyp | string | false | none | Asset type |
| trgPrc | string | false | none | Trigger price |
| avgPrc | string | false | none | Average price |
| dsQty | string | false | none | Disclosed quantity |
| ordID | string | false | none | Order number |
| sts | string | false | none | Order Status |
| dpInsTyp | string | false | none | Display instrument type |
| rjRsn | string | false | none | Rejection reason |
| userID | string | false | none | User id |
| dpExpDt | string | false | none | Display expiry date |
| ltSz | string | false | none | Lot size |
| tkSz | string | false | none | Tick size |
| desc | string | false | none | Order description |
| prc | string | false | none | Price |
| exONo | string | false | none | Exchange order number |
| exp | string | false | none | Scrip expiry |
| rcvDt | string | false | none | Order recieved date |
| pdQty | string | false | none | Pending quantity |
| userCmnt | string | false | none | Comment added by user while placing the order |
| isSL | boolean | false | none | Bracket order SL leg flag |
| isTgt | boolean | false | none | Flag for target leg of bracket order |
| flId | string | false | none | Fill id comes when order is traded (fully or partially) |
| rmk | string | false | none | Remark added by the small case user while placing the order |
| boSeqId | string | false | none | Sequence id for bracket order legs |
| epochTim | string | false | none | none |
| ordTim | string | false | none | Time stamp |
| trgId | string | false | none | Trigger ID |
| dpVal | string | false | none | display real scrip name |
| cta | string | false | none | Call to action based on rejection reason |
| ltp | string | false | none | Last Traded Price |
| vndSrc | string | false | none | Order source vendor (value may be null if unavailable) |
| bsktOrdId | string | false | none | Basket Order Id |
| bsktEpch | string | false | none | Basket Order Placement Time |

## EQConvertPositionReq

```json
{
  "nstOID": "string",
  "flID": "string",
  "prdCodeCh": "CNC",
  "prdCode": "CNC",
  "exc": "string",
  "ordTyp": "LIMIT"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| nstOID | string | false | none | Nest Order ID .Order number received from Order book response. It is mandatory for modifying/cancelling an order |
| flID | string | false | none | Fill Id of the trade obtained from TradeBook API |
| prdCodeCh | string | false | none | New Product code of the trade |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| exc | string | true | none | Name of the exchange, BSE/NSE etc |
| ordTyp | [OrderType](#ordertype) | true | none | Order Type |

#### Enumerated Values

| Property | Value |
| --- | --- |
| prdCodeCh | CNC |
| prdCodeCh | MIS |
| prdCodeCh | NRML |

## EqConvertPositionDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |

## SessionExpired

```json
{
  "config": {},
  "error": {
    "actCd": "string",
    "errCd": "string",
    "errMsg": "Session Expired"
  },
  "msgID": "string",
  "srvTm": 0
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| config | object | false | none | none |
| error | object | false | none | none |
| » actCd | string | false | none | none |
| » errCd | string | false | none | none |
| » errMsg | string | false | none | none |
| msgID | string | false | none | none |
| srvTm | number | false | none | none |

## CommonResponseWrapper

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| appID | string | false | none | unique value internally generated by to identify the device of the source |
| config | object | false | none | none |
| msgID | string | false | none | unique key internally generated for a particular API request/response context |
| srvTm | string | false | none | none |

## CommonErrorResponse

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

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » error | object | false | none | none |
| »» actCd | string | false | none | none |
| »» errCd | string | false | none | none |
| »» errMsg | string | false | none | none |

## TradeRequest

```json
{
  "dur": "DAY",
  "vlDt": "string",
  "sym": "string",
  "lmPrc": "string",
  "ordTyp": "LIMIT",
  "action": "BUY",
  "prdCode": "CNC",
  "exc": "MCX",
  "qty": "string",
  "trdSym": "string",
  "trgPrc": "string",
  "dsQty": "string",
  "rmk": "string",
  "locInd": "MOB",
  "ordSrc": "MOB",
  "vnCode": "string",
  "flQty": "string",
  "nstOID": "string",
  "nstReqID": "string",
  "flID": "string",
  "prdCodeCh": "CNC"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| dur | string | false | none | Order duration / Retention |
| vlDt | string | false | none | Validity Date of order (DD-MM-YYYY) |
| sym | string | false | none | Symbol of the contract that is being traded (SYMBOL_EXCHANGE From MW) |
| lmPrc | string | false | none | Limit Price() |
| ordTyp | [OrderType](#ordertype) | true | none | Order Type |
| action | [Action](#action) | false | none | Action to be performed, BUY/SELL |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| exc | string | true | none | Exchanges |
| qty | string | false | none | Quantity () |
| trdSym | string | false | none | Trading of the contract that is being traded (TRADINGSYMBOL From MW) |
| trgPrc | string | false | none | Trigger Price () |
| dsQty | string | false | none | Disclosed Quantity () |
| rmk | string | false | none | Remarks. Any remarks that you may need to store against an order |
| locInd | string | false | none | Location Indicator |
| ordSrc | string | false | none | Location Indicator |
| vnCode | string | false | none | Vendor Code (NA) |
| flQty | string | false | none | Fill Quantity. . It is mandatory in case of Modify Order |
| nstOID | string | true | none | Nest Order ID.Order number received from Order book response. It is mandatory for modifying/cancelling an order |
| nstReqID | string | false | none | Nest Order Req ID.Order number received from Order book response. It is mandatory for modifying/cancelling an AMO order |
| flID | string | false | none | FILL ID. FILL ID received from Order book response. It is mandatory for position conversion |
| prdCodeCh | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |

#### Enumerated Values

| Property | Value |
| --- | --- |
| dur | DAY |
| dur | IOC |
| dur | GTC |
| dur | GTD |
| dur | GTDys |
| dur | EOS |
| exc | MCX |
| exc | NCDEX |
| locInd | MOB |
| locInd | WEB |
| locInd | TOC |
| ordSrc | MOB |
| ordSrc | WEB |
| ordSrc | XMLAPI |
| ordSrc | TOC |

## ComOrderDetailsDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "ord": [
      {
        "exc": "string",
        "ordID": "string",
        "nstReqID": "string",
        "trsTyp": "string",
        "symName": "string",
        "scName": "string",
        "prcTF": "string",
        "avgPrc": "string",
        "trgPrc": "string",
        "qtyTF": "string",
        "unFlSz": "string",
        "dsQty": "string",
        "exOID": "string",
        "sts": "string",
        "tim": "string",
        "txt": "string",
        "prcTyp": "string",
        "dur": "string",
        "prdCode": "CNC"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» ord | [[ComOrderDetailsResponseObject](#comorderdetailsresponseobject)] | false | none | none |

## ComOrderDetailsResponseObject

```json
{
  "exc": "string",
  "ordID": "string",
  "nstReqID": "string",
  "trsTyp": "string",
  "symName": "string",
  "scName": "string",
  "prcTF": "string",
  "avgPrc": "string",
  "trgPrc": "string",
  "qtyTF": "string",
  "unFlSz": "string",
  "dsQty": "string",
  "exOID": "string",
  "sts": "string",
  "tim": "string",
  "txt": "string",
  "prcTyp": "string",
  "dur": "string",
  "prdCode": "CNC"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | Name of the exchange, BSE/NSE/MCX/NCDEX |
| ordID | string | false | none | Order Id |
| nstReqID | string | false | none | none |
| trsTyp | string | false | none | none |
| symName | string | false | none | none |
| scName | string | false | none | none |
| prcTF | string | false | none | none |
| avgPrc | string | false | none | none |
| trgPrc | string | false | none | none |
| qtyTF | string | false | none | none |
| unFlSz | string | false | none | none |
| dsQty | string | false | none | none |
| exOID | string | false | none | none |
| sts | string | false | none | none |
| tim | string | false | none | none |
| txt | string | false | none | none |
| prcTyp | string | false | none | none |
| dur | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |

## ComOrderHistoryDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "hstOrdBk": [
      {
        "exc": "string",
        "ordID": "string",
        "nstReqID": "string",
        "trsTyp": "string",
        "symName": "string",
        "prcTF": "string",
        "avgPrc": "string",
        "trgPrc": "string",
        "qtyTF": "string",
        "unFlSz": "string",
        "dsQty": "string",
        "exOID": "string",
        "sts": "string",
        "rjRsn": "string",
        "ordTyp": "LIMIT",
        "dur": "string",
        "prdCode": "CNC",
        "rpTyp": "string",
        "trdSym": "string",
        "cstFirm": "string",
        "flQty": "string",
        "exTimStm": "string",
        "ordSrc": "string",
        "flDtTim": "string",
        "ordGenTyp": "string",
        "ordEntTyp": "string"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» hstOrdBk | [[ComOrderHistoryResponseObject](#comorderhistoryresponseobject)] | false | none | none |

## ComOrderHistoryResponseObject

```json
{
  "exc": "string",
  "ordID": "string",
  "nstReqID": "string",
  "trsTyp": "string",
  "symName": "string",
  "prcTF": "string",
  "avgPrc": "string",
  "trgPrc": "string",
  "qtyTF": "string",
  "unFlSz": "string",
  "dsQty": "string",
  "exOID": "string",
  "sts": "string",
  "rjRsn": "string",
  "ordTyp": "LIMIT",
  "dur": "string",
  "prdCode": "CNC",
  "rpTyp": "string",
  "trdSym": "string",
  "cstFirm": "string",
  "flQty": "string",
  "exTimStm": "string",
  "ordSrc": "string",
  "flDtTim": "string",
  "ordGenTyp": "string",
  "ordEntTyp": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | none |
| ordID | string | false | none | none |
| nstReqID | string | false | none | none |
| trsTyp | string | false | none | none |
| symName | string | false | none | none |
| prcTF | string | false | none | none |
| avgPrc | string | false | none | none |
| trgPrc | string | false | none | none |
| qtyTF | string | false | none | none |
| unFlSz | string | false | none | none |
| dsQty | string | false | none | none |
| exOID | string | false | none | none |
| sts | string | false | none | none |
| rjRsn | string | false | none | none |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| dur | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| rpTyp | string | false | none | none |
| trdSym | string | false | none | none |
| cstFirm | string | false | none | none |
| flQty | string | false | none | none |
| exTimStm | string | false | none | none |
| ordSrc | string | false | none | none |
| flDtTim | string | false | none | none |
| ordGenTyp | string | false | none | none |
| ordEntTyp | string | false | none | none |

## ComPortfolioDetailDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "stkLst": [
      {
        "trdSym": "string",
        "sym": "string",
        "asTyp": "string",
        "yrLw": "string",
        "yrH": "string",
        "o": "string",
        "h": "string",
        "l": "string",
        "c": "string",
        "ltp": "string",
        "ltt": "string",
        "altt": "string",
        "lut": "string",
        "atp": "string",
        "bidPr": "string",
        "askPr": "string",
        "vol": "string",
        "loCt": "string",
        "hiCt": "string",
        "chg": "string",
        "chgP": "string",
        "ltSz": "string",
        "tkSz": "string",
        "dpNm": "string",
        "stkPrc": "string",
        "opTyp": "string",
        "exp": "string",
        "desc": "string",
        "exc": "string",
        "brdLotQty": "string",
        "qtyUnits": "string",
        "prcUnits": "string",
        "prcQtn": "string",
        "dpInsTyp": "string",
        "bdSz": "string",
        "akSz": "string",
        "dpExpDt": "string",
        "opInt": "string",
        "opIntChg": "string",
        "opIntChgP": "string",
        "spotSym": "string",
        "spot": "string",
        "spotChg": "string",
        "spotChgP": "string",
        "rlOvrP": "string",
        "rlCAbs": "string",
        "ltTQty": "string",
        "tdrStDt": "string",
        "tdrEndDt": "string",
        "srpStDt": "string",
        "mxLtSz": "string",
        "trdInfoId": [
          "string"
        ],
        "ntByQty": "string",
        "ntSlQty": "string",
        "onewkhi": "string",
        "onewklo": "string",
        "onemnhi": "string",
        "onemnlo": "string",
        "thrmnhi": "string",
        "thrmnlo": "string",
        "alltmhi": "string",
        "alltmlo": "string",
        "askivfut": "string",
        "askivspt": "string",
        "bidivfut": "string",
        "bidivspt": "string",
        "ltpivfut": "string",
        "ltpivspt": "string",
        "ntTrdVal": "string",
        "mns": "string",
        "isMTFEnabled": false,
        "rchFlg": "string",
        "nwsFlg": "string",
        "rlOvrCst": "string",
        "rlOvrCstPrc": "string",
        "rlOvrPrc": "string",
        "bta": "string",
        "pe": "string",
        "mktCap": "string",
        "delta": "string",
        "gamma": "string",
        "theta": "string",
        "vega": "string",
        "idxFutTrdSym": "string",
        "dpVal": "string",
        "pcr": "string",
        "pdVal": "string",
        "bas": "string",
        "qty": "string",
        "avgByPrc": "string",
        "avgSlPrc": "string",
        "urlzPL": "string",
        "dyGn": "string",
        "invVal": "string",
        "ttlPL": "string",
        "dpUnit": "string"
      }
    ],
    "smry": {
      "stkCnt": "string",
      "asOfDt": "string",
      "der": {
        "invVal": "string",
        "curVal": "string",
        "unRlGL": "string",
        "dayGL": "string"
      }
    }
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» stkLst | [[CommPortfolioScrip](#commportfolioscrip)] | false | none | none |
| »» smry | [ComPortfolioSummaryDao](#comportfoliosummarydao) | false | none | none |

## ComPortfolioSummaryDao

```json
{
  "stkCnt": "string",
  "asOfDt": "string",
  "der": {
    "invVal": "string",
    "curVal": "string",
    "unRlGL": "string",
    "dayGL": "string"
  }
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| stkCnt | string | false | none | none |
| asOfDt | string | false | none | none |
| der | [ComPortfolioSummaryDataDao](#comportfoliosummarydatadao) | false | none | none |

## ComPortfolioSummaryDataDao

```json
{
  "invVal": "string",
  "curVal": "string",
  "unRlGL": "string",
  "dayGL": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| invVal | string | false | none | none |
| curVal | string | false | none | none |
| unRlGL | string | false | none | none |
| dayGL | string | false | none | none |

## CommPortfolioScrip

```json
{
  "trdSym": "string",
  "sym": "string",
  "asTyp": "string",
  "yrLw": "string",
  "yrH": "string",
  "o": "string",
  "h": "string",
  "l": "string",
  "c": "string",
  "ltp": "string",
  "ltt": "string",
  "altt": "string",
  "lut": "string",
  "atp": "string",
  "bidPr": "string",
  "askPr": "string",
  "vol": "string",
  "loCt": "string",
  "hiCt": "string",
  "chg": "string",
  "chgP": "string",
  "ltSz": "string",
  "tkSz": "string",
  "dpNm": "string",
  "stkPrc": "string",
  "opTyp": "string",
  "exp": "string",
  "desc": "string",
  "exc": "string",
  "brdLotQty": "string",
  "qtyUnits": "string",
  "prcUnits": "string",
  "prcQtn": "string",
  "dpInsTyp": "string",
  "bdSz": "string",
  "akSz": "string",
  "dpExpDt": "string",
  "opInt": "string",
  "opIntChg": "string",
  "opIntChgP": "string",
  "spotSym": "string",
  "spot": "string",
  "spotChg": "string",
  "spotChgP": "string",
  "rlOvrP": "string",
  "rlCAbs": "string",
  "ltTQty": "string",
  "tdrStDt": "string",
  "tdrEndDt": "string",
  "srpStDt": "string",
  "mxLtSz": "string",
  "trdInfoId": [
    "string"
  ],
  "ntByQty": "string",
  "ntSlQty": "string",
  "onewkhi": "string",
  "onewklo": "string",
  "onemnhi": "string",
  "onemnlo": "string",
  "thrmnhi": "string",
  "thrmnlo": "string",
  "alltmhi": "string",
  "alltmlo": "string",
  "askivfut": "string",
  "askivspt": "string",
  "bidivfut": "string",
  "bidivspt": "string",
  "ltpivfut": "string",
  "ltpivspt": "string",
  "ntTrdVal": "string",
  "mns": "string",
  "isMTFEnabled": false,
  "rchFlg": "string",
  "nwsFlg": "string",
  "rlOvrCst": "string",
  "rlOvrCstPrc": "string",
  "rlOvrPrc": "string",
  "bta": "string",
  "pe": "string",
  "mktCap": "string",
  "delta": "string",
  "gamma": "string",
  "theta": "string",
  "vega": "string",
  "idxFutTrdSym": "string",
  "dpVal": "string",
  "pcr": "string",
  "pdVal": "string",
  "bas": "string",
  "qty": "string",
  "avgByPrc": "string",
  "avgSlPrc": "string",
  "urlzPL": "string",
  "dyGn": "string",
  "invVal": "string",
  "ttlPL": "string",
  "dpUnit": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| trdSym | string | false | none | Trading Symbol |
| sym | string | false | none | Streaming Symbol : unique identifier for MW |
| asTyp | string | false | none | Asset type |
| yrLw | string | false | none | Year low |
| yrH | string | false | none | Year high |
| o | string | false | none | Open price |
| h | string | false | none | Day high |
| l | string | false | none | Day low |
| c | string | false | none | Day close |
| ltp | string | false | none | Last traded price |
| ltt | string | false | none | Last traded time |
| altt | string | false | none | Actual Last traded time |
| lut | string | false | none | Last updated time in Date Format |
| atp | string | false | none | average traded price |
| bidPr | string | false | none | Bid price |
| askPr | string | false | none | Ask price |
| vol | string | false | none | Vol |
| loCt | string | false | none | Lower circuit price |
| hiCt | string | false | none | Higher circuit price |
| chg | string | false | none | change from previous close |
| chgP | string | false | none | change percent from previous close |
| ltSz | string | false | none | Lot size |
| tkSz | string | false | none | Tick size |
| dpNm | string | false | none | Display name |
| stkPrc | string | false | none | Strike price |
| opTyp | string | false | none | Option type |
| exp | string | false | none | Expiry date of contract in milliseconds |
| desc | string | false | none | Description for the scrip / contract |
| exc | string | false | none | Exchange of the scrip / contract |
| brdLotQty | string | false | none | Board lot quantity |
| qtyUnits | string | false | none | Quantity units / deliver units |
| prcUnits | string | false | none | prc units |
| prcQtn | string | false | none | prc units |
| dpInsTyp | string | false | none | Display instrument type |
| bdSz | string | false | none | Bid size |
| akSz | string | false | none | Ask size |
| dpExpDt | string | false | none | Display expiry date |
| opInt | string | false | none | Open interest |
| opIntChg | string | false | none | Change in Open interest |
| opIntChgP | string | false | none | Percentage Change in Open interest |
| spotSym | string | false | none | Spot price of underlying |
| spot | string | false | none | Spot price of underlying |
| spotChg | string | false | none | Spot Change of underlying |
| spotChgP | string | false | none | Spot Change Percent of underlying |
| rlOvrP | string | false | none | Rollover percentage |
| rlCAbs | string | false | none | Absolute Cost for Rollover |
| ltTQty | string | false | none | Last traded quantity |
| tdrStDt | string | false | none | Tender start date in epoch (milliseconds) |
| tdrEndDt | string | false | none | Tender end date in epoch (milliseconds) |
| srpStDt | string | false | none | Scrip start date in epoch (milliseconds) |
| mxLtSz | string | false | none | Max Lot size |
| trdInfoId | [string] | false | none | t2t text info |
| ntByQty | string | false | none | Total Buy Quantity |
| ntSlQty | string | false | none | Total Sell Quantity |
| onewkhi | string | false | none | One Week High |
| onewklo | string | false | none | One Week Low |
| onemnhi | string | false | none | One month high |
| onemnlo | string | false | none | one month low |
| thrmnhi | string | false | none | Three months high |
| thrmnlo | string | false | none | Three months low |
| alltmhi | string | false | none | All time high |
| alltmlo | string | false | none | All time low |
| askivfut | string | false | none | Ask IV for future |
| askivspt | string | false | none | Ask IV for spot |
| bidivfut | string | false | none | Bid IV for future |
| bidivspt | string | false | none | Bid IV for spot |
| ltpivfut | string | false | none | Bid IV for future |
| ltpivspt | string | false | none | Bid IV for spot |
| ntTrdVal | string | false | none | Total traded value |
| mns | string | false | none | Moneyness Type, note:this field might be null as well i.e the key may not come in the response |
| isMTFEnabled | boolean | false | none | MTF flag |
| rchFlg | string | false | none | Research Flag |
| nwsFlg | string | false | none | News Flag |
| rlOvrCst | string | false | none | Roll Over Cost , can be null |
| rlOvrCstPrc | string | false | none | Roll Over Cost Percentage, can be null |
| rlOvrPrc | string | false | none | Roll Over Percentage, can be null |
| bta | string | false | none | Beta Value, can be null |
| pe | string | false | none | PE value for for Equity, can be null |
| mktCap | string | false | none | Market Cap value for Equity, can be null |
| delta | string | false | none | delta |
| gamma | string | false | none | gamma |
| theta | string | false | none | theta |
| vega | string | false | none | vega |
| idxFutTrdSym | string | false | none | Nifty future's nearest expiry trading symbol |
| dpVal | string | false | none | DP Value --> Original symbol-name |
| pcr | string | false | none | PC Ratio |
| pdVal | string | false | none | Prem/Disc Value |
| bas | string | false | none | Prem/Disc |
| qty | string | false | none | none |
| avgByPrc | string | false | none | none |
| avgSlPrc | string | false | none | none |
| urlzPL | string | false | none | none |
| dyGn | string | false | none | none |
| invVal | string | false | none | none |
| ttlPL | string | false | none | none |
| dpUnit | string | false | none | none |

## ComRMSLimitsDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "lmt": {
      "lrB": "string",
      "colVal": "string",
      "piAmt": "string",
      "poAmt": "string",
      "lmAvl": "string",
      "mrUzd": "string"
    }
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» lmt | [ComRMSLimitsObject](#comrmslimitsobject) | false | none | none |

## ComRMSLimitsObject

```json
{
  "lrB": "string",
  "colVal": "string",
  "piAmt": "string",
  "poAmt": "string",
  "lmAvl": "string",
  "mrUzd": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| lrB | string | false | none | none |
| colVal | string | false | none | none |
| piAmt | string | false | none | none |
| poAmt | string | false | none | none |
| lmAvl | string | false | none | none |
| mrUzd | string | false | none | none |

## CommAMODao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "sts": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» sts | string | false | none | none |

## ComOrderBookDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "ord": [
      {
        "exc": "string",
        "ordID": "string",
        "nstReqID": "string",
        "trsTyp": "string",
        "trdSym": "string",
        "sym": "string",
        "srs": "string",
        "cpName": "string",
        "prc": "string",
        "avgPrc": "string",
        "ntQty": "string",
        "dsQty": "string",
        "flQty": "string",
        "trgPrc": "string",
        "exONo": "string",
        "sts": "string",
        "rjRsn": "string",
        "ordTyp": "LIMIT",
        "rcvTim": "string",
        "dur": "string",
        "vlDt": "string",
        "prdCode": "CNC",
        "ogt": "string",
        "sipID": "string",
        "userID": "string",
        "pdQty": "string",
        "desc": "string",
        "dpInsTyp": "string",
        "dpExpDt": "string",
        "stkPrc": "string",
        "opTyp": "string",
        "edit": "string",
        "cancel": "string",
        "exit": "string",
        "asTyp": "string",
        "tkSz": "string",
        "ltSz": "string",
        "isCOSecLeg": "string",
        "exp": "string",
        "dpName": "string",
        "qtyUnits": "string",
        "rcvEpTim": "string",
        "rmk": "string",
        "trgId": "string",
        "userCmnt": "string",
        "cta": "string",
        "ltp": "string"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» ord | [[ComOrderBookResponseObject](#comorderbookresponseobject)] | false | none | none |

## ComTradeBookDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "trade": [
      {
        "exc": "string",
        "ordID": "string",
        "ordTyp": "LIMIT",
        "trsTyp": "string",
        "trdSym": "string",
        "sym": "string",
        "cpName": "string",
        "srs": "string",
        "dsQty": "string",
        "exONo": "string",
        "rcvTim": "string",
        "prdCode": "CNC",
        "flQty": "string",
        "qty": "string",
        "trdID": "string",
        "flPrc": "string",
        "ltp": "string",
        "chg": "string",
        "chgP": "string",
        "asTyp": "string",
        "dpInsTyp": "string",
        "dpExpDt": "string",
        "stkPrc": "string",
        "opTyp": "string",
        "psCnv": "string",
        "ntPrc": "string",
        "sts": "string",
        "tkSz": "string",
        "ltSz": "string",
        "dpName": "string",
        "exp": "string",
        "qtyUnits": "string",
        "rmk": "string"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» trade | [[ComTradeBookResponseObject](#comtradebookresponseobject)] | false | none | none |

## ComPositionBookDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "pos": [
      {
        "exc": "string",
        "trdSym": "string",
        "sym": "string",
        "cpName": "string",
        "byQty": "string",
        "avgByPrc": "string",
        "byAmt": "string",
        "slQty": "string",
        "avgSlPrc": "string",
        "slAmt": "string",
        "ntAmt": "string",
        "ntQty": "string",
        "prdCode": "CNC",
        "rlzPL": "string",
        "urlzPL": "string",
        "mtm": "string",
        "ltp": "string",
        "dpExpDt": "string",
        "brkEvnPrc": "string",
        "dpInsTyp": "string",
        "opTyp": "string",
        "stkPrc": "string",
        "sqOff": "string",
        "asTyp": "string",
        "ntPL": "string",
        "tkSz": "string",
        "ltSz": "string",
        "mul": "string",
        "trsTyp": "string",
        "dpName": "string",
        "prc": "string",
        "rchFlg": "string",
        "nwsFlg": "string",
        "gn": "string",
        "gd": "string",
        "pn": "string",
        "pd": "string"
      }
    ],
    "ntMTM": "string",
    "tdyMtm": "string",
    "urlMtm": "string",
    "npos": "string",
    "opn": "string",
    "cls": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» pos | [[ComPositionBookObject](#compositionbookobject)] | false | none | none |
| »» ntMTM | string | false | none | none |
| »» tdyMtm | string | false | none | none |
| »» urlMtm | string | false | none | none |
| »» npos | string | false | none | none |
| »» opn | string | false | none | none |
| »» cls | string | false | none | none |

## ComOrderBookResponseObject

```json
{
  "exc": "string",
  "ordID": "string",
  "nstReqID": "string",
  "trsTyp": "string",
  "trdSym": "string",
  "sym": "string",
  "srs": "string",
  "cpName": "string",
  "prc": "string",
  "avgPrc": "string",
  "ntQty": "string",
  "dsQty": "string",
  "flQty": "string",
  "trgPrc": "string",
  "exONo": "string",
  "sts": "string",
  "rjRsn": "string",
  "ordTyp": "LIMIT",
  "rcvTim": "string",
  "dur": "string",
  "vlDt": "string",
  "prdCode": "CNC",
  "ogt": "string",
  "sipID": "string",
  "userID": "string",
  "pdQty": "string",
  "desc": "string",
  "dpInsTyp": "string",
  "dpExpDt": "string",
  "stkPrc": "string",
  "opTyp": "string",
  "edit": "string",
  "cancel": "string",
  "exit": "string",
  "asTyp": "string",
  "tkSz": "string",
  "ltSz": "string",
  "isCOSecLeg": "string",
  "exp": "string",
  "dpName": "string",
  "qtyUnits": "string",
  "rcvEpTim": "string",
  "rmk": "string",
  "trgId": "string",
  "userCmnt": "string",
  "cta": "string",
  "ltp": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | none |
| ordID | string | false | none | none |
| nstReqID | string | false | none | none |
| trsTyp | string | false | none | none |
| trdSym | string | false | none | none |
| sym | string | false | none | none |
| srs | string | false | none | none |
| cpName | string | false | none | none |
| prc | string | false | none | none |
| avgPrc | string | false | none | none |
| ntQty | string | false | none | none |
| dsQty | string | false | none | none |
| flQty | string | false | none | none |
| trgPrc | string | false | none | none |
| exONo | string | false | none | none |
| sts | string | false | none | none |
| rjRsn | string | false | none | none |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| rcvTim | string | false | none | none |
| dur | string | false | none | none |
| vlDt | string | false | none | Order validity data -GTC/GTD |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| ogt | string | false | none | none |
| sipID | string | false | none | none |
| userID | string | false | none | none |
| pdQty | string | false | none | none |
| desc | string | false | none | none |
| dpInsTyp | string | false | none | none |
| dpExpDt | string | false | none | none |
| stkPrc | string | false | none | none |
| opTyp | string | false | none | none |
| edit | string | false | none | none |
| cancel | string | false | none | none |
| exit | string | false | none | none |
| asTyp | string | false | none | none |
| tkSz | string | false | none | none |
| ltSz | string | false | none | none |
| isCOSecLeg | string | false | none | none |
| exp | string | false | none | none |
| dpName | string | false | none | none |
| qtyUnits | string | false | none | none |
| rcvEpTim | string | false | none | none |
| rmk | string | false | none | none |
| trgId | string | false | none | Trigger ID |
| userCmnt | string | false | none | Comment added by user while placing the order |
| cta | string | false | none | Call to action based on rejection reason |
| ltp | string | false | none | Last Traded Price |

## ComTradeBookResponseObject

```json
{
  "exc": "string",
  "ordID": "string",
  "ordTyp": "LIMIT",
  "trsTyp": "string",
  "trdSym": "string",
  "sym": "string",
  "cpName": "string",
  "srs": "string",
  "dsQty": "string",
  "exONo": "string",
  "rcvTim": "string",
  "prdCode": "CNC",
  "flQty": "string",
  "qty": "string",
  "trdID": "string",
  "flPrc": "string",
  "ltp": "string",
  "chg": "string",
  "chgP": "string",
  "asTyp": "string",
  "dpInsTyp": "string",
  "dpExpDt": "string",
  "stkPrc": "string",
  "opTyp": "string",
  "psCnv": "string",
  "ntPrc": "string",
  "sts": "string",
  "tkSz": "string",
  "ltSz": "string",
  "dpName": "string",
  "exp": "string",
  "qtyUnits": "string",
  "rmk": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | none |
| ordID | string | false | none | none |
| ordTyp | [OrderType](#ordertype) | false | none | Order Type |
| trsTyp | string | false | none | none |
| trdSym | string | false | none | none |
| sym | string | false | none | none |
| cpName | string | false | none | none |
| srs | string | false | none | none |
| dsQty | string | false | none | none |
| exONo | string | false | none | none |
| rcvTim | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| flQty | string | false | none | none |
| qty | string | false | none | none |
| trdID | string | false | none | none |
| flPrc | string | false | none | none |
| ltp | string | false | none | none |
| chg | string | false | none | none |
| chgP | string | false | none | none |
| asTyp | string | false | none | none |
| dpInsTyp | string | false | none | none |
| dpExpDt | string | false | none | none |
| stkPrc | string | false | none | none |
| opTyp | string | false | none | none |
| psCnv | string | false | none | none |
| ntPrc | string | false | none | none |
| sts | string | false | none | none |
| tkSz | string | false | none | none |
| ltSz | string | false | none | none |
| dpName | string | false | none | none |
| exp | string | false | none | none |
| qtyUnits | string | false | none | none |
| rmk | string | false | none | none |

## ComPositionBookObject

```json
{
  "exc": "string",
  "trdSym": "string",
  "sym": "string",
  "cpName": "string",
  "byQty": "string",
  "avgByPrc": "string",
  "byAmt": "string",
  "slQty": "string",
  "avgSlPrc": "string",
  "slAmt": "string",
  "ntAmt": "string",
  "ntQty": "string",
  "prdCode": "CNC",
  "rlzPL": "string",
  "urlzPL": "string",
  "mtm": "string",
  "ltp": "string",
  "dpExpDt": "string",
  "brkEvnPrc": "string",
  "dpInsTyp": "string",
  "opTyp": "string",
  "stkPrc": "string",
  "sqOff": "string",
  "asTyp": "string",
  "ntPL": "string",
  "tkSz": "string",
  "ltSz": "string",
  "mul": "string",
  "trsTyp": "string",
  "dpName": "string",
  "prc": "string",
  "rchFlg": "string",
  "nwsFlg": "string",
  "gn": "string",
  "gd": "string",
  "pn": "string",
  "pd": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| exc | string | false | none | none |
| trdSym | string | false | none | none |
| sym | string | false | none | none |
| cpName | string | false | none | none |
| byQty | string | false | none | none |
| avgByPrc | string | false | none | none |
| byAmt | string | false | none | none |
| slQty | string | false | none | none |
| avgSlPrc | string | false | none | none |
| slAmt | string | false | none | none |
| ntAmt | string | false | none | none |
| ntQty | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| rlzPL | string | false | none | none |
| urlzPL | string | false | none | none |
| mtm | string | false | none | none |
| ltp | string | false | none | none |
| dpExpDt | string | false | none | none |
| brkEvnPrc | string | false | none | none |
| dpInsTyp | string | false | none | none |
| opTyp | string | false | none | none |
| stkPrc | string | false | none | none |
| sqOff | string | false | none | none |
| asTyp | string | false | none | none |
| ntPL | string | false | none | none |
| tkSz | string | false | none | none |
| ltSz | string | false | none | none |
| mul | string | false | none | none |
| trsTyp | string | false | none | none |
| dpName | string | false | none | none |
| prc | string | false | none | none |
| rchFlg | string | false | none | none |
| nwsFlg | string | false | none | none |
| gn | string | false | none | none |
| gd | string | false | none | none |
| pn | string | false | none | none |
| pd | string | false | none | none |

## ConvertPositionDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» msg | string | false | none | none |

## MFTradeRequestDao

```json
{
  "currentOrdSts": "ACCEPTED",
  "token": "string",
  "isin": "string",
  "txnTyp": "string",
  "clientCode": "string",
  "qty": 0,
  "amt": 0,
  "reInvFlg": "string",
  "reqstdBy": "string",
  "folioNo": "string",
  "ordTyp": "string",
  "txnId": 0,
  "schemeName": "string",
  "rmrk": "string",
  "mnRdmFlg": "string",
  "ordSrc": "string",
  "strtDy": 0,
  "strtDt": "string",
  "endDt": "string",
  "sipFrq": "string",
  "gfot": "string",
  "tnr": "string",
  "mdtId": "string",
  "sipregno": "string",
  "siporderno": "string",
  "schemePlan": "Direct",
  "schemeCode": "schemeCode",
  "closeAccountFlag": "string",
  "kycflag": "string",
  "dpc": "string",
  "euinflag": "string",
  "euinnumber": "string",
  "physicalFlag": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| currentOrdSts | string | false | none | Order Status in case of Modify or Cancel |
| token | string | false | none | Token of scheme |
| isin | string | false | none | ISIN of scheme |
| txnTyp | string | false | none | FP – Fresh Purchase AP – Additional Purchase R – Redemption SIP – SIP XSIP - XSIP |
| clientCode | string | false | none | Client code of user, mandatory for GPS |
| qty | number(double) | false | none | Units to redeem |
| amt | number(double) | false | none | for Fresh Purchase/ Additional Purchase/ SIP/XSIP/ISIP |
| reInvFlg | string | false | none | Z- Growth Y- Div Reinvest N- Div Payout |
| reqstdBy | string | false | none | DealerCode/Clientcode |
| folioNo | string | false | none | Blank for Fresh Purchase For Redeem/Additional Purchase/ SWITCH  For physical Order Type Mandatory,For Demat On mandatory |
| ordTyp | string | false | none | Order type : Fresh, Modify or Cancel |
| txnId | integer(int64) | false | none | 0 for New Order ,OrderID for Modify ,Order OrderID for Cancel Order |
| schemeName | string | false | none | Scheme Name |
| rmrk | string | false | none | remarks |
| mnRdmFlg | string | false | none | Y/N (Y- for Full Redeem) |
| ordSrc | string | false | none | WEB/EMT/Admin |
| strtDy | integer(int32) | false | none | For SIP/XSIP - 09 (DAY of SIP Start Date) Mandatory for SIP/ISIP/XSIP/SWP/STP |
| strtDt | string | false | none | SIP / XSIP/ISIP/STP/SWP Start Date (Mandatory for SIP/ISIP/XSIP/SWP/STP) |
| endDt | string | false | none | SIP / XSIP/ISIP/STP/SWP Start Date (Mandatory for SIP/ISIP/XSIP/SWP/STP) |
| sipFrq | string | false | none | Monthly – (SIP/ XSIP/ISIP/STP/SWP Frequency Mandatory for SIP/ISIP/XSIP/SWP/STP) |
| gfot | string | false | none | Y/N – (Genrate first order today Mandatory for SIP/ISIP/XSIP/SWP/STP) |
| tnr | string | false | none | Tenure Period Like 99 Mandatory for SIP/ISIP/XSIP/SWP/STP |
| mdtId | string | false | none | Mandate id selected by client |
| sipregno | string | false | none | SIP Registration Number |
| siporderno | string | false | none | SIP Order Number |
| schemePlan | string | false | none | Scheme Plan |
| schemeCode | string | false | none | Scheme Code |
| closeAccountFlag | string | false | none | none |
| kycflag | string | false | none | none |
| dpc | string | false | none | none |
| euinflag | string | false | none | none |
| euinnumber | string | false | none | none |
| physicalFlag | string | false | none | none |

#### Enumerated Values

| Property | Value |
| --- | --- |
| currentOrdSts | ACCEPTED |
| currentOrdSts | REJECTED |
| currentOrdSts | CANCELLED |
| currentOrdSts | AMO ... |
| schemePlan | Direct |
| schemePlan | Normal |
| schemeCode | schemeCode |

## TradeMFResponseDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "ordNo": "string",
    "msg": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» ordNo | string | false | none | Order number of the order created / edited |
| »» msg | string | false | none | Message to be displayed to client |

## MFHoldingsResponseDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "mfHdgUsable": [
      {
        "nav": "string",
        "hdgVl": "string",
        "scName": "string",
        "sym": "string",
        "isin": "string",
        "srs": "string",
        "symName": "string",
        "usdQty": "string",
        "ct": "string",
        "prdCode": "CNC",
        "amc": "string",
        "hdgQty": "string",
        "trdSym": "string",
        "folioID": "string",
        "units": 0,
        "amount": 0,
        "mode": "string",
        "physHldQty": [
          {
            "units": 0,
            "folioNo": "string"
          }
        ]
      }
    ],
    "usableHld": "string",
    "nonUsable": [
      {
        "category": "string",
        "amc": "string",
        "companyName": "string",
        "pledgQty": "string",
        "lockedInQty": "string",
        "ltp": "string",
        "holdingValue": "string",
        "assetClass": "string",
        "isin": "string"
      }
    ],
    "nonUsableHld": "string",
    "mfHV": "string"
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» type | string | false | none | none |
| »» mfHdgUsable | [[MFSSHoldingsObject](#mfssholdingsobject)] | false | none | List of Usable holdings |
| »» usableHld | string | false | none | Total holding value of usable holdings |
| »» nonUsable | [[ELSSReportIndividualHoldings](#elssreportindividualholdings)] | false | none | List of Non Usable holdings |
| »» nonUsableHld | string | false | none | Total non usable holdings |
| »» mfHV | string | false | none | Total mf holdings value |

## ReconciliationRespDao

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "ordLst": [
      {
        "txnID": "string",
        "clientID": "string",
        "schemeID": "string",
        "txnType": "string",
        "units": "string",
        "amount": "string",
        "closeAccountFlag": "string",
        "reinvestmentFlag": "string",
        "toSchemeID": "string",
        "isNFO": false,
        "txnDate": "string",
        "txnTime": "string",
        "folioNo": "string",
        "checkDigNo": "string",
        "redPyMec": "string",
        "status": "string",
        "fileGeneratedFreq": "string",
        "remarks": "string",
        "orderedBy": "string",
        "lastModifiedBy": "string",
        "lastModifiedOn": "string",
        "sysRefNo": "string",
        "referenceNO": "string",
        "token": "string",
        "schemeCode": "string",
        "rnTSchemeCode": "string",
        "inBatchID": "string",
        "inSubBatchID": "string",
        "physicalFlag": "string",
        "minRedeemFlag": "string",
        "redeemDate": "string",
        "redeemAmount": "string",
        "vcOrderRemarks": "string",
        "clientCode": "string",
        "isSpread": "string",
        "orderSource": "string",
        "startDay": "string",
        "startDate": "string",
        "endDate": "string",
        "genrateToday": "string",
        "tenure": "string",
        "mandateID": "string",
        "brokerage": "string",
        "switchSchemeCode": "string",
        "switchISIN": "string",
        "createdBy": "string",
        "createdOn": "string",
        "exchangeRefNo": "string",
        "mode": "string",
        "validateMargin": "string",
        "brokerRefNo": "string",
        "limitValidation": "string",
        "checkHoldings": "string",
        "modelPortFolioName": "string",
        "orderType": "string",
        "uniqueNumber": "string",
        "subBrokerCode": "string",
        "paymentMode": "string",
        "mandateSts": "string",
        "ordStatus": "string",
        "isModify": false,
        "isCancel": false,
        "schemeName": "string",
        "isin": "string",
        "nav": 0,
        "sipfrequency": "string",
        "dpc": "string",
        "euinflag": "string",
        "mfimfdflag": "string",
        "arn": "string",
        "euinnumber": "string",
        "settlementType": "string",
        "sipregDate": "string",
        "rmcode": "string",
        "navasNoDate": "string",
        "kycflag": "string",
        "amcschemeCode": "string",
        "amccode": "string"
      }
    ]
  }
}
```

### Properties

allOf

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | [CommonResponseWrapper](#commonresponsewrapper) | false | none | none |

and

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| *anonymous* | object | false | none | none |
| » data | object | false | none | none |
| »» ordLst | [[DIONReportReconciliation](#dionreportreconciliation)] | false | none | List of orders |

## DIONReportReconciliation

```json
{
  "txnID": "string",
  "clientID": "string",
  "schemeID": "string",
  "txnType": "string",
  "units": "string",
  "amount": "string",
  "closeAccountFlag": "string",
  "reinvestmentFlag": "string",
  "toSchemeID": "string",
  "isNFO": false,
  "txnDate": "string",
  "txnTime": "string",
  "folioNo": "string",
  "checkDigNo": "string",
  "redPyMec": "string",
  "status": "string",
  "fileGeneratedFreq": "string",
  "remarks": "string",
  "orderedBy": "string",
  "lastModifiedBy": "string",
  "lastModifiedOn": "string",
  "sysRefNo": "string",
  "referenceNO": "string",
  "token": "string",
  "schemeCode": "string",
  "rnTSchemeCode": "string",
  "inBatchID": "string",
  "inSubBatchID": "string",
  "physicalFlag": "string",
  "minRedeemFlag": "string",
  "redeemDate": "string",
  "redeemAmount": "string",
  "vcOrderRemarks": "string",
  "clientCode": "string",
  "isSpread": "string",
  "orderSource": "string",
  "startDay": "string",
  "startDate": "string",
  "endDate": "string",
  "genrateToday": "string",
  "tenure": "string",
  "mandateID": "string",
  "brokerage": "string",
  "switchSchemeCode": "string",
  "switchISIN": "string",
  "createdBy": "string",
  "createdOn": "string",
  "exchangeRefNo": "string",
  "mode": "string",
  "validateMargin": "string",
  "brokerRefNo": "string",
  "limitValidation": "string",
  "checkHoldings": "string",
  "modelPortFolioName": "string",
  "orderType": "string",
  "uniqueNumber": "string",
  "subBrokerCode": "string",
  "paymentMode": "string",
  "mandateSts": "string",
  "ordStatus": "string",
  "isModify": false,
  "isCancel": false,
  "schemeName": "string",
  "isin": "string",
  "nav": 0,
  "sipfrequency": "string",
  "dpc": "string",
  "euinflag": "string",
  "mfimfdflag": "string",
  "arn": "string",
  "euinnumber": "string",
  "settlementType": "string",
  "sipregDate": "string",
  "rmcode": "string",
  "navasNoDate": "string",
  "kycflag": "string",
  "amcschemeCode": "string",
  "amccode": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| txnID | string | false | none | none |
| clientID | string | false | none | none |
| schemeID | string | false | none | none |
| txnType | string | false | none | none |
| units | string | false | none | none |
| amount | string | false | none | none |
| closeAccountFlag | string | false | none | none |
| reinvestmentFlag | string | false | none | none |
| toSchemeID | string | false | none | none |
| isNFO | boolean | false | none | none |
| txnDate | string | false | none | none |
| txnTime | string | false | none | none |
| folioNo | string | false | none | none |
| checkDigNo | string | false | none | none |
| redPyMec | string | false | none | none |
| status | string | false | none | none |
| fileGeneratedFreq | string | false | none | none |
| remarks | string | false | none | none |
| orderedBy | string | false | none | none |
| lastModifiedBy | string | false | none | none |
| lastModifiedOn | string | false | none | none |
| sysRefNo | string | false | none | none |
| referenceNO | string | false | none | none |
| token | string | false | none | none |
| schemeCode | string | false | none | none |
| rnTSchemeCode | string | false | none | none |
| inBatchID | string | false | none | none |
| inSubBatchID | string | false | none | none |
| physicalFlag | string | false | none | none |
| minRedeemFlag | string | false | none | none |
| redeemDate | string | false | none | none |
| redeemAmount | string | false | none | none |
| vcOrderRemarks | string | false | none | none |
| clientCode | string | false | none | none |
| isSpread | string | false | none | none |
| orderSource | string | false | none | none |
| startDay | string | false | none | none |
| startDate | string | false | none | none |
| endDate | string | false | none | none |
| genrateToday | string | false | none | none |
| tenure | string | false | none | none |
| mandateID | string | false | none | none |
| brokerage | string | false | none | none |
| switchSchemeCode | string | false | none | none |
| switchISIN | string | false | none | none |
| createdBy | string | false | none | none |
| createdOn | string | false | none | none |
| exchangeRefNo | string | false | none | none |
| mode | string | false | none | none |
| validateMargin | string | false | none | none |
| brokerRefNo | string | false | none | none |
| limitValidation | string | false | none | none |
| checkHoldings | string | false | none | none |
| modelPortFolioName | string | false | none | none |
| orderType | string | false | none | none |
| uniqueNumber | string | false | none | none |
| subBrokerCode | string | false | none | none |
| paymentMode | string | false | none | none |
| mandateSts | string | false | none | none |
| ordStatus | string | false | none | none |
| isModify | boolean | false | none | Is modifiable True/False |
| isCancel | boolean | false | none | Is cancellable True/False |
| schemeName | string | false | none | schemeName |
| isin | string | false | none | none |
| nav | number(double) | false | none | none |
| sipfrequency | string | false | none | none |
| dpc | string | false | none | none |
| euinflag | string | false | none | none |
| mfimfdflag | string | false | none | none |
| arn | string | false | none | none |
| euinnumber | string | false | none | none |
| settlementType | string | false | none | none |
| sipregDate | string | false | none | none |
| rmcode | string | false | none | none |
| navasNoDate | string | false | none | none |
| kycflag | string | false | none | none |
| amcschemeCode | string | false | none | none |
| amccode | string | false | none | none |

## MFSSHoldingsObject

```json
{
  "nav": "string",
  "hdgVl": "string",
  "scName": "string",
  "sym": "string",
  "isin": "string",
  "srs": "string",
  "symName": "string",
  "usdQty": "string",
  "ct": "string",
  "prdCode": "CNC",
  "amc": "string",
  "hdgQty": "string",
  "trdSym": "string",
  "folioID": "string",
  "units": 0,
  "amount": 0,
  "mode": "string",
  "physHldQty": [
    {
      "units": 0,
      "folioNo": "string"
    }
  ]
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| nav | string | false | none | none |
| hdgVl | string | false | none | none |
| scName | string | false | none | none |
| sym | string | false | none | none |
| isin | string | false | none | none |
| srs | string | false | none | none |
| symName | string | false | none | none |
| usdQty | string | false | none | none |
| ct | string | false | none | none |
| prdCode | [PrdCode](#prdcode) | false | none | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF/CO/BO |
| amc | string | false | none | none |
| hdgQty | string | false | none | none |
| trdSym | string | false | none | none |
| folioID | string | false | none | none |
| units | number(double) | false | none | none |
| amount | number(double) | false | none | none |
| mode | string | false | none | none |
| physHldQty | [[PhysicalHoldingsQty](#physicalholdingsqty)] | false | none | Physical Holdings Quantity |

## ELSSReportIndividualHoldings

```json
{
  "category": "string",
  "amc": "string",
  "companyName": "string",
  "pledgQty": "string",
  "lockedInQty": "string",
  "ltp": "string",
  "holdingValue": "string",
  "assetClass": "string",
  "isin": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| category | string | false | none | none |
| amc | string | false | none | none |
| companyName | string | false | none | none |
| pledgQty | string | false | none | none |
| lockedInQty | string | false | none | none |
| ltp | string | false | none | none |
| holdingValue | string | false | none | none |
| assetClass | string | false | none | none |
| isin | string | false | none | none |

## PhysicalHoldingsQty

```json
{
  "units": 0,
  "folioNo": "string"
}
```

### Properties

| Name | Type | Required | Restrictions | Description |
| --- | --- | --- | --- | --- |
| units | number(double) | false | none | none |
| folioNo | string | false | none | none |

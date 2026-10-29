# Authentication

The OAuth2 authentication protocol is used for all API calls. Any OAuth2 client library can be used.

## OAuth2 Configuration

| Setting | Value |
| --- | --- |
| Base URL | `<base_url>` (examples use `https://masterswift-beta.mastertrust.co.in`) |
| OAuth2 Client ID | User's choice |
| OAuth2 Client Secret | Provided by Tradelab (save it for future use) |
| Grant type | Authorization Code |
| Authorization endpoint | `/oauth2/auth` |
| Access token endpoint | `/oauth2/token` |
| Redirect URL | User's choice (default `http://127.0.0.1`) |
| Scope | `orders holdings` |
| Credentials | As Basic Auth header (default) |

## Login Flow

Open the authorization URL in a web browser (once every trading day):

```
<base_url>/oauth2/auth?scope=orders%20holdings&state=%7B%22param%22:%22value%22%7D&redirect_uri=http://127.0.0.1&response_type=code&client_id=<oauthID>
```

Enter the trading platform's login credentials and 2FA ([TOTP](#totp)). After this step, the user receives an access token (via the standard authorization-code exchange at `/oauth2/token`).

## Using the Access Token

Send the access token with every API request unless stated otherwise:

```
Authorization: Bearer {access_token}
```

If the token expires, the API returns HTTP `401`, and a new access token must be obtained.

## TOTP

TOTP (Time-based One-Time Password) is a secure authentication method where a unique, temporary password is generated using time as a factor. An authenticator app on the user's device generates a new code at set intervals. Use TOTP as the 2FA for an extra layer of security.

### How to Enable TOTP

1. Visit [www.mastertrust.co.in](https://www.mastertrust.co.in) and click **Sign in** to the Master Web platform.
2. Log in on the **MASTERWEB** screen with your User ID, password, and OTP.
3. An **Activate TOTP** page appears. Follow its steps:
   1. Download and install Microsoft Authenticator or Google Authenticator on your phone or tablet.
   2. Scan the QR code shown (or copy the code if you are unable to scan) in the authenticator app.

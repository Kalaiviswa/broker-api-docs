# C# library for Accessing the Services Provided by Nuvama

The Library API Connect is a set of REST-like APIs that expose many capabilities required to build
a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live
market data, and more, with the simple HTTP API collection This module provides an easy to use abstraction
over the HTTP APIs. The HTTP calls have been converted to methods and their JSON responses are returned.

C# SDK :

- API version: v1
- SDK version: 1.0.0

## Frameworks supported

- .NET 4.0 or later
- Windows Phone 7.1 (Mango)

## Dependencies

- [RestSharp](https://www.nuget.org/packages/RestSharp) - 105.1.0 or later
- [Json.NET](https://www.nuget.org/packages/Newtonsoft.Json/) - 7.0.0 or later
- [JsonSubTypes](https://www.nuget.org/packages/JsonSubTypes/) - 1.2.0 or later
- [IniParser](https://www.nuget.org/packages/ini-parser/) - 2.5.2 or later
- [Log4net](https://www.nuget.org/packages/log4net/) - 2.0.12 or later
- [NUnit3TestAdapter](https://www.nuget.org/packages/NUnit3TestAdapter/) - 4.0.0 or later
- [NUnit](https://www.nuget.org/packages/NUnit/) - 3.11.0 or later

The DLLs included in the package may not be the latest version. We recommend using [NuGet](https://docs.nuget.org/consume/installing-nuget) to obtain the latest version of the
packages:

```csharp
Install-Package RestSharp
Install-Package Newtonsoft.Json
Install-Package JsonSubTypes
Install-Package ini-parser
Install-Package log4net
Install-Package NUnit3TestAdapter
Install-Package NUnit
```

NOTE: RestSharp versions greater than 105.1.0 have a bug which causes file uploads to fail. See [RestSharp#742](https://github.com/restsharp/RestSharp/issues/742)

## Installation

Run the following command to generate the DLL

- [Windows] `build.bat`

Then include the DLL (under the `bin` folder) in the C# project, and use the namespaces:

```csharp
using .Api;
using .Client;
using .Model;
```

## Packaging

A `.nuspec` is included with the project. You can follow the Nuget quickstart to [create](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#create-the-package)
and [publish](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#publish-the-package)
packages.

This `.nuspec` uses placeholders from the `.csproj`, so build the `.csproj`
directly:

```csharp
nuget pack -Build -OutputDirectory out .csproj
```

Then, publish to a [local
feed](https://docs.microsoft.com/en-us/nuget/hosting-packages/local-feeds) or [other host](https://docs.microsoft.com/en-us/nuget/hosting-packages/overview) and
consume the new package via Nuget as usual.

## Configuration from external INI file

When using APIConnect wrapper ,various parameters are read from the Settings.ini file.These
parameters are configurable. Description for these parameters is given below.

| Parameters | Description | Remarks |
| --- | --- | --- |
||  |  |  |
| --- | --- | --- |
| [GLOBAL] | Contains global configuration |  |
 [LOG] | Contains logging related configuration |  |
| LogLevel | Contains logging related configuration | DEBUG |
| LogFilePath | Absolute path to the logging file. |  |
| [SERVER] | Contains Streaming related configuration |  |
| Server | Host address of streaming socket. | ncst.nuvamawealth.com |
| Port | Port of streaming socket. | 9443 |

# APIConnect documentation

- [User Login Flow](https://www.nuvamawealth.com/library-documentation/docs/UserLoginFlow.md.html)

## Getting Started

```csharp
#!cSharp
using APIConnect

# Redirect the user to the login url - <https://www.nuvamawealth.com/api-connect/login?api_key=xxx>
# after the login flow, You will get requestId.
# Generate a session with this request id
# as follows.
apiConnect = new APIConnect("apiKey", "api_secret_password", "requestId", True, "File_path_to_external_INI_file");

# Place an order
response = apiConnect.PlaceTrade('symbol',
                          'exchange',
                          'buy-sell',
                          validity',
                          'orderType',
                          'quantity',
                          'exchangeCode',
                          'limitPrice',
                          'productCode');

# Fetch all orders
apiConnect.OrderBook();
#Fetch all trades
apiConnect.TradeBook();
```

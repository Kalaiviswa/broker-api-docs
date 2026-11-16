# JAVA library for Accessing the Services Provided by Nuvama

The Library API Connect is a set of REST-like APIs that expose many capabilities required to build
a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live
market data, and more, with the simple HTTP API collection This module provides an easy to use abstraction
over the HTTP APIs. The HTTP calls have been converted to methods and their JSON responses are returned.

Java JDK :

- API version: v1
- JDK version: 1.8

## Dependencies

- [junit](https://mvnrepository.com/artifact/junit/junit) - 3.8.1
- [commons-codec](https://mvnrepository.com/artifact/commons-codec) - 1.11
- [org.ini4j](https://mvnrepository.com/artifact/org.ini4j) - 0.5.1
- [net.sf.supercsv](https://mvnrepository.com/artifact/net.sf.supercsv) - 2.4.0
- [log4j](https://mvnrepository.com/artifact/log4j) - 1.2.17
- [com.neovisionaries](https://mvnrepository.com/artifact/com.neovisionaries) - 2.3
- [org.json](https://mvnrepository.com/artifact/org.json) - 20171018
- [com.squareup.okhttp3](https://mvnrepository.com/artifact/com.squareup.okhttp3) - 4.4.0
- [com.google.code.gson](https://mvnrepository.com/artifact/com.google.code.gson) - 2.6.2
- [org.jetbrains.kotlin](https://mvnrepository.com/artifact/org.jetbrains.kotlin) - 1.3.70
- [org.apache.maven.plugins](https://mvnrepository.com/artifact/org.apache.maven.plugins) - 3.8.1

## Set up the project

First you’ll need to setup a Java project for Maven to build. Create this structure in a project folder.

Maven is downloadable as a zip file at https://maven.apache.org/download.cgi. Only the binaries are
required, so look for the link to apache-maven-{version}-bin.zip or apache-maven-{version}-bin.tar.gz.

**Build Java code**

Maven is now ready to build the project. You can execute several build lifecycle goals with Maven now,
including goals to compile the project’s code,
create a library package (such as a JAR file), and install the library in the local Maven dependency
repository.

mvn compile

This will run Maven, telling it to execute the compile goal. When it’s finished, you should find the compiled
.class files in the target/classes directory.

## Packaging

mvn package

The package goal will compile Java code, run any tests, and finish by packaging the code up in a JAR file
within the target directory.
The name of the JAR file will be based on the project’s artifactId and version.

To execute the JAR file run:

java -jar target/apiconnect-maven-0.1.0.jar

## Installing 3rd party JARs

To install a JAR in the local repository use the following command:

mvn install:install-file -Dfile= -DgroupId= -DartifactId= -Dversion=
 -Dpackaging=
If there's a pom-file as well, you can install it with the following command:

mvn install:install-file -Dfile= -DpomFile=
With version 2.5 of the maven-install-plugin, it can get even simpler: if the JAR was built by Apache
Maven, it'll contain a pom.xml in a subfolder of the META-INF/ directory, which will be read by default.
In that case, all you need to do is:

mvn org.apache.maven.plugins:maven-install-plugin:2.5.2:install-file -Dfile=

## Configuration from external INI file

When using APIConnect wrapper ,various parameters are read from the Settings.ini file.These
parameters are configurable. Description for these parameters is given below.

| Parameters | Description | Remarks |
| --- | --- | --- |
| [GLOBAL] | Contains global configuration |  |
| [LOG] | Contains logging related configuration |  |
| Level | Log level key. | DEBUG |
| [PROXY] | Contains PROXY related configuration |  |
| Host | Hostname for proxy settings. |  |
| Port | Port number for proxy settings. |  |
| User | Username for proxy settings. |  |
| Pass | Password for proxy settings. |  |
| [Stream] | Contains Streaming related configuration |  |
| Host | Hostname for Streamer. | ncst.nuvamawealth.com |
| Port | Port number for Streamer. | 9443 |

# APIConnect documentation

- [User Login Flow](https://www.nuvamawealth.com/library-documentation/docs/UserLoginFlow.md.html)

## Getting Started

```java
#!Java
using APIConnect

# Redirect the user to the login url - <https://www.nuvamawealth.com/api-connect/login?api_key=xxx>
# after the login flow, You will get requestId.
# Generate a session with this request id
# as follows.
APIConnect connect = new APIConnect("apiKey", "api_secret_password", "requestId", True, "File_path_to_external_INI_file");

# Place an order
String response = connect.PlaceTrade("trdSymbol",
                         "exchange","action",
                         "duration","orderType",
                         "quantity","streamingSymbol",
                         "limitPrice","dscQty", "trgPrc",
                         "productCode");

# Fetch all orders
connect.orderBook();
#Fetch all trades
connect.tradeBook();
```

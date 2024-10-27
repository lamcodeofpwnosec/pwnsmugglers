# pwnsmugglers

**pwnsmugglers** is an automated tool designed for detecting HTTP Request Smuggling vulnerabilities in web applications. This vulnerability, also known as HTTP Desync Attack, occurs due to discrepancies in the processing of HTTP requests between front-end and back-end servers. The tool automates the detection and exploitation process, making it easier for penetration testers and security researchers to identify these critical vulnerabilities in their target web applications.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Payloads](#payloads)
5. [Requirements](#requirements)
6. [Contributing](#contributing)
7. [License](#license)

## Features

pwnsmugglers offers several core features designed to simplify the process of identifying and exploiting HTTP Request Smuggling vulnerabilities:

- **Automatic HTTP Request Smuggling Detection**: The tool uses pre-built payloads to automatically detect if a target is vulnerable to HTTP Request Smuggling attacks. It works by sending specially crafted requests to the server and analyzing its responses.
  
- **Payload Customization**: The tool comes with a default set of payloads in `payloads.json`, but users can modify or add their own payloads based on specific requirements. This makes the tool versatile in testing various server configurations.

- **Support for Chunked and Content-Length Smuggling**: The tool supports both types of smuggling techniques:
  - **Chunked Transfer Encoding**: Smuggling through discrepancies in chunked transfer encoding.
  - **Content-Length Header**: Exploiting mismatches between Content-Length headers to force the server to interpret part of a request as a new request.

- **Modular and Extensible**: The code is organized into modular sections, which makes it easy for users to extend the tool by adding additional detection capabilities or different attack types.

- **Verbose Output**: Provides detailed output about the attack attempts, including HTTP responses, headers, and any signs of vulnerability detected.

- **Log and Report Generation**: Automatically generates a detailed log of each scanning session, which can be used for further analysis or reporting purposes.

## Installation

### Prerequisites
Before using **pwnsmugglers**, ensure you have the following installed on your system:

- Python 3.x
- `pip` package manager

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```
Clone this repository to your local machine:
```
$ git clone https://github.com/lamcodeofpwnosec/pwnsmugglers.git
$ cd pwnsmugglers
$ python3 smuggle.py -u https://target-website.com
```
The tool will automatically attempt various HTTP Request Smuggling techniques on the provided URL. You can also provide additional options for more advanced usage:
 - `-v`: Verbose mode, provides detailed output of each request and response.
 - `-p`: Specify a custom payload file if you want to use your own set of payloads.

## Payloads
The tool comes with a default set of payloads located in the `payloads.json` file. These payloads are specifically crafted to test different variations of HTTP Request Smuggling attacks. Users can modify this file to add more payloads or adjust existing ones to suit the specific environment they are testing.
Here’s an example structure of a payload:
```json
{
    "name": "Basic CL.TE Smuggle",
    "payload": "POST / HTTP/1.1\r\nHost: vulnerable.com\r\nContent-Length: 13\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nG",
    "method": "POST",
    "headers": {
        "Host": "vulnerable.com",
        "Content-Length": "13",
        "Transfer-Encoding": "chunked"
    },
    "body": "0\r\n\r\nG"
}
```
Each payload includes the following fields:
 - **name:** A descriptive name for the payload.
 - **payload:** The raw HTTP request that will be sent.
 - **method:** The HTTP method to be used (e.g., GET, POST).
 - **headers:** Any custom headers that should be included in the request.
 - **body:** The request body, if applicable.


> [!NOTE]
> Copyright [©lamcodeofpwnosec](https://github.com/lamcodeofpwnosec/)


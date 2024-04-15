# Web Security Headers Checker

Web Security Headers Checker is a Python tool to check security headers of websites.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Authors](#authors)

## Description

This Python script checks the security headers of a given website. It verifies whether essential security headers like X-Frame-Options, X-XSS-Protection, Content-Security-Policy, etc., are implemented correctly. If any security header is missing, it provides a description of the header and suggests implementing it for better security.

## Installation

1. Clone or download the repository to your local machine.
2. Make sure you have Python 3 installed.
3. Install the required dependencies using pip:


## Usage

Run the script `websecuritychecker.py` using Python. It will prompt you to enter the domain name of the website you want to analyze. After analyzing the website, it will display the status of each security header along with any missing headers and their descriptions.

To execute the script, use the following command:

python3 websecuritychecker.py


Follow the on-screen instructions to perform the security header scan.

## License

This program is licensed under the [GNU General Public License](http://www.gnu.org/licenses/).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request on GitHub.

## Authors

- **Jeret Christopher** - *Initial work* - [M0du5](https://github.com/M0du5)

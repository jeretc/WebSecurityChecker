#!/usr/bin/env python3

# websecuritychecker - Web Security Headers Checker!
# Copyright (C) 2024  Jeret Christopher@M0du5
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Define metadata
print()
author = "\033[1;32mJeret Christopher@M0du5\033[0m"
version = "\033[1;36m1.0\033[0m"
description = "\033[1;34mWeb Security Checker - Python tool to check security headers of websites.\033[0m"

# Display metadata
print(f"Author: {author}")
print(f"Version: {version}")
print(f"Description: {description}\n")

import requests
import sys

def check_security_headers(url):
    headers = [
        ('X-Frame-Options', 'Prevents your webpage from being embedded in an iframe by another site.'),
        ('X-XSS-Protection', 'Enables the cross-site scripting (XSS) filter built into modern web browsers.'),
        ('X-Content-Type-Options', 'Prevents Google Chrome and Internet Explorer from MIME-sniffing a response away from the declared content type.'),
        ('X-Permitted-Cross-Domain-Policies', 'Specifies who can access your website\'s data across different domains.'),
        ('Strict-Transport-Security', 'Instructs browsers to only access your site over HTTPS.'),
        ('Content-Security-Policy', 'Prevents XSS, clickjacking, and other code injection attacks by specifying content sources.'),
        ('Referrer-Policy', 'Controls how much information the browser includes with navigations away from a document.'),
        ('Feature-Policy', 'Allows you to selectively enable, disable, and modify the behavior of certain browser features and APIs used by your website.'),
        ('Expect-CT', 'Enables the Certificate Transparency (CT) policy enforcement, which protects you from misissued SSL certificates.')
    ]

    results = {}

    try:
        response = requests.get(url)
        for header, description in headers:
            if header in response.headers:
                results[header] = {'status': 'Implemented', 'value': response.headers[header]}
            else:
                results[header] = {'status': 'Not Implemented', 'value': '', 'description': description}
    except requests.exceptions.RequestException as e:
        print()
        print("Error occurred while connecting to the website.")
        print("Possible reasons:")
        print("- The website does not exist.")
        print("- There is an issue with your internet connection.")
        print("- The website may be down or unreachable.")
        print("Error details:", str(e))
        print()
        sys.exit(1)

    return results

def print_results(results):
    for header, info in results.items():
        if info['status'] == 'Implemented':
            print(f"{header}: \033[92m{info['status']}\033[0m - {info['value']}")
            print()
        else:
            print(f"{header}: \033[91m{info['status']}\033[0m")
            print(f"Description: {info['description']}")
            print("Solution: Implement the missing security header.")
            print()

if __name__ == "__main__":
    try:
        while True:
            website = input("Enter The Website Domian Name To Analyze: ")
            print()
            results = check_security_headers(website)
            print_results(results)
            print()
            perform_another_scan = input("Do you want to perform another scan? (yes/no): ").strip().lower()
            if perform_another_scan != 'yes':
                break
    except KeyboardInterrupt:
        print("\nUser interrupted. Exiting...")
        sys.exit(0)
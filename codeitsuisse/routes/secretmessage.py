import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def evaluateSecretMessage():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for test_case in data:
        result.append(encrypt(test_case["n"], test_case["text"]))
    logging.info("My result :{}".format(result))
    return jsonify(result);

def encrypt(n,text):
    processedtext = ""
    list_of_strings = []

    for i in text:
        if i.isalnum():
            processedtext += i.upper()

    if len(processedtext)//n < 1:
        return(processedtext)

    start = 0
    for j in range(n):
        length = len(processedtext) // n
        remainder = len(processedtext) %n
    
        if j < remainder:
            length += 1
        substring = processedtext[start:start + length]
        list_of_strings.append(substring)
        start += length
    print(list_of_strings)
    result = ''
    for i in range(len(processedtext)):
        listIndex = i % n
        index = i // n
        result += list_of_strings[listIndex][index]

    return(result)
import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSalad():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    numberValue = data.get("number_of_salads");
    saladList = data.get("salad_prices_street_map");
    result = leastCostCombination(numberValue,saladList)
    logging.info("My result :{}".format(result))
    return jsonify({"result":result});

def leastCostCombination(n,S):
    validmethods = []
    for lists in S:
        ps = 0
        for i in range(len(lists)-n+1):
            try:
                summ = 0
                for j in range(n):
                    int(lists[j+ps])
                    summ += int(lists[j+ps])
                validmethods.append(summ)
                ps += 1
            except:
                ps += 1
    if len(validmethods) == 0:
        return(0)
    return(min(validmethods))


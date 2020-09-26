import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def mopping():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = cleanfloor(data["tests"])
    logging.info("My result :{}".format(result))
    return jsonify({"answers":result});

def cleanfloor(dictionary):
        solution = {}
        for i in dictionary:
                floor = dictionary[i]["floor"]
                solution[i] = mop(floor)
        return(solution)

     
def mop(floor):
        global position
        global actions
        if sum(floor) == 0:
                del(position)

                return(actions)

        try:
                position
        except NameError:
                position = 0
                actions = 0
        
        if floor[position] == 0 and position != len(floor)-1:
                floor[position + 1] = abs(floor[position + 1]-1)
                actions += 1
                position += 1
                return(mop(floor))

        if floor[position] == 0:
                floor[position - 1] = abs(floor[position - 1]-1)
                actions += 1
                position -= 1
                return(mop(floor))


        elif floor[position] == 1 and position != len(floor)-1:
                floor[position + 1] = abs(floor[position + 1]-1)
                floor[position] -= 1
                actions += 2
                return(mop(floor))

        elif floor[position] == 1:
                floor[position - 1] = abs(floor[position - 1]-1)
                floor[position] -= 1
                actions += 2
                return(mop(floor))
        
        elif floor[position] > 1 and position != len(floor)-1:
                actions += floor[position]//2*4
                floor[position + 1] -= floor[position]//2*2
                floor[position] -= floor[position]//2*2
                if floor[position +1]< 0:
                        floor[position + 1]= floor[position + 1]%2
                return(mop(floor))

        elif floor[position] > 1:
                actions += floor[position]//2*4
                floor[position - 1] -= floor[position]//2*2
                floor[position] -= floor[position]//2*2
                if floor[position - 1]< 0:
                        floor[position - 1]= floor[position - 1]%2
                return(mop(floor))

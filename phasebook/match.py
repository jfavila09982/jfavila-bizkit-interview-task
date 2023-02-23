import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    set1 = set(fave_numbers_1)
    set2 = set(fave_numbers_2)

    return len(set1.intersection(set2))
    '''
    Description of refactoring code
    -----------------------------------------------
    #This code might takes too long and complexity can be (O*m ) wherein
    we need to iterate through the length of fave_numbers_2 just to match each number or element. 
    This would be takes too long if we have large data set or have long lists of favorite numbers.
    For this given scenario we can use Intersection method to improve the matching algorithm.
    Since our goal is to only find matching users based on their favorite numbers,  
    intersection built in method return a set that contains the similarity between sets.
    '''

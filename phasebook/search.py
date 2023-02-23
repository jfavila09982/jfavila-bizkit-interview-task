from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):

    

    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    
    matching_users = USERS

    id_users = []
    name_users = []
    age_users = []
    occupation_users = []
    
    uniq_occupation_users = []
    # filter by id if provided
    if "id" in args:
        id_users = [user for user in matching_users if user["id"] == args["id"]]

    if "name" in args:
        # making search a case-insensitive and match partial names
        query = args["name"].lower()
        matching_name_users = [user for user in matching_users if query in user["name"].lower() or (len(query) > 1 and query[:2] in user["name"].lower())]
        
        for name in matching_name_users:
            if name not in name_users:
                name_users.append(name)

    if "age" in args:
        age = int(args["age"])
        age_users = [user for user in matching_users if user["age"] in range(age-1, age+2)]


    if "occupation" in args:
        # make search case-insensitive and match partial occupations
        
        occupation_user = [user for user in matching_users if args["occupation"].lower() in user["occupation"].lower()]
   
        for user in matching_users:
            if "occupation" in user and args["occupation"].lower() in user["occupation"].lower():
                if user not in uniq_occupation_users:
                    uniq_occupation_users.append(user)
    # combine the results of each search criteria
    results = id_users + name_users + age_users + uniq_occupation_users

    return results

    

    #if request.args['age'] == name:
         #result.append(next(user for user in USERS if user["age"] == request.args.get("name")))
    '''
    elif request.args['age'] == age:
         result.append(next(user for user in USERS if user["for"] == request.args.get("for")))
    elif request.args['occupation'] == name:
         result.append(next(user for user in USERS if user["occupation"] == request.args.get("occupation")))
    '''
    
    #return next(user for user in USERS if user["id"] == request.args.get("id"))
    
    



    

    
    
    
 
        

    

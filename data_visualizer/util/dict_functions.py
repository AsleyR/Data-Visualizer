import re

def convert_dict_to_list(dict_list, *, with_keys=False):
    if type(with_keys) != bool:
        raise ValueError(f"'with_keys' must be a boolean")

    result_list = []
    for iteration in range(len(dict_list)):
        item_list = []
        if with_keys == True:
            for key in dict_list[iteration].keys():
                item_list.append(key)
                item_list.append(dict_list[iteration].get(key))
        elif with_keys == False:
            for value in dict_list[iteration].values():
                item_list.append(value)

        result_list.append(item_list)
    return result_list

# Take list of dicts and outputs only desired dicts
# into another list
def get_desired_dicts(dictionary, param):
    result = []
    for iteration in range(len(dictionary)):
        for key in dictionary[iteration].keys():
            if key == param:
                result.append({key: dictionary[iteration].get(key)})
    
    return result

# LIST OF DICTS
def get_dict_keys(dictionary):
        dictionary = dictionary[0]
        keys = []
        for key in dictionary.keys():
            keys.append(key)
        return keys

# LIST OF DICTS
def get_dict_values(dictionary):
    values = []
    for iteration in range(len(dictionary)):
        value_list = []
        for value in dictionary[iteration].values():
            value_list.append(value)
        values.append(value_list)
    return values

# DISGUSTING FUNCTION, CHANGE NEEDED!
def search_dict(data, search_item, search_param=''):
    item_list = []
    if search_param == "":
        for i in range(len(data)):
            for value in data[i].values():
                # print(value)
                search = re.search(search_item, value, re.IGNORECASE)
                if search:
                    item_list.append(data[i])

    else:
        for i in range(len(data)):
            for key in data[i].keys():
                if key == search_param:
                    value = data[i].get(key)
                    search = re.search(search_item, value, re.IGNORECASE)
                    if search:
                        item_list.append(data[i])
                else:
                    pass
    return item_list
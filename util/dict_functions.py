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
    print(result_list)
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


def test_function(dict, *, with_headings: bool = False):
    if type(with_headings) != bool:
        raise ValueError("'with_headings' argument must be a boolean")
    
    if with_headings != False:
        print("Yes")
    else:
        print("No")
    print(dict)

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
        print(item_list)

    else:
        for i in range(len(data)):
            for key in data[i].keys():
                if key == search_param:
                    print(key)
                    value = data[i].get(key)
                    search = re.search(search_item, value, re.IGNORECASE)
                    if search:
                        item_list.append(data[i])
                else:
                    pass
        print(item_list)
    return item_list


ed = {
    "Color": "Blanco",
    "Brand": "SAMSUNG",
    "Size": "20",
    "Tech": "Good"
}

ed1 = {
    "Color": "Negro",
    "Brand": "Huawei",
    "Size": "15",
    "Tech": "Bad"
}

prueba = [
    {'\ufeffId Cliente': '4200', 'Cliente': 'REDCAMIF - J0810000136761', 'Id vendedor': '25', 'Vendedor': 'Ana Flores Rodriguez', 'Id producto': '30228392', 'Producto': 'Toa Scott airflex MF 1P 25x1x150 hjs.', 'Cantidad': '25', 'Venta': '1607', 'Mes': 'Apr-22'}, {'\ufeffId Cliente': '4204', 'Cliente': 'CREACIONES GARCIA ROMERO', 'Id vendedor': '33', 'Vendedor': 'Massiel Rivera Herrera', 'Id producto': '30223334', 'Producto': 'Kcp Pap Hig JRT Scott Exp 1P 6x1x400 mts.', 'Cantidad': '6', 'Venta': '547.98', 'Mes': 'Apr-22'}
]

ed3 = [ed, ed1]

new_d = {}

# mierda = get_desired_dicts(ed3, "Color")
# # print(mierda)
# convert_dict_to_list(prueba, with_keys=False)
search_dict(prueba, "red", 'Cliente')

# test_function(ed)
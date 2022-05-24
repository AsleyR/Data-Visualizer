import re

class searchFunctions:
    def __init__(self, data):
        self.data = data

    # Get all lines in dict that falls with the params
    def update_data(self, param, item):
        item_list = []
        for line in self.data:
            if line.get(param) == item:
                item_list.append(line)
            else:
                pass
        return item_list

    # Search items from search bar in data
    def search_item(self, search_value):
        item_list = []
        data = self.data
        for i in range(len(data)):
            for value in data[i]:
                search = re.search(search_value, data[i]) # Regex search
                if search:
                    item_list.append(data[i])
        print(item_list)
        return item_list

    # Returns only 1 iteration of item in list
    def look_for_item(self, param, item):
        item_list = []
        for line in self.data:
            if line.get(param) == item:
                if line.get(param) in item_list:
                    pass
                else:
                    item_list.append(line.get(param))
        return item_list

    # Returns all items from section. ex: All vendedores
    def get_all_specific_items(self, item):
        item_list = []
        for value in self.data:
            if value.get(item) in item_list:
                pass
            else:
                item_list.append(value.get(item))
        return item_list


def busqueda_prubea(data, search_item, *, search_param=""):
    if type(search_param) != str:
        raise ValueError("'search_param' argument must be a string")
    
    item_list = []
    if search_param != '':
        for i in range(len(data)):
            for key in data[i].keys():
                if key == search_param:
                    item_list.append({key: data[i].get(key)})
                else:
                    pass
    else:
        for i in range(len(data)):
            for value in data[i]:
                print(value)
                search = re.search(search_item, value)
                if search:
                    item_list.append(data[i])
                    # print(data[i])

    print(item_list)
    return item_list

# Take list of dicts and searchs for a specific param
# It can do two things:
# 1) Search in list of dict with only search param or
# 2) Search in list of dict search param found inside the key of header param
# ex 2: {'is_potato': 'yes'} -> search 'yes' in 'is_potato' 
def busqueda_dos_dict(data, search_param, header_param=""):
    item_list = []
    # if type(header_param) == str:
    #     raise ValueError("'header_param' must be a string!")

    # if header_param == "":
    #     for i in range(len(data)):
    #         for value in data[i]:
    #             search = re.search(search_param, value)
    #             if search:
    #                 item_list.append(data[i])
    #     return item_list

    if header_param == "":
        for i in range(len(data)):
            for value in data[i].values():
                # print(value)
                search = re.search(search_param, value)
                if search:
                    item_list.append(data[i])
        print(item_list)

    else:
        for i in range(len(data)):
            for key in data[i].keys():
                if key == header_param:
                    print(key)
                    value = data[i].get(key)
                    search = re.search(search_param, value)
                    if search:
                        item_list.append(data[i])
                else:
                    pass
        print(item_list)
        return

prueba = [
    {'\ufeffId Cliente': '4200', 'Cliente': 'REDCAMIF - J0810000136761', 'Id vendedor': '25', 'Vendedor': 'Ana Flores Rodriguez', 'Id producto': '30228392', 'Producto': 'Toa Scott airflex MF 1P 25x1x150 hjs.', 'Cantidad': '25', 'Venta': '1607', 'Mes': 'Apr-22'}, {'\ufeffId Cliente': '4204', 'Cliente': 'CREACIONES GARCIA ROMERO', 'Id vendedor': '33', 'Vendedor': 'Massiel Rivera Herrera', 'Id producto': '30223334', 'Producto': 'Kcp Pap Hig JRT Scott Exp 1P 6x1x400 mts.', 'Cantidad': '6', 'Venta': '547.98', 'Mes': 'Apr-22'}
]

mier = ['1', '2', '3', '4']

potato = [['4200', 'REDCAMIF - J0810000136761', '25', 'Ana Flores Rodriguez', '30228392', 'Toa Scott airflex MF 1P 25x1x150 hjs.', '25', '1607', 'Apr-22'], ['4204', 'CREACIONES GARCIA ROMERO', '33', 'Massiel Rivera Herrera', '30223334', 'Kcp Pap Hig JRT Scott Exp 1P 6x1x400 mts.', '6', '547.98', 'Apr-22'], ['he', 'ha', 'potato']]

# search = busqueda_prubea(potato, 'potato')
# print(search.search_item('4200'))

fit = []
# print(prueba[0].items())

# mpro = [1, 2, 3]
# pore = ['f', 'e', '3']
# fetulencia = dict(mpro = pore)
# print(fetulencia)

busqueda_dos_dict(prueba, "REDCAMIF", 'Cliente')
# print(len(fit)
# print(search)


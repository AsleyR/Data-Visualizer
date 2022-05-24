import csv
import re

# Id Cliente,Cliente,Id vendedor,Vendedor,Id producto,Producto,Cantidad,Venta,Mes

class csvData:
    def __init__(self, file_location):
        self.file_location = file_location
        self.data = []

    # data = [1, 2, 3, 4]
    def create_data_array(self):
        with open(self.file_location, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = self.data
            for line in csv_reader:
                data.append(line)
            csv_file.close() # Remember to always close files
            return data

    # data = {1:'A', 2:'B', 3:'C', 4:'D'}
    def create_data_dict(self):
        with open(self.file_location, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = self.data
            for line in csv_reader:
                data.append(line)
            csv_file.close() # Remember to always close files
            return data
    

class searchFuntions:
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
        
        values = []
        for iteration in range(len(item_list)):
            value_list = []
            for value in item_list[iteration].values():
                value_list.append(value)
            values.append(value_list)
        return values

    # Search items from search bar in data
    def search_item(self, search_value, data_file):
        data = self.data
        csv_data = csvData(data_file)
        data = csv_data.get_dict_values(self.data)
        item_list = []
        for i in range(len(data)):
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
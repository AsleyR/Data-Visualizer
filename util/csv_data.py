import csv

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

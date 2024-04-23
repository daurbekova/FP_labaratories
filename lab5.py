# Функциональное Декомпозирование
# -	Создать серию взаимосвязанных ленивых функций, каждая из которых выполняет одно действие в цепочке обработки данных
def lazy_load_data(source):
    print("Loading data from:", source)
    return [1, 2, 3, 4, 5]
def lazy_preprocess_data(data):
    print("Preprocessing data")
    return [x * 2 for x in data]
def lazy_filter_data(data):
    print("Filtering data")
    return [x for x in data if x > 3]
def lazy_transform_data(data):
    print("Transforming data")
    return [x ** 2 for x in data]
def lazy_save_data(data, destination):
    print("Saving data to:", destination)
    # Here you can implement saving logic
    print("Data saved successfully")
def data_processing_pipeline(source, destination):
    data = lazy_load_data(source)
    data = lazy_preprocess_data(data)
    data = lazy_filter_data(data)
    data = lazy_transform_data(data)
    lazy_save_data(data, destination)
data_processing_pipeline("input_data.txt", "output_data.txt")

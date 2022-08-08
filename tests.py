import parse
import data_store
import core


parse.start_parse()
item = data_store.dataSaver._data["Orfen"]

print (core.calc_time_for_boss("Orfen", item))
print(data_store.dataSaver._unic_bos)
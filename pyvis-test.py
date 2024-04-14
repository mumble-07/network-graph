from pyvis.network import Network
import json

file = "./json_files/alcuin_letters.json"

def get_data(): 
  with open (file, "r") as json_file: 
    data = json.load(json_file)
    return(data)
  
epp_data = get_data()

print(epp_data)
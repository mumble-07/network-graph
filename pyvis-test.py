from pyvis.network import Network
import json

file = "json_files/alcuin_letters.json"

def get_data(): 
  with open (file, "r") as json_file: 
    data = json.load(json_file)
    return(data["alcuin_letters"])
  
# epp_data = get_data()
# print(epp_data)

def map_data(letter_data, ep_color="#03DAC6", ms_color="#da03b3", edge_color="#018786"):
  g = Network(height="100vh", width="1500px", bgcolor="#222222", font_color="white")

  for letter in letter_data:
    ep = (letter["ep_num"])[0]
    mss = (letter["mss"])
    g.add_node(ep, color=ep_color)
    for ms in mss:
      g.add_node(ms, color=ms_color)
      g.add_edge(ep, ms, color=edge_color)

  # g.barnes_hut()
  g.show("letters.html", notebook=False)


epp_data = get_data()
map_data(letter_data=epp_data)
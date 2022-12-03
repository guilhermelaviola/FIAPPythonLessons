# Dictionary example with football players

# Empty dictionary
players={}

# Populating the dictionary with several players at once
players={
    "Lukaku":["Romelu Lukaku","90","2019/20"],
    "Barella":["Nicolò Barella","23","2019/20"],
    "Mkhitaryan":["Henrikh Mkhitaryan","22","2022/23"],
    "Skriniar":["Milan Skriniar","37","2017/18"],
    "Onana":["André Onana","26","2022/23"],
    "Lautaro":["Lautaro Martínez","10","2018/19"]
    }

# Inserting more players into the dictionary, but now one at a time
players["Çalhanoglu"]=["Hakan Çalhanoglu", "20", "2021/22"]
players["Brozovic"]=["Marcelo Brozovic", "77", "2014/15"]

# Displaying the dictionary
print(players)
print("--------------------------------------------------------------------")

# Displaying the element with the key "Lukaku"
print(players.get("Lukaku"))


def str_to_b(str: str):
    result = ""
    for i in str:
        if i.lower() == "a":
            result += "00"
        if i.lower() == "c":
            result += "01"
        if i.lower() == "g":
            result += "10"
        if i.lower() == "t":
            result += "11"
    return int(result, 2)

def b_to_str(b):
    octets = bytes(b)
    return octets.decode('utf-8')

def encode_adn(path):
    with open(path, "r") as r:
        with open("result.bin", "wb") as w:
            while True:
                txt = r.read(4)
                if txt == "":
                    break
                b = str_to_b(txt)
                w.write(bytes([b]))
    
encode_adn("bac_1/C_algo/TP/TP_3/adn.txt")
            
a={
"rajeev": ["father"],
"archana": ["mother"],
"tushar": ["big brother"],
"vishal":["middle brother"],
"om":["small brother"]
}
print(a.keys())
print(a.values())
print(a.items())
print(a)
b={
    "rajeev": ["papa"],
    "state" : ["uttarpradesh"]
}
a.update(b)
print(a)
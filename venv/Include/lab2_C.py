A = (["a",1],["b",2],["c",3],["d",4],["e",5],["f",6]) # задание №3
D = dict(A)
print(D.keys())   #a
print(D.get("d")) #b
print(D.items()) #c
print(D.setdefault("as","NONE")) #d
D.clear()

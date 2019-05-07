dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %s" %(dictionary_tk["nationality"])) # And by the way I'm Brazilian

#### Adding new elements on Dictionary

dictionary_tkcheck = {
  "name": "David",
  "nickname": "Tk",
  "nationality": "Vietnamese"
}

dictionary_tkcheck['age'] = 24

print(dictionary_tkcheck) # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}

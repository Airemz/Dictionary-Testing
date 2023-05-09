x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]

#print(x[2])
menu = {'Hamburger' : 4.5, 'Pizza' : 5, 'Falafel' : 3, 'Fanta' : 1, "no":{"food": 5,"dog": 2}}

menu["sub"]=6
print(menu.get("Hamburger"))
print(menu)

# del menu["Pizza"]
# print(menu)

menu.pop("Pizza")


# for key, value in menu.items():
#   if type(key)==dict:
#     for key2, value2 in value.items():
#       print (key2,value2)

#   else:
#    print(key, value)

# for key in menu.keys():
#   if type(key)==dict:
#     for key2, value2 in value.items():
#       print (key2,value2)

  # else:
  #  print(key)

print(menu["no"]["food"])
#x = ['a', 'b', {'foo': 1,'bar': { 'x' : 10,'y' : 20,'z' : 30},'baz': 3},'c','d']
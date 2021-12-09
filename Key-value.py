object = {
    'a'  : {
		    'b' : {
			      'c' : {
				            "d"
			            }
		          }
           	}
}

key_input = input(print (" enter the key :  "))
key_str = key_input.split('/')
keys = list(key_str)

for key in keys :
    if key != 'd' : 
        object=object.get(key)
print(f' value of entered key is : {object}')
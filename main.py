# create (name) : boolean
# read(index) : name
# readByName(name) : name[]
# existsByName (name) : boolean
# update (oldName, newName) : boolean
# deleteByName(name) : boolean
# deleteByIndex(index) : boolean
# show() 


import example as ex

def main():
	while True:
		action = input("Input action\n"\
			"create (c)\n"\
			"read by index (ri)\n"\
			"read by name (rn)\n"\
			"existsByName (e)\n"\
			"update (u)\n"\
			"delete by name (dn)\n"\
			"delete by index (di)\n"\
			"show (s)\n"\
			"quit (q)\n"\
			)
		if action.lower() == "c":
			name = input("Input new name - ")
			name = name.capitalize()
			ex.create_name(name)

		elif action.lower() == "ri":
			ex.read_name_by_index()

		elif action.lower() == "rn":
			ex.read_by_name()
		
		elif action.lower() == "e":
			ex.exists_by_name()

		elif action.lower() == "u":
			name = input("Input old name to find- ")
			name = name.capitalize()
			ex.update_name(name)

		elif action.lower() == "dn":
			ex.delete_by_name()

		elif action.lower() == "di":
			ex.delete_by_index()	
			
		elif action.lower() == "s":
			ex.show_all()

		elif action.lower() == "q":
			break
			
		else:
			print("Please input correct agan !")	
main()	
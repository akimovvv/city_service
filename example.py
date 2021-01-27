

names = []


def check_name(name):
	if len(name) >= 4 and name not in names:
		return True
	return False


def create_name(name):
	if check_name(name) == True:
		names.append(name)
		print("Sucsess !")
	else:
		print("This name also in list or menshe 4 bukv")


def read_name_by_index():
	if len(names) > 0:
		name_index = int(input(f"Please input a index (1 do {len(names)}) to show name by index - "))
		if name_index <= len(names):
			print(names[name_index - 1])
		else:
			print("Something went wrong please try agan !")
	else:
		print("List is empty input something !")	


def read_by_name():
	if len(names) > 0:
		name = input("Input name to find - ")
		name = name.capitalize()
		if name in names:
			iname = names.index(name)
			print(f"Yuor name {name} in list {iname + 1} ")
		else:
			print("Something went wrong please try agan !")
	else:
		print("List is empty input something !")


def exists_by_name():
	if len(names) > 0:
		a = input("Input something to find a close words - ")
		b = a.capitalize()
		matching = [_ for _ in names if a in _]
		matching1 = [_ for _ in names if b in _]
		if len(matching) > 0:
			print("Found this names -", matching)
		elif len(matching1) > 0:
			print("Found this names -", matching1)	
		else:
			print(f"Not found anything by this keys {a} !")
	else:
		print("List is empty input something !")


def update_name_check(name):
	if len(names) > 0:
		if name in names:
			return True
		return False
	else:
	 	print("List is empty input something !")

		
def update_name(name):		
	if update_name_check(name) == True:
		name_new = input("Input new name to insert - ")
		name_new = name_new.capitalize()
		if len(name_new) >= 4 and name_new not in names:
			index = names.index(name)
			names.remove(name)
			names.insert(index,name_new)
			print("Sucsess you update\n"\
			f"{name} on {name_new}!")
		else:
			print("This name also in list or menshe 4 bukv")	
	else:
		print("Something went wrong please try agan !")


def delete_by_name():
	if len(names) > 0:
		print (names)
		delete = input("Input delete name - ")
		delete = delete.capitalize()
		if delete in names:
			names.remove(delete)
			print(f"This name {delete} is delete !")
		else:
			print("Something went wrong please try agan !")
	else:
		print("List is empty input something !")


def delete_by_index():
	if len(names) > 0:
		print (names)
		delete_index = int(input(f"Input posithion 1 -{len(names)} to delete name - "))
		names.pop(delete_index - 1)
	else:
		print("List is empty input something !")


def show_all():
	print(names)

'''
--Conceptual script: mission BASIC 06 of hackthissite--
----https://www.hackthissite.org/missions/basic/6/ ----
'''

def password_enc():
	name = raw_input("Password: ")
	new_name = ""
	x = 0
	for i in name:
		o = ord(i) + x
		x += 1
		new_char = chr(o)
		new_name += new_char

	return new_name

if __name__ == "__main__":
	print(password_enc())
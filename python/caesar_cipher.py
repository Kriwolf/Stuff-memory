'''
--Conceptual script: mission BASIC 06 of hackthissite--
----https://www.hackthissite.org/missions/basic/6/ ----
'''

def password_enc():
	passw = raw_input("Password: ")
	new_passw = ""
	x = 0
	for i in passw:
		o = ord(i) + x
		x += 1
		new_char = chr(o)
		new_passw += new_char

	return new_passw

if __name__ == "__main__":
	print(password_enc())

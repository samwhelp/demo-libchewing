#!/usr/bin/env python3

from chewing import userphrase

def main():

	list = userphrase.find_all()

	##print(list)

	for item in list:
		print()
		print('phrase:', item[0])
		print('bopomofo:', item[1])

if __name__ == '__main__':
	main()

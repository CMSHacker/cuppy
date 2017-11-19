#!/usr/bin/python
#
# A UNIX Password Cracker
#
# Scripte by CMSHacker
#
#

import crypt
import sys
import os

def testPass(cryptPass, fileDict) :
	salt = cryptPass[0:2]
	dictFile = open(fileDict, 'r')
	for word in dictFile.readlines() :
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if cryptWord == cryptPass :
			print "[+] Found password : %s \n" % (word)
			return
	print "[-] Password Not Found \n"
	return

def main() :
	if len(sys.argv) == 3 :
		filePass = sys.argv[1]
		fileDict = sys.argv[2]
		if not os.path.isfile(filePass) or not os.path.isfile(fileDict) :
			print "[!] Error : File does not exist"
			exit(0)
		if not os.access(filePass, os.R_OK) or not os.access(fileDict, os.R_OK) :
			print "[!] Error : Access Denied!"
			exit(0)
		getPass(filePass, fileDict)
	else :
		print "[!] Usage : %s <Password-File> <Dictionary>" % (sys.argv[0])
	
def getPass(filePass, fileDict) :
	passFile = open(filePass, 'r')
	for line in passFile.readlines() :
		if ":" in line :
			user = line.split(":")[0]
			cryptPass = line.split(":")[1].strip('\n')
			print "Cracking Password For : %s " % (user) 
			testPass(cryptPass, fileDict)

if __name__ == '__main__' :
	main()

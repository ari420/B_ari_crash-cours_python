#from pathlib import Path

#path = Path('cc10_dt/cc10test3.py')

#path.write_text('#i love python :)')





from pathlib import Path

path2 = Path('cc10_dt/cc10test3.py')

massag = '#what up\n\n'
massag +='#how are you doing\n'
massag +='#was it usefull\n'
path2.write_text(massag)
    



####replace method
#from pathlib import Path
#
#path3 = Path("cc10_dt/cc10test2.py")
#read3 = path3.read_text()
#print(read3)
#print(f'\n\n\n\n')
#
#string2 = ''
#lines = read3.splitlines()
#for lines in lines:
#    string2 = lines + string2
#
#ms = string2
#x = ms.replace('and','haha')    
#
#print (string2.split())
#print(f'\n\n\n\n')
#print (x)





#####relative  path 
#from pathlib import Path
#path = Path('cc10_imported.py')
#read = path.read_text()
#print(read)
#
#
#print('----------------------------------------------------------------------------------------------')
#
####absolute path 
#path2 = Path("cc10_dt/cc10test.py")
#read2 = path2.read_text()
#print(read2)
#
#
#
#print('----------------------------------------------------------------------------------------------')
#
#
#
####file content useing 
#string = ''
#lines = read2.splitlines()
#for lines in lines:
#    string = lines + string
#
#print (string.split())
#
#
#
#print('----------------------------------------------------------------------------------------------')
#
#
#
#
####my practic test fore you 
#path3 = Path("cc10_dt/cc10test2.py")
#read3 = path3.read_text()
#print(read3)
#
#string2 = ''
#lines = read3.splitlines()
#for lines in lines:
#    string2 = lines + string2
#
#print (string2.split())
#
#
#print('----------------------------------------------------------------------------------------------')
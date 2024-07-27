










id_dic = {
    "shrry":{
        'name':'shaghaygh',
        'lastname':'ghiasi',
        'location':'canada',
    },
    'arian':{
        'name':'arian',
        'lastname':'afsharian',
        'location':'iran',
    },
}
for shrry , arian in id_dic.items():
    print(f'shrry: {id_dic} \n')
    information1 = f'{shrry["name"]}\n{shrry["lastname"]}'
    information2 = f'{arian["name"]}\n{arian["lastname"]}'
    loc = f'{shrry["location"]}'
    loc2 = f'{arian["location"]}'
    print(f'{information1}')
    print(loc)
    print(f'{information2}')
    print(loc2)












items = ['kitka','snikers','m and m','hobby','cheps']
print (f" from menue bloue chose  your order pless:)\n\t-------------------------------\n{items}")
print ('===========================================')
c_list = {'sumorder': 0}
order = str(input('enter you choise:)=>'))
c_list['costomerord'] = order
order2 = str(input('enter you choise:)=>'))
c_list['costomerord2'] = order2
order3 = str(input('enter you choise:)=>'))
c_list['costomerord3'] = order3
order4 = str(input('enter you choise:)=>'))
c_list['costomerord4'] = order4
order5 = str(input('enter you choise:)=>'))
c_list['costomerord5'] = order5
for c_list in c_list :
    if c_list['costomerord'] == 'kitka':
        print (f'wounderful choes')
        x = x + 1
    elif c_list['costomerord2'] == 'snikers':
        print(f'wonderful chose')  
        x = x + 1
    elif c_list['costomerord3'] == 'm and m':
        print(f'wonderful chose')
        x = 1 + x  
    elif c_list['costomerord4'] == 'hobby':
        print(f'wonderful chose')
        x = 1 + x   
    elif c_list['costomerord5'] == 'chaps':
        print(f'wonderful chose') 
        x = 1 + x
    else:
        print(f'sorry i do not have your item:/:(')
        x = 0 + x

c_list['sumorder']= x
print (c_list)  


                 








#arian = {'arian','ali','sherry','roham'}
#print(arian)
#arian.add('david')
#print(arian)
#arian.remove('ali')
#print(arian)
#for arian in arian:
#    arian
#    if 'sherry' in arian:
#        print('--------------')
#        print(arian,'thats my untiy')
#        print('--------------')
#    if 'david' in arian:
#        print('--------------')
#        print(arian , 'my homie')
#        print('---------------')
#    if 'roham' in arian:
#        print('--------------')
#        print(arian , 'my friend')
#        print('---------------')
#    if 'arian' in arian:
#        print('--------------')
#        print(arian , 'and finaly here i am')
#
#
#        print('---------------')

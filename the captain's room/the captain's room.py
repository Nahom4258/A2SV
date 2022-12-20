K = 0
room_list = ''
mydict = dict()

K = input()

room_list = input().split(' ')

for room in room_list: 
    if room in mydict:
        mydict[room] = str(int(mydict[room]) + 1)
    else:
        mydict[room] = str(1)
      
captain_room = ''  
for captain in mydict.items():
    if captain[1] == '1':
        captain_room = captain[0]
        
print(captain_room)

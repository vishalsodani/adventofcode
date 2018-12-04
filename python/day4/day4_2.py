inputs = []
i = 0


with open('input.txt') as fp:
    for input in fp:
        data = input.split(']')
        datedata = long(data[0][1:5]+ data[0][6:8] + data[0][9:11] + data[0][12:14]+data[0][15:17])
        if 'Guard' in input:
            inputs.append([ datedata, {'id':data[1].split('#')[1].split('b')[0].strip()}])
        else:
            if 'asleep' in data[1]:
                inputs.append([datedata, {'guard_status':0}])
            if 'wakes' in data[1]:
                inputs.append([datedata, {'guard_status':1}])
        i = i + 1

inputs.sort(key=lambda x: x[0])
guards = {}
running_id = None
last_slept_at = 0

for data in inputs:
   
    if 'id' in data[1]:
        if data[1]['id'] not in guards:
            guards[data[1]['id']] = {'totalsleep':0, 'sleptatminute':{}}
        running_id = data[1]['id']
        last_slept_at = 0
    else:
        if 'guard_status' in data[1]:
           if data[1]['guard_status'] == 0:
               sleptat = str(data[0])[-2:]
               last_slept_at = int(sleptat)
               if sleptat not in guards[running_id]['sleptatminute']:
                   guards[running_id]['sleptatminute'][sleptat] = 1
               else:
                   guards[running_id]['sleptatminute'][sleptat] += 1
           if data[1]['guard_status'] == 1:
              awakeat = int(str(data[0])[-2:])
              guards[running_id]['totalsleep'] += awakeat - last_slept_at
              for i in range(last_slept_at + 1, awakeat):
                inpumin = str(i)
                if inpumin not in guards[running_id]['sleptatminute']:
                   guards[running_id]['sleptatminute'][inpumin] = 1
                else:
                   guards[running_id]['sleptatminute'][inpumin] += 1
                
max_slept_at = 0
guardid = 0
guard_most_asleep = {'guardid':0, 'most_slept_at':0, 'times_slept':0}

for key, data in guards.iteritems():
    sleptat_collection = data['sleptatminute']
    for innerkey, value in sleptat_collection.iteritems():
        if value > guard_most_asleep['times_slept']:
            guard_most_asleep['guardid'] = key
            guard_most_asleep['most_slept_at'] = innerkey
            guard_most_asleep['times_slept'] = value
    

print(int(guard_most_asleep['guardid']) * int(guard_most_asleep['most_slept_at']))


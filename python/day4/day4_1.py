inputs = []
import re

with open('input.txt') as fp:
    for input in fp:
        data = input.split(']')
        regex = re.search('(?<=\[)(.*?)(?=\])', input)
        datedata = regex.group(0).replace('-','').replace(' ','').replace(':','')
        if 'Guard' in input:
            inputs.append([ datedata, {'id':data[1].split('#')[1].split('b')[0].strip()}])
        else:
            if 'asleep' in data[1]:
                inputs.append([datedata, {'guard_status':0}])
            if 'wakes' in data[1]:
                inputs.append([datedata, {'guard_status':1}])
        
inputs.sort(key=lambda x: x[0])
guards = {}
running_id = None
last_slept_at = 0

for data in inputs:
    second_part = data[1]
    if 'id' in second_part:
        guards_id = second_part['id']
        if guards_id not in guards:
            guards[guards_id] = {'totalsleep':0, 'sleptatminute':{}}
        running_id = guards_id
        last_slept_at = 0
    else:
        
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
            

           
           
max_sleep_minutes = 0
guardid = 0
for key, data in guards.iteritems():
    if data['totalsleep'] > max_sleep_minutes:
        guardid = key
        max_sleep_minutes = data['totalsleep']
        
all_minutes = guards[guardid]['sleptatminute']
max_slept_at = 0
max_slept_at_minute = 0

for key, data in all_minutes.iteritems():
    if data > max_slept_at:
        max_slept_at = data
        max_slept_at_minute = key

print('ANSWER')        
print(guardid)
print(max_slept_at_minute)
print(int(guardid) * int(max_slept_at_minute))
    
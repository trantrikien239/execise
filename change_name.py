import os


list_name = os.listdir()
name_data = {}
for name in list_name:
    name_data[name] = {}
    try:
        practice_number = int(name.split('_')[0])
    except:
        practice_number = -1
    if practice_number > 0:
        name_data[name]['needed_changing'] = True
        new_name = '_'.join(name.split('_')[1:])
        new_name = new_name[:-3]+'_'+str(practice_number)+'.py'
        name_data[name]['new_name'] = new_name
    else:
        name_data[name]['needed_changing'] = False
print(name_data)

for key,val in name_data.items():
    if val['needed_changing']:
        os.rename(key,val['new_name'])
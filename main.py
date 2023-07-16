from datetime import datetime
data = dict()
data['Name'] = str(input('Name: '))
birth = int(input('Year of birth: '))
data['Age'] = datetime.now().year - birth
data['Work card'] = int(input('Work card (0 do not have): '))
if data['Work card'] != 0:
    data['Hiring'] = int(input('Year of hire: '))
    data['Salary'] = float(input('Salary: R$'))
    data['Retirement'] = data['Age'] + ((data['Hiring'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in data.items():
    print(f'  - \033[4;33m{k}\033[m has the value \033[4;32m{v}\033[m')

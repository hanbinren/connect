# coding: utf-8
#import qdarkstyle
import ftrack_api.structure
import ftrack_api.entity
import ftrack_api.accessor
import ftrack_api
import arrow
session = ftrack_api.Session(
server_url='https://ckyh.ftrackapp.cn',
    api_key='OWM1ODBmMjktMTYxMi00YTVhLWFkMzAtODY3NjQ0NzE1OGI2Ojo1YzQ4YWE0Ny01OWFkLTQ4ODYtYWIzNC0yMWQwNzkwMTY5ZTQ',
    api_user='wangxiaowei@ckyhvfx.com')
# for i in sorted(session.types.keys()):
#     print i

# projects = session.query('Project')
# for b in projects:
#     if b['id'] == b['link'][0]['id']:
#         name = b['name']





# print projects
# for i in projects:
#     print i
# peo_id = session.query('Project where id is dayingjia_dyj')
# print peo_id
# for a in peo_id:
#     print a['id']
#
a = []
b= []
projects_2 = session.query('Project where name is dayingjia_dyj')
print projects_2[0]['children']
#print projects_2[0].items()
# for s in projects_2[0].items():
#     print s
#     a.append(s)

seq = session.query('Shot where name is 0060')
print seq[0].items()
print seq[0]['name']
for v in seq[0].items():
    print v
    b.append(v)
print '*'*99

seqs1 = projects_2[0]['children']
print seqs1
print seqs1[0]['name']

print seqs1[0]['object_type']['name']
print seqs1[0]['parent']['name']
print seqs1[0]['parent_id']
print projects_2[0]['id']
t = seqs1[0]['children']
print t[0]['children']

for a in t:
    print a['name']
# seqs = projects_2[0]['children']
# print seqs
#
# print seqs1['name']
# #print seqs1['object_type']['name']
#
# #
parent_name = []
tm = 0
ti = 1
print project_dict
print seq_dict
try:
    a = len([k for k, v in seq_dict.items()])
    self.textEteil1.setRowCount(a)
    for k, v in seq_dict.items():
        print k, v
        if v == 'Shot' or v == 'Asset Build' or v == 'Task':
            # if v == 'Sequence':
            ne = QTableWidgetItem(k)
            self.textEteil1.setItem(tm, 0, ne)
            se = str(v)
            ne = QTableWidgetItem(se)
            self.textEteil1.setItem(tm, ti, ne)
            tm += 1

            type_name = session.query('{0} where name is {1}'.format(v, k))
            type_par = type_name[0]['parent']
            name = type_par['name']
            print name
            parent_name.append(name)
            print parent_name
            self.textEteil.setPlaceholderText(str(name))

    a = len([k for k, v in project_dict.items()])
    self.textEteil1.setRowCount(a)
    for k, v in project_dict.items():
        print k, v
        if v == 'Sequence' or v == 'Folder' or v == 'Asset Build':
            ne = QTableWidgetItem(k)
            self.textEteil1.setItem(tm, 0, ne)
            se = str(v)
            ne = QTableWidgetItem(se)
            self.textEteil1.setItem(tm, ti, ne)
            tm += 1

            type_name = session.query('{0} where name is {1}'.format(v, k))
            type_par = type_name[0]['parent']
            name = type_par['name']
            print name
            parent_name.append(name)
            print parent_name
            self.textEteil.setPlaceholderText(str(name))
except Exception:
    pass




































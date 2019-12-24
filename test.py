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

seq = session.query('Sequence where name is asset')
print seq[0].items()
print seq[0]['parent']['name']
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
# # print seqs1.items()
# # print seqs1['id']
# seque = session.query('Sequence where name is asset')
# print seque[0]['parent']['name']

# for i in seqs1:
#     print i
#
# a = seqs1['object_type']
# b = str(a['name'])
# print b





#t = projects_3['name']
# for i,v in enumerate(t):
#     print t[i]['name']
# for i in sorted(session.types.keys()):
#     print i

# s =session.query('Project where Project.name is')
# print s
# for i in s:
#     print i['name']
#
#
# projects = session.query('Project where name is dayingjia_dyj')
# print projects
# print dir(projects)
# for a in projects:
#     print a['name']
#
# b = session.query('Sequence where project.name is "{0}"'.format(projects[0]['name']))
# print b

# A = session.query('select name,Project.children from Project')
# for i in A:
#     print 'i["name"]-i[0]["children"]'.format()
# print A




































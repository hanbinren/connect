import ftrack_api

# session = ftrack_api.Session(
#     server_url='https://ckyh.ftrackapp.cn',
#     api_key='MGVmZTdlODMtNzVkZC00MDBmLTllMGItNTFiZjgzZTRjZWI5Ojo0YzdkMTc5My05YzVlLTRkOTEtODZhNC05ZTgzMzdkNTM0OGE',
#     api_user='hanbin'
# )

session = ftrack_api.Session(
server_url='https://ckyh.ftrackapp.cn',
    api_key='OWM1ODBmMjktMTYxMi00YTVhLWFkMzAtODY3NjQ0NzE1OGI2Ojo1YzQ4YWE0Ny01OWFkLTQ4ODYtYWIzNC0yMWQwNzkwMTY5ZTQ',
    api_user='wangxiaowei@ckyhvfx.com')

a = []
b = []
projects_1 = session.query('Project where name is dayingjia_dyj' )
f = projects_1[0]['children']
c = projects_1[0]['id']
print c
for s in projects_1:
    print s['name']
    print s['id']
seq = session.query('Sequence where name is production')
print seq.all()
print
for a in seq[1]['children']:
    print a['name']

d = seq[0]['parent_id']
print d
print '**'*99
par = []
for i in seq[1]['children']:
    name = i['name']
    type = i['object_type']['name']
    types = i['parent']['object_type']['name']
    print name
    print type
    print types
    if types == 'Task':
        parent = i['parent']['name']
        par.append(parent)
        print parent
        print '**' * 99
    elif types == 'Sequence':
        for parent in par:
            parents = parent[0]['name']
            print parents
    else:
        pass

if c != d:
    e = f[0]['children']
    print e[0]['name']
    print e[0]['object_type']['name']



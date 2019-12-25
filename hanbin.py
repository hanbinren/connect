# coding: utf-8
import ftrack_api
session = ftrack_api.Session(
server_url='https://ckyh.ftrackapp.cn',
    api_key='OWM1ODBmMjktMTYxMi00YTVhLWFkMzAtODY3NjQ0NzE1OGI2Ojo1YzQ4YWE0Ny01OWFkLTQ4ODYtYWIzNC0yMWQwNzkwMTY5ZTQ',
    api_user='wangxiaowei@ckyhvfx.com')

# se = session.query('Project where name is riyue_ry')
# print se[0]['id']
#
# se = session.query('AssetBuild where name is asset')
# print se[0]['children']
# print se[0]['id']
# print se[0]['parent_id']
# c = se[0]['children']
# for v in c:
#     print v['name']
#     print v['parent_id']
a = [111,1,1,1,1,6,1,1,1,1]
print len(a)
print a
a = session.query('Project where name is it')
b = a[0]['name']



se = session.query('Folder where name is "任务列表"' )
print se.all()
c = se[0]['children']
for s in c:
    print s['name']
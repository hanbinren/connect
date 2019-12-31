# coding: utf-8
from ftrack_api import entity
# import ftrack_api.entity.base
import ftrack_api.entity.factory
import ftrack_api.entity.base
import ftrack_api.cache
import ftrack_api.accessor.disk
import ftrack_api.structure.origin

import os
import arrow
import ftrack_api
session=ftrack_api.Session(
    server_url='https://ckyh.ftrackapp.cn',
    api_key='MGVmZTdlODMtNzVkZC00MDBmLTllMGItNTFiZjgzZTRjZWI5Ojo0YzdkMTc5My05YzVlLTRkOTEtODZhNC05ZTgzMzdkNTM0OGE',
    api_user='hanbin'
)

# project_dict = {}
# seq={}
# c = []
# projects_1 = session.query('Project where name is dayingjia_dyj')
# print projects_1
# hierarchy = projects_1[0]['children']
# print hierarchy
# for a in hierarchy:
#     print a['name']
#     s = a['name']
#     type_p = hierarchy[0]
#     types = type_p['object_type']
#     se = str(types['name'])
#     print se
#     project_dict[a['name']] = se
#     print project_dict
# print project_dict
# for key,value in project_dict.items():
#     print key,value
#
# for k,v in project_dict.items():
#     print k,v
#     seq1 = session.query(v+' where name is '+k)
#     t = seq1[0]['children']
#     for i,v in enumerate(t):
#         print v['name']
#         type_p = t[i]
#         types = type_p['object_type']
#         se = str(types['name'])
#         print se
#         seq[v['name']] = se
#         print seq
# print seq
#寻找ren_ren/bvt/fix_connect
# task_id = session.query('Task where name is fix_connect')
# print task_id.all()
# task = task_id[0]['id']
# print task
#获取任务的ID
task = session.get('Task','f6e644e0-f6d4-11e9-a07d-0a58ac1e0254')
#任务的父级用与以下发布资产
task_parent = task['parent']
print task_parent
#创建资产和该资产的版本
task_type = session.query('AssetType where name is "Geometry"').one()
print task_type
#创建一个资产
asset = session.create('Asset',{
    'name':'my asset',
    'type':task_type,
    'parent':task_parent
})
print asset
#创建一个版本
asset_version = session.create('AssetVersion',{
    'asset':asset,
    'task':task
})
print asset_version
print asset_version['id']
s = asset_version.items()
print s
for a in s:
    print a[0]













#找到服务器路径
loc = session.query('Location where name is "rd2.y"')
print loc

for l in loc:
    print l['name']
print loc[0].keys()

y = loc[0]
print y

s = y.accessor = ftrack_api.accessor.disk.DiskAccessor(
    prefix=r'\\rd2\render'
)
print s
a = y.structure = ftrack_api.structure.origin.OriginStructure(
    prefix=r''
)
print a
#拿到要传入文件的路径
path = r'y:\rndtest_rndt\seq1\0010\animation\v001rndt_seq1_0010_v021_wxw.exr'
#任务不用做资产的父挤，把任务和assetversion直接连接
#当我们有一个可以创建组建得的版本
#这将自动创建一个新组件并将其添加到已配置为第一个优先级的位置
asset_version.create_component(
    path,
    data={
        'name':'render'
    },
    location=y
)

asset_version['custom_attributes']['majorversion'] = 2
asset_version['custom_attributes']['minorversion'] = 1
for i in asset['versions']['custom_attributes']:
    print i



session.commit()
session.close()






# print session.types.keys()
# print session.query('CustomAttributeConfiguration').all()
# projects = session.query('Project')
# print projects
# for project in projects:
#     print project['name']
#     st = str(project['name'])
# # print 111111
# projects_1 = session.query('Project where name is Project')
# print projects_1
# print projects_1[0]['children']

# for a in projects_1[0]['children']:
#     print a['name']

# stands = []
# projects = session.query('Project')
# print projects
# for project in projects:
#         print project['name']
#         st = str(project['name'])
#         stands.append(st)
# for i,v in enumerate(stands):
#     print i,v
#     projects_1 = session.query('Project where name is' + stands[i] )
#     print projects_1[0]['children']
#     project_s = []
#     for a in projects_1[0]['children']:
#         print a['name']
#         project_s.append(a['name'])
#     print project_s
#     for s,x in enumerate(project_s):
#         print s+1,x

# project_schema = session.query('ProjectSchema where name is VFX').one()
# print project_schema
# s =  project_schema.get_types('Task')[0]['name']
# print s
#
# for tp in project_schema['object_types']:
#     print tp['name']
# for project in projects:
#     print project['metadata'].keys()
#     print project['metadata'].items()
#
# if t[0] == 'Asset':
#     pass
#
# projects =session.query(t[0])
# print projects
# for p in projects:
#     print p['Asset']
# projects = session.query('Project')
# print projects
# print projects[2].keys()
# print 11111
# for i in projects[2].keys():
#     print i
# print 11111
# projectss = session.query('Asset')
# print projectss
# print projectss[2].keys()
# print 11111
# for v in projectss[2].keys():
#     print v
# print 11111




# for project in projects:
#     print project['name']
#
#
#
#
# project=session.query('Project').first()
# print 11111
# print project['name']
# print type(project['name'])
# print 11111
# print project['children']
# print type(project['children'])
# loc = session.query('Location where name is "rd2.y"')
# for l in loc:
#     print l['name']
# print l.keys()
#
# print loc[0].keys()
# y = loc[0]
# print 11111
# print y.items()
# print ftrack_api.mixin(y,ftrack_api.entity.location.UnmanagedLocationMixin)
# y.accessor = ftrack_api.accessor.disk.DiskAccessor(
#     prefix=r'\\rd2\render'
# )
# print type(y.accessor)
#
# asset = session.query('Asset where name is dsr_jr_0010_comp').one()
# print asset.items()
#
# task = session.query('Task where name is comp').first()
# print task.items()
#
# print y.accessor.list(r'shengyin_sy\_library')
# y.structure = ftrack_api.structure.origin.OriginStructure(
#     prefix=r''
# )
# print type(y.structure)
# c = os.path.dirname(project['name'][0])
# print c
# print 222222
#
# active_projects = session.query('Project where status is active')
# active_project_ending_before_next_week=session.query(
#     'Project where status is active and end_data before"{0}"'.format(
#         arrow.now().replace()
#     )
# )
# print active_project_ending_before_next_week
#
# child = project['children'][0]
# print child['parent'] is project
#
# results = session.query(
#     'Context where parent.name like "te%"'
# )
# print results
#
# new_sequence = session.create('Sequence',{'name':'Starlord Reveal'})
# print new_sequence
#
# new_sequence['description']='First hero character reveal.'
# print new_sequence
#
# new_sequence['parent']=project
# print new_sequence
# print project['children'].append(new_sequence)
#
# # session.commit()
#
# user = session.query('User').first()
# with session.auto_populating(False):
#     print user['email']
# print user
# print session.types.keys()
# print isinstance(projects,session.types['Project'])
# note =session.query('Note').first()
# print note.keys()
# print note['content']
# note['content'] = 'A different message!'
# reply = note.create_reply('con','wangxiaowei@ckyhvfx.com')
#
# task = session.query('Task').first()
# print task.keys()
# # for k,v in task.items():
# # #     print k
# for attribute in type(task).attributes:
#     print attribute
# print task('id')
# class Factory(ftrack_api.entity.factory.StandardFactory):
#     def create(self,schema,bases=None):
#         cls = super(Factory,self).create(schema,bases=bases)
#         if schema['id']=='User':
#             cls.get_full_name = 'wangxiaowei@ckyhvfx.com'
#             # cls.get_full_name = get_full_name
#         return cls

# session = ftrack_api.Session()
# user = session.query('User').first()
# print user.get_full_name()
# def callback_a(event):
#     return 'A'
# def callback_b(event):
#     return 'B'
# session = ftrack_api.Session(
#     server_url='https://ckyh.ftrackapp.cn',
#     api_key='OWM1ODBmMjktMTYxMi00YTVhLWFkMzAtODY3NjQ0NzE1OGI2Ojo1YzQ4YWE0Ny01OWFkLTQ4ODYtYWIzNC0yMWQwNzkwMTY5ZTQ',
#     api_user='wangxiaowei@ckyhvfx.com'
# )
# session.event_hub.subscribe(
#   'topic=test-synchronous',callback_a,priority=10
# )
# session.event_hub.subscribe(
#     'tooic=test-synchronous',callback_b,priority=20
# )
# results = session.event_hub.publish(
#     ftrack_api.entity.base.Entity(topic='test-synchtonous'),synchronous=True
# )
# import ftrack_api
# import ftrack_api.event.base
#
# def callback_a(event):
#    return 'A'
#
# def callback_b(event):
#    return 'B'
#
# session = ftrack_api.Session()
# session.event_hub.subscribe(
#     'topic=test-synchronous', callback_a, priority=10
# )
# session.event_hub.subscribe(
#   'topic=test-synchronous', callback_b, priority=20
# )
# results = session.event_hub.publish(
#     ftrack_api.event.base.Event(topic='test-synchronous'),
#     synchronous=True
#  )
# print results



































































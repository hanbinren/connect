# coding: utf-8
#import qdarkstyle
import ftrack_api.structure.id
import ftrack_api.structure.origin
import ftrack_api.entity.location
import ftrack_api.accessor.disk
import ftrack_api
import tempfile

import arrow
session = ftrack_api.Session(
server_url='https://ckyh.ftrackapp.cn',
    api_key='OWM1ODBmMjktMTYxMi00YTVhLWFkMzAtODY3NjQ0NzE1OGI2Ojo1YzQ4YWE0Ny01OWFkLTQ4ODYtYWIzNC0yMWQwNzkwMTY5ZTQ',
    api_user='wangxiaowei@ckyhvfx.com')


# import ftrack_api
# import ftrack_api.entity.location
#
#
# #创建一个位置
# location = session.create('Location',dict(name = 'my.location'))
# # session.commit()
#
# location_by_id = session.get('Location','unique-id')
# print location_by_id
# location_by_name = session.query('Location where name is "my.location"').one()
# print location_by_name
# all_locations = session.query('Location').all()
# for existing_location in all_locations:
#     print existing_location['name']
#
# #为磁盘访问器配置temporary存储
# location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix=tempfile.mkdtemp())
# location.structure = ftrack_api.structure.id.IdStructure()
# location.priority = 30


#创建组件时自动选择位置
# (_, component_path) = tempfile.mkstemp(suffix='.txt')
# component_a = session.create_component(path=component_path)
#
# (_, component_path) = tempfile.mkstemp(suffix='.txt')
# component_b = session.create_component(
#     path=component_path, location=location
# )
#
# (_, component_path) = tempfile.mkstemp(suffix='.txt')
# component_c = session.create_component(path=component_path, location=None)
#
# origin_location = session.query(
#     'Location where name is "ftrack.origin"'
# ).one()
# location.add_component(component_c, origin_location)
# location.remove_component(component_b)
# #关闭数据管理
# ftrack_api.mixin(location, ftrack_api.entity.location.UnmanagedLocationMixin)

shot = session.query('Shot where project.name is "rndtest_rndt"'
                     'and parent.name is "seq1"and name is "0010"').one()
print shot
task=shot['children'][0]
print task
#创建资产
asset_type = session.query('AssetType where short is "Upload"').first()
print asset_type
asset = session.create('Asset',{
    'parent':shot,
    'name':'forest',
    'type':asset_type
})
#为资产里创建一个新的版本
status = session.query('Status where name is "In progress"').one()
print status
version = session.create('AssetVersion',{
    'Asset':asset,
    'status':status,
    'comment':'Added more leaves.',
    'task':task

})
print version['version']
#持续保存的时候再创建版本号
a ='Version number before commit: {0}'.format(version['version'])
print a

#session.commit()
print 'Version number after commit: {0}'.format(version['version'])
#改变路径的前缀
loc = session.query('Location where name is "rd2.y"')
print loc[0]
y = loc[0]

ftrack_api.mixin(y, ftrack_api.entity.location.UnmanagedLocationMixin)

y.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix=r'\\rd2\render')

y.structure = ftrack_api.structure.origin.OriginStructure(prefix=r'')

#添加一些组件
component_path = r'y:\rndtest_rndt\seq1\0010\animation\v001\rndt_seq1_0010_v021_wxw.exr'

version.create_component(component_path,location=y)

model_path = r'y:\rndtest_rndt\seq1\0010\comp\v008\mov\rndt_seq1_0010_comp_v008_ytj.mov'
compenent_model = version.create_component(model_path,{
    'name':'model'
},location=y)

version['is_published']=True

session.commit()
# 将缩略图添加到版本.
# thumbnail = version.create_thumbnail(
#     '/path/to/forest_thumbnail.jpg'
# )
#
# # 在其他对象上设置缩略图而不复制它.
# task['thumbnail'] = thumbnail
# session.commit()



# for i in sorted(session.types.keys()):
#     print i
#查询所有位置
# location_all = session.query('Location').all()
# print location_all
# for location in location_all:
#     print location['name']
# # projects = session.query('Project')
# # for b in projects:
# #     if b['id'] == b['link'][0]['id']:
# #         name = b['name']
#
# id  = session.query('Location where name is "rd2.y"')
# print id.all()
# locations = id[0]['location_components']
# for location in locations:
#     print location
# print id[0].keys()




# print projects
# for i in projects:
#     print i
# peo_id = session.query('Project where id is dayingjia_dyj')
# print peo_id
# for a in peo_id:
#     print a['id']
#
# a = []
# b= []
# projects_2 = session.query('Project where name is dayingjia_dyj')
# print projects_2[0]['children']
# print projects_2[0].items()
# print '*'*99
# # for s in projects_2[0].items():
# #     print s
# #     a.append(s)
#
# seq = session.query('Shot where name is 0060')
# print seq[0].items()
# print seq[0]['name']
# for v in seq[0].items():
#     print v
#     b.append(v)
# print '*'*99
#
# seqs1 = projects_2[0]['children']
# print seqs1
# print seqs1[0]['name']
#
# print seqs1[0]['object_type']['name']
# print seqs1[0]['parent']['name']
# print seqs1[0]['parent_id']
# print projects_2[0]['id']
# t = seqs1[0]['children']
# print t[0]['children']
#
# for a in t:
#     print a['name']
# seqs = projects_2[0]['children']
# print seqs
#
# print seqs1['name']
# #print seqs1['object_type']['name']
#
# #







































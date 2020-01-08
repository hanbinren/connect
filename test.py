# coding: utf-8
#import qdarkstyle
import ftrack_api.structure.id
import ftrack_api.structure.origin
import ftrack_api.entity.location
import ftrack_api.accessor.disk
import ftrack_api
import tempfile

import arrow
session=ftrack_api.Session(
    server_url='https://ckyh.ftrackapp.cn',
    api_key='MGVmZTdlODMtNzVkZC00MDBmLTllMGItNTFiZjgzZTRjZWI5Ojo0YzdkMTc5My05YzVlLTRkOTEtODZhNC05ZTgzMzdkNTM0OGE',
    api_user='hanbin'
)





folder_all_list = []
    for node_id in node_id_list:
        node = LocalFolderModule().get_node_data(node_id, graph)
        if node['label'] == 'folder':
            node_id_list = LocalFolderModule().get_all_folder_from_folder(node_id, graph)
            if node_id_list:
                node_list = json_folders(node_id_list, graph)
                node_list.sort(key=lambda p_folder: p_folder['name'])
                node['children'] = node_list
            folder_all_list.append(node)
        elif node['label'] == 'transaction':
            case_id_list = LocalFolderModule().get_all_folder_from_folder(node_id, graph)
            if case_id_list:
                case_list = []
                for case_id in case_id_list:
                    case_node = LocalFolderModule().get_node_data(case_id, graph)
                    case_list.append(case_node)
                case_list.sort(key=lambda p_folder: p_folder['case_name'])
                node['children'] = case_list
            folder_all_list.append(node)
    return folder_all_list
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
print shot['name']
task=shot['children'][0]
print task['name']
#创建资产
asset_type = session.query('AssetType where name is "Upload"').first()
print asset_type['name']
asset = session.create('Asset',{
    'parent':shot,
    'name':'forest',
    'type':asset_type
})
print asset['parent']['name']
asset_name = session.query('Asset where name is "forest"')
print asset_name
for asset_n in asset_name:
    print asset_n['name']

task_name = session.query('Task where name is "comp"').first()

#为资产里创建一个新的版本
status = session.query('Status where name is "In progress"').one()
print status['name']
version = session.create('AssetVersion',{
    'Asset':asset,
    'status':status,
    'comment':'Added more leaves.',
    'task':task

})
print version['version']
print version['id']


# #持续保存的时候再创建版本号
# a ='Version number before commit: {0}'.format(version['version'])
# print a
#
# #session.commit()
# print 'Version number after commit: {0}'.format(version['version'])
#找到服务器路径
loc = session.query('Location where name is "my.location"')
#print loc[0]
y = loc[0]
#取消数据的自动管理
#ftrack_api.mixin(y, ftrack_api.entity.location.UnmanagedLocationMixin)
#本地文件的系统访问,设置临时空间
y.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix=r'\\dr2\render')
#生成资源标识符
y.structure = ftrack_api.structure.origin.OriginStructure(prefix=r'')
#
# #添加一些组件
component_path = r'y:\rndtest_rndt\seq1\0010\animation\v001\rndt_seq1_0010_v021_wxw.exr'
# print component_path
#
# #print version.create_component(component_path,location=y)
#
# model_path = r'y:\rndtest_rndt\seq1\0010\comp\v008\mov\rndt_seq1_0010_comp_v008_ytj.mov'
compenent_model = version.create_component(component_path,data={
    'name':'model'},
 location=y)

#
# #必须附加到已提交版本和具有父上下文的已提交资产
# version['is_published']=True
#
session.commit()
# session.close()
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







































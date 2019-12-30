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
#查询所有位置
location_all = session.query('Location').all()
print location_all
for location in location_all:
    print location['name']
# projects = session.query('Project')
# for b in projects:
#     if b['id'] == b['link'][0]['id']:
#         name = b['name']

id  = session.query('Location where name is "rd2.y"')
print id.all()
locations = id[0]['location_components']
for location in locations:
    print location
print id[0].keys()

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
print projects_2[0].items()
print '*'*99
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







































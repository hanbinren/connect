# coding: utf-8
from itertools import groupby
import ftrack_api
import clique
import os
import lucidity

# session = ftrack_api.Session(
#     server_url='https://ckyh.ftrackapp.cn',
#     api_key='MGVmZTdlODMtNzVkZC00MDBmLTllMGItNTFiZjgzZTRjZWI5Ojo0YzdkMTc5My05YzVlLTRkOTEtODZhNC05ZTgzMzdkNTM0OGE',
#     api_user='hanbin'
# )
# a =[]
# def workfile(file):
#     for root, dirs, files in os.walk(file):
#         for f in files:
#             a.append(f)
# def main():
#     workfile(r"Y:\rndtest_rndt\seq1\0010\comp\v008\fullres")
# if __name__ == '__main__':
#     main()
# print a
# collections,remainder = clique.assemble(a)
# for collection in collections:
#     print repr(collection)
#     print collection
# head = 'rndt_seq1_0010_comp_v007_ytj.'
# tail = '.exr'
# padding = 4
#
# collection = clique.Collection(head=head,tail=tail,padding=padding)
# print collection.indexes
# print collection.match('rndt_seq1_0010_comp_v007_ytj.1001.exr')
# print collection.format('{head}[index]{tail}')
#
# path = r'\jobs\monty\assets\circus\model\high\circus_high_v001.abc'
# #path = '/jobs/monty/assets/circus/model/high/circus_high_v001.abc'
# template = lucidity.Template('model', r'\jobs\{job}\assets\{asset_name}\model\{lod}\{asset_name}_{lod}_v{version}.{filetype}')
# #template = lucidity.Template('model', r'/jobs/{job}/assets/{asset_name}/model/{lod}/{asset_name}_{lod}_v{version}.{filetype}')
# print template.keys()
#
# data = template.parse(path)
# print data
# print data['asset_name']
# path = template.format(data)
# print path
# templates = lucidity.discover_templates(paths=['/templates'],recursive=False)
#
#
# template = lucidity.Template('job',r'\jobs\{job_code}')
# print template.parse(r'\jobs\monty')
# print template.format({'job_code': 'monty'})
#
# template = lucidity.Template('name','partten',default_placeholder_expression='[^\]+')
# templatea = lucidity.Template('name', 'file_v{version:\d+}.ext')
# print templatea.format({'version': '001'})


session = ftrack_api.Session(
server_url='https://ckyh.ftrackapp.cn',
    api_key='OWM1ODBmMjktMTYxMi00YTVhLWFkMzAtODY3NjQ0NzE1OGI2Ojo1YzQ4YWE0Ny01OWFkLTQ4ODYtYWIzNC0yMWQwNzkwMTY5ZTQ',
    api_user='wangxiaowei@ckyhvfx.com')
# project_id = []
# pr = session.query('Project where name is dayingjia_dyj')
# print pr[0]['name']
# print pr[0]['id']
# c = pr[0]['children']
# for pr_name in c:
#     pr_id = pr_name['id']
#     project_id.append(pr_id)
#
# print project_id
# for sequence_id in project_id:
#     print sequence_id
#
#     #se = session.query('Sequence where name is {0}'.format(sequence_id))
#     #ses = session.query('Sequence where id is {0}'.format(sequence_id))
# ses = session.query('Sequence where name is asset')
#
# print ses[0]['name']
# sh = ses[0]['children'][0]['name']
# print sh
# id = ses[0]['children'][0]['id']
# parent_id = ses[0]['parent_id']
# print parent_id
# if parent_id == pr[0]['id']:
#     name = ses[0]['children'][0]['name']
#     print name
# else:
#     seb = session.query('Sequence where id is 5cabe900-2615-11ea-990e-0a58ac1e037c')
#     name = seb[0]['name']
#     children_name = seb[0]['children'][0]['name']
#     print name
#     print children_name
#
#
#
#
#     print '*'*99
#     ta = session.query('Shot where name is {0}'.format(children_name))
#
#     print ta[0]['children'][0]['name']
#     print ta[0]['children'][0]['id']
#     print ta[0]['children'][0]['parent_id']

# object_all_list = []
# se = session.query('Sequence where name is sc030')
# print se
# print se.all()
# print se[0]['children']
# print se[0]['children'][0]['name']
# for children_se in se[0]['children']:
#     print children_se


# cli_list = ['rndt_seq1_0010_comp_v006_ytj.1005.exr','rndt_seq1_0010_comp_v006_ytj.1006.exr'
#     ,'rndt_seq1_0010_comp_v006_ytj.1007.exr','rndt_seq1_0010_comp_v006_ytj.1008.exr'
#     ,'rndt_seq1_0010_comp_v006_ytj.1009.exr','rndt_seq1_0010_comp_v006_ytj.1010.exr'
#     ,'rndt_seq1_0010_comp_v006_ytj.1011.exr']
# collections,remainder = clique.assemble(cli_list)
# for collection in collections:
#     print repr(collection)
#     print collection


print '*'*99
# cli_list = ['file.0001.jpg', '_cache.txt', 'file.0002.jpg',
#          'foo.1.txt', 'file.0002.dpx', 'file.0001.dpx',
#           'file.0010.dpx', 'scene_v1.ma', 'scene_v2.ma']
# collections,remainder = clique.assemble(cli_list,minimum_items=1)
# for collection in collections:
#     print repr(collection)
# print '*'*99
# collection = collections[0]
# print collection.head
# print collection.tail
# print collection.padding
# print collection.indexes

file_list = []
int_list = []
head_list = []
tail_list = []
path = r'Y:\rndtest_rndt\seq1\0010\comp\v007\mov'
dir = os.listdir(path)
print dir
if len(dir) == 1:
    print dir[0]
else:
    for file in dir:
        print file
        int_name = file.split('.')[1]
        file_list.append(file)

        head = file.split('.')[0]
        head_list.append(head)

        tail = file.split('.')[2]
        tail_list.append(tail)
        name_int = int(int_name)
        int_list.append(name_int)



    fun = lambda x: x[1] - x[0]
    for k, g in groupby(enumerate(int_list), fun):
        l1 = [j for i, j in g]
        if len(l1) > 1:
            scop = str(min(l1)) + '-' + str(max(l1))
            print scop
        else:
            scop = l1[0]
            print scop
        print("连续数字范围：{}".format(scop))

    collections,remainder = clique.assemble(file_list)
    for collection in collections:
        print repr(collection)

    head = head_list[1]
    heada = '{0}.'.format(head)
    tail = tail_list[1]
    taila = '.{0}'.format(tail)

    collection = clique.Collection(head=heada,tail=taila,padding=4)
    for name in file_list:
        collection.add(name)
    print collection.is_contiguous()
    print collection.indexes
    print collection.holes()




#
# collection = clique.parse('/path/to/file.%04d.ext [1, 2, 5-10]')
# print repr(collection)

# collection = clique.parse(
#     '/path/to/file.%04d.ext [1-10] (2, 8)'
#     '{head}{padding}{tail} [{range}] ({holes})'
# )
# print repr(collection)


# collection = clique.Collection(head='file.',tail='.jpg',padding=4)
# #collection.add('file.0001.jpg')
# collection.add('file.0001.jpg')
# collection.add('file.0002.jpg')
# collection.add('file.0003.jpg')
# collection.add('file.0004.jpg')
# print collection.match('file.0002.jpg')
# print list(collection)[-1]
# print collection.indexes
# print collection.indexes.update([3,4,5])
# for item in collection:
#     print repr(item)
# print '*'*99
# collection = clique.Collection('file.', '.jpg', 4, indexes=set([1,2,3,4,5]))
# print collection.format()
# print collection.format('{head}[index]{tail}')
# print collection.is_contiguous()
# collection.indexes.discard(3)
# print collection
# print collection.is_contiguous()
#
#
#
#
# missing = collection.holes()
# print missing
# print missing.indexes
#
# subcollections = collection.separate()
# for subcollection in subcollections:
#     print subcollection
# collection_a = clique.Collection('file.','.jpg',4,set([1,2]))
# collection_b = clique.Collection('file.','.jpg',4,set([4,5]))
# print collection_a.indexes
# collection_a.merge(collection_b)
# print collection_a.indexes









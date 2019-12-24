#!/usr/bin/env python
# coding: utf-8

# In[233]:


import ftrack_api
import os


# In[234]:


session = ftrack_api.Session(
    server_url='https://ckyh.ftrackapp.cn',
    api_key='NzM5YTcxN2ItMmFkYS00ZGYyLWExMGEtZTIwZTYzOTM4Y2JmOjplNTZkNjIxZC0xNDJjLTQyOGQtODhiOC00ZDI2NmQzZWU2ZTA',
    api_user='hanbin'
)


# In[235]:


for i in sorted(session.types.keys()):
    print i


# ###  获取project

# In[236]:


projects = session.query('Project')
for i in projects:
    print i['name']



# In[237]:


project_1 =  session.query('Project').first()


# In[238]:


dsr = projects[3]
for i in dsr['children']:
    print i['name']


# ### 获取location

# In[239]:


loc = session.query('Location where name is "rd2.y"')
for l in loc:
    print l['name']
loc[0].keys()
y = loc[0]


# In[240]:


y.items()


# ### 取消location对数据的自动管理。

# In[241]:


#ftrack_api.mixin(y, ftrack_api.entity.location.UnmanagedLocationMixin)


# ### 设置location
# 
# Accssor的prefix是路径的前缀，比如是`y:`
# 
# ```
# y.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix='y:')
# ```
# 
# 后续用到的路径都是相对`y`的相对路径，路径字符前面不加斜杠。比如下面。
# 
# ```
# y.accessor.list('disanren_dsr\000')
# ```
# 输出结果是：
# ```
# ['disanren_dsr\\000\\000', 'disanren_dsr\\000\\0030']
# ```

# In[242]:


# Assign a disk accessor with *temporary* storage
y.accessor = ftrack_api.accessor.disk.DiskAccessor(
    prefix=r'\\rd2\render'
)

y.structure = ftrack_api.structure.origin.OriginStructure(
    prefix=r''
)


# In[254]:


# y.accessor.list('y:/rndtest_rndt/seq1/0010/comp/v006/fullres/')


# ### 获取Asset

# In[244]:


asset = session.query('Asset where name is dsr_jr_0010_comp').one()


# ### 获取 task###

# In[245]:


asset.items()


# In[246]:


task = session.query('Task where name is comp').first()


# In[247]:


task.items()


# ### 创建version

# In[248]:


asset_version = session.create('AssetVersion', {
    'name': 'dsr_jr_0010_comp v008',
    'asset': asset,
    'task': task
})


# ### 创建component

# In[249]:


pth = r'y:\rndtest_rndt\seq1\0010\comp\v008\mov\rndt_seq1_0010_comp_v007_ytj.mov'
#pth = r'y:\rndtest_rndt\seq1\0010\animation\v001\rndt_seq1_0010_v021_wxw.exr'


# In[250]:


asset_version.create_component(
    pth,
    data = {
        'name':'render'
    },
    location = y
)


# In[251]:


session.commit()


# In[252]:


session.close()


# ### 查询custum attributre

# In[79]:


v = session.query('AssetVersion where custom_attributes any ( key is "versionname" and value is "dsr_hy_0090_fx_smoke_smoke_wl_v004_v004_thh")')
print v
v[0]['custom_attributes']['versionname']


# ### 测试
# 

# In[3]:


session = ftrack_api.Session()

user = session.query(
    'select username from User where username is "{0}"'.format(u'hanbin')
).one()

seq = session.query('Sequence where name is api_test').one()
shot = session.query('Shot where name is api_test_shot').one()
task = session.query('Task where name is api_test_task2').one()
asset = session.query('Asset where name is dsr_hy_0090_fx_smoke_smoke_wl').one()


# In[524]:


loc = session.query('Location where name is "ckyh.wrap.y"')
y = loc[0]

ftrack_api.mixin(y, ftrack_api.entity.location.UnmanagedLocationMixin)

y.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix='y:')

y.structure = ftrack_api.structure.origin.OriginStructure(prefix='')


# In[529]:


y.accessor.list(r'disanren_dsr\000')


# In[ ]:


asset_version = session.create('AssetVersion', {
    'custom_attributes.versionname': 'dsr_hy_0090_fx_smoke_smoke_wl_v004_v004_thh',
    'asset': asset,
    'task': task
})


# In[521]:


pth = r'y:\disanren_dsr\hy\0090\fx\v001\_slap\v002_v002\dsr_hy_0090_fx_smoke_smoke_wl_v002_v002_thh.%04d.exr'

asset_version.create_component(
    pth,
    data = {
        'name':'render3'
    },
    location = y
)


# In[ ]:


asset_version['custom_attributes']['versionname'] = 'dsr_hy_0090_fx_smoke_smoke_wl_v004_v004_thh'


# In[498]:


asset_version['custom_attributes']['majorversion'] = 2
asset_version['custom_attributes']['minorversion'] = 4
# for i in asset['versions']:
#     print i.keys()


# In[484]:


for i in asset['versions'][0]['custom_attributes']:
    print i


# ### 测试通过task创建asset version

# In[30]:


task['appointments'][0].items()


# In[6]:


task.items()


# In[32]:


asset.items()


# In[34]:


asset['versions'][0].items()


# In[78]:


v = session.query('AssetVersion where custom_attributes any ( key is "versionname" and value is "dsr_hy_0090_fx_smoke_smoke_wl_v004_v004_thh")')
v[0]['custom_attributes']['versionname']


# In[85]:


a = session.query('AssetBuild where name is "chabei01"')
a[0]['parent']


# In[88]:


0.1*60


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ftrack_api
import os


# In[4]:


session = ftrack_api.Session(
    server_url='https://ckyh.ftrackapp.cn',
    api_key='NzM5YTcxN2ItMmFkYS00ZGYyLWExMGEtZTIwZTYzOTM4Y2JmOjplNTZkNjIxZC0xNDJjLTQyOGQtODhiOC00ZDI2NmQzZWU2ZTA',
    api_user='hanbin'
)


# In[15]:


for i in sorted(session.types.keys()):
    print i

# ###  获取project

# In[18]:


projects = session.query('Project')
for i in projects:
    print i['name']


# In[25]:


project_1 =  session.query('Project').first()


# In[38]:


dsr = projects[0]
for i in dsr['children']:
    print i['name']


# ### 创建entity

# In[40]:


new_seq = session.create('Sequence', {
    'name':'api_test'
})


# In[41]:


new_seq['description'] = '测试api用'


# In[44]:


# 下面两个方法都可以将sequence添加到制定project内
new_seq['parent'] = dsr

#dsr['children'].append(new_seq)


# In[45]:


session.commit()
session.close()


# ## Session
# 
# 所有跟ftrack server的沟通都通过session实现。好处是一个python
#  precess里可以与多个ftrack server沟通。
#  
# Session可以有通过两个方式定义：
# 
# ```
# >>> session = ftrack_api.Session(
# ...     server_url='http://mycompany.ftrackapp.com',
# ...     api_key='7545384e-a653-11e1-a82c-f22c11dd25eq',
# ...     api_user='martin'
# ... )
# ```
# 
# 还可以通过环境变量定义：
# 1. `FTRACK_SERVER`
# 2. `FTRACK_API_USER`
# 3. `FTRACK_API_KEY`
# 
# 当用环境变量的方式时，不需要提供上面的具体参数:
# ```
# >>> session = ftrack_api.Session()
# ```

# ### Auto-population
# 
# Session有自动cache的功能。当跟服务器query一次后再query并不会与服务器沟通而是直接调用本地的cache。

# #### 定义plugin的环境变量
# 
# Ftrack通过下面的环境变量定义放置plugin的path。
# 
# 
# ```
# FTRACK_EVENT_PLUGIN_PATH
# ```

# ## Entity
# 
# Entity是类似python字典结构的object。Key对应的是相应type的attribute。同时提供一些method用来执行一些常见的操作。
# 
# ```
# note = session.query('Note').first()
# print note.keys()
# print note['content']
# note['content'] = 'A different message!'
# reply = note.create_reply(...)
# ```
# ### Attributes
# 
# 不同的entity有不同给的attribute。
# 
# 通过`keys()`查看所有可能的attribute名字。
# ```
# >>> task = session.query('Task').first()
# >>> print task.keys()
# ```

# ### 用环境变量接入ftrack session

# In[2]:


os.environ['FTRACK_SERVER'] = 'https://liantong.ftrackapp.cn'
os.environ['FTRACK_API_KEY'] = 'fd804d32-88cb-11e3-b92b-f23c91df2148'
os.environ['FTRACK_API_USER'] = 'liantong109@aliyun.com'


# In[433]:


session = ftrack_api.Session()


# In[376]:


project = session.query('Project where name is disanren_dsr').first()
project['name']
# for i in projects:
#     print i['name']


# ### 获取user

# In[400]:


# 获取特定的user

user = session.query(
    'select username from User where username is "{0}"'.format(u'xingyuanyang@ckyhvfx.com')
).one()

user['username']


# In[439]:


seq = session.query('Sequence where name is api_test').one()
shot = session.query('Shot where name is api_test_shot').one()
task = session.query('Task where name is api_test_task2').one()
asset = session.query('Asset where name is dsr_hy_0090_fx_smoke_smoke_wl').one()


# ### 创建sequence

# In[184]:


# 创建sequence

new_seq = session.create("Sequence", {
    'name':'api_test2'
})


# ### 创建shot

# In[190]:


#创建shot

new_shot = session.create('Shot', {
    'name': 'api_test_shot',
    'parent': seq
})


# ###  查询项目设置

# In[319]:


# 查询项目设置

project_schema = session.query('ProjectSchema where name is VFX').one()

# 获取task的type
a = project_schema.get_types('Task')[0]['name']
print a

# In[323]:


for tp in project_schema['object_types']:
    print tp['name']


# ### 获取task的type

# In[237]:


# 获取task的type

task_type = session.query('Type where name is Tracking').one()
task_type['name']


# ### 创建task

# In[260]:


#创建task

new_task2 = session.create('Task',{
    'name': 'api_test_task3',
    'parent': shot,
    'type': task_type,
#      'assignments': user
})


# ### 分配任务

# In[379]:


# 分配任务

session.create('Appointment', {
    'context': task,
    'resource': user,
    'type': 'assignment'
})


# ### 获取user的task列表

# In[382]:


# 获取特定user的task列表

assigned_tasks = session.query(
    'select link from Task \
    where assignments any (resource.username = "{0}")'.format(user['username'])
)

for t in assigned_tasks:
    print u' / '.join(item['name'] for item in t['link'])


# ### 创建location

# In[ ]:


loc = session.create('Location', dict(name='ckyh.test'))


# ### 获取location

# In[453]:


loc = session.query('Location where name is "ckyh.wrap.y"')
for l in loc:
    print l['name']
loc[0].keys()
y = loc[0]


# In[358]:


y.items()


# ### 取消location对数据的自动管理。

# In[448]:


ftrack_api.mixin(y, ftrack_api.entity.location.UnmanagedLocationMixin)


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

# In[454]:


# Assign a disk accessor with *temporary* storage
y.accessor = ftrack_api.accessor.disk.DiskAccessor(
    prefix=''
)

y.structure = ftrack_api.structure.origin.OriginStructure(
    prefix=''
)


# In[450]:


y.accessor.list('y:/disanren_dsr/hy/0090/fx/v001/_slap/v001_v001/')


# ### 创建Asset

# In[ ]:


# 获取task
task = assigned_tasks[0]

# 获取asset的父级
asset_parent = task['parent']

asset_type = session.query('AssetType where name is "FX"').one()
asset = session.create('Asset', {
    'name': 'dsr_hy_0090_fx_smoke_smoke_wl',
    'type': asset_type,
    'parent': asset_parent
})


# ### 创建version

# In[451]:


asset_version = session.create('AssetVersion', {
    'name': 'dsr_hy_0090_fx_smoke_smoke_wl_v003_v003_thh',
    'asset': asset,
    'task': task
})


# ### 创建component

# In[455]:


pth = r'y:\disanren_dsr\hy\0090\fx\v001\_slap\v002_v002\dsr_hy_0090_fx_smoke_smoke_wl_v002_v002_thh.%04d.exr'


# In[456]:


asset_version.create_component(
    pth,
    data = {
        'name':'render3'
    },
    location = y
)


# In[522]:


session.commit()


# In[487]:


session.close()


# ### 查询custum attributre

# In[79]:


v = session.query('AssetVersion where custom_attributes any ( key is "versionname" and value is "dsr_hy_0090_fx_smoke_smoke_wl_v004_v004_thh")')
v[0]['custom_attributes']['versionname']


# ### 测试
# 

# In[3]:


session = ftrack_api.Session()

user = session.query(
    'select username from User where username is "{0}"'.format(u'xingyuanyang@ckyhvfx.com')
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


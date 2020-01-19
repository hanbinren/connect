# coding: utf-8
import lucidity
from lucidity import Template

def register():
    '''注册模板'''
    return [
        Template('job', '/jobs/{job.code}'),
        Template('shot', '/jobs/{job.code}/shots/{scene.code}_{shot.code}')
    ]
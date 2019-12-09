# coding=utf-8

"""
@作者: Angst
@邮箱: jiqialin@163.com
@开发工具: PyCharm
@创建时间: 2019/12/6 10:21
"""
from comet.util.parserIni import getConfigValue


def dataManipulation(summary, section=None,  **kwargs):
    """
        Process test results for reporting transfer
    :param summary: test result
    :param section: key
    :param kwargs: anything
    :return: list
    """
    result = dict()
    if summary and isinstance(summary, dict):
        params = summary.get('stat').get('testcases')

        result['projectId'] = ''
        result['testTime'] = params.get('test')
        result['total'] = params.setdefault('total', 0)
        result['passCount'] = params.setdefault('success', 0)
        result['failCount'] = params.setdefault('fail', 0)
        result['skipCount'] = params.setdefault('skip', 0)

        result['type'] = getConfigValue(section, 'project.type')
        result['department'] = getConfigValue(section, 'department')
        result['projectName'] = getConfigValue(section, 'project.name')
        result['businessLine'] = getConfigValue(section, 'business.line')
        result['verticalGroup'] = getConfigValue(section, 'business.group')

        result['buildId'] = kwargs.get('build_id')
        return result

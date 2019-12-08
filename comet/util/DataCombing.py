# coding=utf-8

"""
@作者: Angst
@邮箱: zhouqing@yunjiglobal.com
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
    result_list = []
    if summary and isinstance(summary, dict):
        result = dict()
        test_cases = summary['stat']['testcases']

        result['total'] = test_cases.setdefault('total', 0)
        result['passCount'] = test_cases.setdefault('success', 0)
        result['failCount'] = test_cases.setdefault('fail', 0)
        result['skipCount'] = test_cases.setdefault('skip', 0)
        result['testTime'] = test_cases.setdefault('test')
        result['department'] = getConfigValue(section, 'department')
        result['type'] = getConfigValue(section, 'type')
        result['verticalGroup'] = getConfigValue(section, 'businessGroup')
        result['businessLine'] = getConfigValue(section, 'businessLine')
        result['projectId'] = ''
        result['buildId'] = kwargs.get('build_id')
        result['projectName'] = getConfigValue(section, 'projectName')
        result_list.append(result)
        return result_list

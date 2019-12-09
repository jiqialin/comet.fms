# coding=utf-8

"""
@作者: Angst
@邮箱: jiqialin@163.com
@开发工具: PyCharm
@创建时间: 2019/12/6 9:36
"""
import os
import requests
from httprunner.api import HttpRunner
from comet.util.parserIni import getConfigValue
from comet.util.DataCombing import dataManipulation


class RunCaseAndUpload(object):

    def __init__(self, **kwargs):
        self.runner = HttpRunner()
        self.summary = self._runTestCase()
        self.section = kwargs.get('section')
        self.build_id = kwargs.get('buildId')

    # noinspection SpellCheckingInspection
    def _runTestCase(self, dot_env_path=None, maping=None):
        """
            Run the test case in the specified directory based on the parameters.
        :param dot_env_path: Empty runs the default environment, otherwise the corresponding environment
        :param maping: ignore
        :return: test case result.
        """
        path = getConfigValue(self.section, 'autoTest.casePath')
        if not path:
            print("test path  nonentity or  not find files 'properties.ini'")
            raise FileNotFoundError

        elif os.getenv("TEST_ENV") == 'txy':
            self.runner.run(path, dot_env_path=dot_env_path, mapping=maping)
            return self.runner.summary

        elif os.getenv("TEST_ENV") == 'docker':
            self.runner.run(path, dot_env_path='doc.env', mapping=maping)
            return self.runner.summary

    def uploadDataToStargazing(self):
        """
            Processing is completed the processing of the results will be uploaded to stargazing platform.
        :return:
        """
        headers = {'Content-Type': 'application/json'}
        url = getConfigValue('stargazing', 'total')
        data = dataManipulation(self.summary, self.section, buildId=self.build_id)
        # noinspection PyBroadException
        try:
            response = requests.post(url, json=data, headers=headers)
            print("upload success: {}".format(response.json() if response.status_code == 200 else "upload failed:",
                                              response.content))
        except Exception as e:
            print(f'Upload Exception:{e}')

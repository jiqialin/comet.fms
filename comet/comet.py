# coding=utf-8

"""
@作者: Angst
@邮箱: jiqialin@163.com
@开发工具: PyCharm
@创建时间: 2019/12/5 14:30
"""
import os, sys
import argparse
from comet.util.runAndUpload import RunCaseAndUpload
from comet.util.weChatNotice import WeChatNotice

HELP = "The httpRunner plug-in is packaged with CI/CD for use with the Darwin platform. Default Txy Cloud"

if len(sys.argv) == 1:
    sys.argv.append('--help')

parser = argparse.ArgumentParser()

parser.add_argument('--env', type=str, default='txy', help=HELP)
parser.add_argument('--buildUrl', default='', help="CI/CD Darwin Platform Jenkins Build Address Information.")
parser.add_argument('--project', type=str, default='', help="Please Read Configuration Files Properties.ini ")
parser.add_argument('--testType', type=int, default=0, help='Default: 0.Normal 1.Monitoring 2. Health')
arguments = parser.parse_args()


def mainRun():
    """
        step1: Execute test cases
        step2: The result data is uploaded to the stargazing platform
        step3: The result data is uploaded to Enterprise WeChat
    :return:
    """
    project = arguments.project
    build_id = arguments.buildUrl.split('/')[-2] if str(arguments.buildUrl).endswith('/') else arguments.buildUrl.split('/')[-1]
    report_url = f'{arguments.buildUrl}/testReport/'
    os.environ['TEST_ENV'] = str(arguments.env)

    runner = RunCaseAndUpload(section=project, buildId=build_id)
    runner.uploadDataToStargazing()

    weChat = WeChatNotice(runner.summary, report_url, arguments)
    weChat.sendMessages()


if __name__ == '__main__':
    mainRun()
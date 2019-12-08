# coding=utf-8

"""
@作者: Angst
@邮箱: zhouqing@yunjiglobal.com
@开发工具: PyCharm
@创建时间: 2019/12/5 14:30
"""
import os, sys
import argparse
from comet.util.runAndUpload import RunCaseAndUpload
from comet.util.weChatNotice import WeChatNotice

HELP = "The httpRunner plug-in is packaged with CI/CD for use with the Darwin platform"

if len(sys.argv) == 1:
    sys.argv.append('--help')

parser = argparse.ArgumentParser()
parser.add_argument('-h', '--help', type=str, default='', help=HELP)
parser.add_argument('-u', '--buildUrl', default='', help="jenkins build address info.")
parser.add_argument('-e', '--env', help=" 1.docker 2.default:txy 3.development environment")
parser.add_argument('-p', '--project', default=0, help="read ~/.comet.fms configuration, please ~/.comet.fms database")
parser.add_argument('-t', '--testType', type=int, default='0', help='default: 0.normal 1.monitoring 2. health')
args = parser.parse_args()


def mainRun():
    """
        step1: Execute test cases
        step2: The result data is uploaded to the stargazing platform
        step3: The result data is uploaded to Enterprise WeChat
    :return:
    """
    project = args.project
    build_id = args.buildUrl.split('/')[-2] if str(args.buildUrl).endswith('/') else args.buildUrl.split('/')[-1]
    report_url = f'{args.buildUrl}/testReport/'
    os.environ['TEST_ENV'] = str(args.env)

    runner = RunCaseAndUpload(section=project, reportUrl=args.buildUrl)
    runner.uploadDataToStargazing(build_id=build_id)

    weChat = WeChatNotice(runner.summary, report_url, args)
    weChat.sendMessages()


if __name__ == '__main__':
    mainRun()
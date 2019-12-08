# coding=utf-8

"""
@作者: Angst
@邮箱: zhouqing@yunjiglobal.com
@开发工具: PyCharm
@创建时间: 2019/12/6 14:45
"""
import demjson
import requests
from comet.util.DataCombing import dataManipulation
import time


class WeChatNotice(object):
    def __init__(self, summary, report_url, *args):
        self.summary = summary
        self.reportUrl = report_url
        self.projectName = args.__getattribute__('project')
        self.failCount = 0
        self.test_type = args.__getattribute__('testType')

    def addMarkdownInfo(self):
        caseInfo = dataManipulation(self.summary, self.projectName)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if self.test_type == 0:

            info = f""" 
            ### {now_time}<font color=\"info\">{caseInfo['projectName']}</font>接口测试发布\n
            ### 执行用例数<font color=\"info\"> {caseInfo['total']}条</font>, 
            请相关同事注意 <font color=\"info\"> {caseInfo['at']}</font>\n \
            "> 成功用例数： <font color=\"comment\">{caseInfo['success']}条</font> \n \
            "> 失败用例数： <font color=\"warning\">{caseInfo['fail']}条</font> \n \
            "> 跳过用例数： <font color=\"comment\">{caseInfo['skip']}条</font> \n \
            ">【报告地址】：[点击查看测试报告]({self.reportUrl})
    
        """

            messages = dict(msgtype='markdown', markdown={'content': info})
            return messages

    def sendMessages(self):

        headers = {'Content-Type': 'application/json'}
        json_data = demjson.encode(self.addMarkdownInfo())
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=40cc189f-96d7-478c-9ed6-a7cb2da6dfbf'

        if not self.addMarkdownInfo():
            print('Data is empty, not send any messages .')
        else:
            print(f"Send WeChat messages: {json_data}")
            try:
                response = requests.post(url, data=json_data, headers=headers)
                assert response.status_code == 200

            except Exception as e:
                print(f'Send Failed: {e}')

            else:
                print('Send Success.')

#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/10/13
@File    : send_email.py
"""
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 第三方授权码（通过代码foxmail或者代码登录邮箱都需要授权码，qq邮箱、163邮箱设置授权码自行百度开启）
_user = '邮箱地址'
_pwd = '密码'

# 获取时间戳
now = time.strftime('%Y-%m-%d_%H_%M_%S')


class sendEmail:

    def send_email(self, email_to, filepath):
        '''
        :param email_to:  收件方
        :param filepath:  发送附件的地址
        :return: 如名字所示MIMEMultipart就是分多个部分
        '''
        msg = MIMEMultipart()
        # 发件人主题
        msg['Subject'] = now + '华华的测试报告'
        # 发件人
        msg['From'] = _user
        # 收件人
        msg['To'] = email_to

        # 正文文本格式
        part = MIMEText('今天多云转晴')
        # msg.attach文字部分
        msg.attach(part)

        # 针对只发送一个附件  filepath更改为需要发送的附件的位置  只能读文件不能读文件夹
        # MIMEApplication多媒体部分
        part = MIMEApplication(open(filepath, 'rb').read())
        part.add_header('Content_Disposition', 'attach,emt', filename=filepath)
        msg.attach(part)
        # 建立smtp邮件服务器，默认端口25
        s = smtplib.SMTP_SSL('smtp.qq.com', timeout=30)
        s.login(_user, _pwd)
        s.sendmail(_user, email_to, msg.as_string())
        s.close()
        # # for循环处理读取多个文件信息  []列表
        # path = ['路径1', '路径2', '路径3']
        # for item in path:
        #     # MIMEApplication多媒体部分
        #     part = MIMEApplication(open(item, 'rb').read())
        #     part.add_header('Content_Disposition', 'attach,emt', filename=filepath)
        #     msg.attach(part)
        #     # 建立smtp邮件服务器，默认端口25
        #     s = smtplib.SMTP_SSL('smtp.qq.com', timeout=30)
        #     s.login(_user, _pwd)
        #     s.sendmail(_user, email_to, msg.as_string())
        #     s.close()


if __name__ == '__main__':
    sendEmail().send_email("790729742@qq.com", r"D:\doc\工作记录.xlsx")

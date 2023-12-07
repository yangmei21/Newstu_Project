# 代码练习：自动发送邮件（html格式，有正文，有链接，有附件）

import smtplib                               # 引用控值邮箱发送邮件的库
from email.mime.text import MIMEText
# 引入mail.mime的MIMEText 类来实现支持HTML格式的邮件（email.mime是smtplib模块邮件内容主体的扩展）
from email.mime.multipart import MIMEMultipart

# 引进MIMEMultipart可以同时添加正文和附件
# 设置基础内容

user = '2168517841@qq.com'  # 定义发件人邮箱
pwd = 'abdabccfmblreajg'  # QQ邮箱POP3/SMTP的授权码
to = '1154372391@qq.com'  # 收件人邮件
msg = MIMEMultipart()  # 创建一个可以同时添加正文和附件的msg
# 设置HTML格式的邮件正文
# 三个单引号表示包围注释内容，用来包含HTML代码
mail_msg = '''
<p>是一个测试报告邮件，请查收！附件内(*^▽^*)
<p><a href="https://www.baidu.com">这里是链接</a>
'''
# 如果仅添加正文可以用此公式：msg=MIMEText(mail_msg,'html','utf-8')#表示添加正文内容
msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))  # 添加正文
# 添加附件
att1 = MIMEText(open('D:\\pycharm_project\\Newstu_Project\\Run_example_file\\yx_login01.html', 'rb').read(), 'base64', 'utf-8')
# 添加附件，由于定义了中文编码，所以文件可以带中文
att1["Content-Type"] = 'application/octet-stream'  # 数据传输类型的定义
att1["Content-Disposition"] = 'attachment;filename="yx_login.html"'  # 定义文件在邮件中显示的文件名和后缀名，名字不可为中文
msg.attach(att1)  # 将附件添加到邮件内容当中
# 配置调用邮件信息
msg['Subject'] = '测试邮件（yx测试报告）'  # 设置邮件主题
msg['From'] = user  # 设置发件人
msg['To'] = to  # 设置收件人
# 执行命令
s = smtplib.SMTP_SSL('smtp.qq.com',
                     465)  # 选择QQ邮箱服务，默认端口465（smtplib.SMTP()：构造函数，功能是与smtp服务器建立连接，连接成功后，就可以向服务器发送相关请求，比如登录，校验，发送，退出）
s.login(user, pwd)  # 登录QQ邮箱
s.send_message(msg)  # 发送邮件
s.quit()  # 退出QQ邮箱服务
print('Success')

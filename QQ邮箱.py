import tkinter.filedialog
from tkinter import colorchooser
from tkinter import*
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication

def send():
    _user=entry_user.get()
    _pwd=entry_pwd.get()
    _to=entry_to.get().split(';')
    #如名字所示Multipart就是分多个部分 # 构造一个MIMEMultipart对象代表邮件本身 
    msg = MIMEMultipart() 
    msg["Subject"] = entry_theme.get()
    msg["From"]  = _user 
    msg["To"]   = ';'.join(_to) 
       
    #---这是文字部分--- 
    part = MIMEText(entry_msg.get())
    msg.attach(part)

    s = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25 
    s.login(_user, _pwd)#登陆服务器 
    s.sendmail(_user, _to, msg.as_string())#发送邮件 
    s.close()
    print('发送成功')

def send_others():
    filename=filedialog.askopenfilename()
    print(filename)
    _user=entry_user.get()
    _pwd=entry_pwd.get()
    _to=entry_to.get().split(';')
    #如名字所示Multipart就是分多个部分 # 构造一个MIMEMultipart对象代表邮件本身 
    msg = MIMEMultipart() 
    msg["Subject"] = entry_theme.get()
    msg["From"]  = _user 
    msg["To"]   = ';'.join(_to)
    if filename:
        #---这是文字部分--- 
        parts = MIMEText(entry_msg.get())
        msg.attach(parts)
        part = MIMEApplication(open(filename,'rb').read()) 
        part.add_header('Content-Disposition', 'attachment', filename=filename) 
        msg.attach(part)
        s = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25 
        s.login(_user, _pwd)#登陆服务器 
        s.sendmail(_user, _to, msg.as_string())#发送邮件 
        s.close()
        print('发送成功')

def color1():
    fileName = colorchooser.askcolor()
    if fileName[1]:
        frame['background']=fileName[1]

tk=Tk()
tk.title('邮件发送端')
tk.geometry('360x400+200+20')
frame=Frame(tk,bg='silver')
frame.pack(side=LEFT,fill=BOTH,expand=True,padx=10,pady=10)
label_user=Label(frame,text='邮箱账号',fg='black')
label_user.grid(row=0,column=0,columnspan=2,sticky=E,padx=10,pady=10)
entry_user=Entry(frame,width=30)
entry_user.grid(row=0,column=2,padx=10,pady=10)
entry_user.insert(0,'1084578612@qq.com')
label_pwd=Label(frame,text='邮箱授权码',fg='black')
label_pwd.grid(row=1,column=0,columnspan=2,sticky=E,padx=10,pady=10)
entry_pwd=Entry(frame,width=30)
entry_pwd.grid(row=1,column=2,padx=10,pady=10)
label_to=Label(frame,text='目标邮箱',fg='black')
label_to.grid(row=2,column=0,columnspan=2,sticky=E,padx=10,pady=10)
entry_to=Entry(frame,width=30)
entry_to.grid(row=2,column=2,padx=10,pady=10)

label_theme=Label(frame,text='消息主题',fg='black')
label_theme.grid(row=3,column=0,columnspan=2,sticky=E,padx=10,pady=10)
entry_theme=Entry(frame,width=30)
entry_theme.grid(row=3,column=2,padx=10,pady=10)

label_msg=Label(frame,text='消息内容',fg='black')
label_msg.grid(row=4,column=0,columnspan=2,sticky=E,padx=10,pady=10)
entry_msg=Entry(frame,width=30)
entry_msg.grid(row=4,column=2,padx=10,pady=10)

button=Button(frame,text='发送',bg='white',command=send)
button.grid(row=5,column=2,sticky=E,padx=10,pady=10)
#-----------------菜单
menubar=Menu(tk)
menubar.add_command(label='发送文件',command=send_others)
#级联菜单
filemenu=Menu(menubar,tearoff=False)
filemenu.add_command(label='frame',command=color1)
menubar.add_cascade(label='背景色',menu=filemenu)
#.......
tk.config(menu=menubar)#把menubar放进tk中
mainloop()

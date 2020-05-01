from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
import win32com.client as wincl
speak=wincl.Dispatch("SAPI.SpVoice")

bot=ChatBot('BispBot')
conv=open('chat1.txt','r').readlines()
trainer=ListTrainer(bot)
trainer.train(conv)
name=input("Enter Your Name:--  ")

phone=input("Enter Your Phone:--   ")
useremail=input("Enter Your Email Id:--  ")
print('Hello '+ name  + '\n Welcome to Scholars Trainings . \n This is Charles. \n How may I assist you today?')
speak.Speak('Welcome to Scholars Trainings'+name)
speak.Speak('entered mobile number is'+phone)
speak.Speak('and your mail id is'+useremail)
while True:
       request=input(name+':')
       if request=='Bye' or request =='bye':
              print('Charles: Bye')
              speak.Speak('bye bye')
              break
       else:
              response=bot.get_response(request)
              print('Charles:',response)
              speak.Speak(response)
try:
       fromaddr = "scholartraining.2u@gmail.com"
       toaddr = useremail
       msg = MIMEMultipart()
       msg['From'] = fromaddr
       msg['To'] = toaddr
       msg['Subject'] = "Thanks for Connecting"
       body = "Hi , "+name+" \n Thanks for showing Interest in Scholar training Program.We are the leading tutors in city.\n We provide all the expertise training in all the blooming computer Languages  \n.c \n .c++ \n .java \n .PHP \n .pearl \n .R programing \n\n we have all the facilities as such as take away materials such as: \n journals \n reference books \n lab guide \n case studies \n\n we have two types of working systems you can do the training at our institute itself or u can attend the live sessions.the time of the course is 32 hours.\n\n The cost of the course starts at 9000 only \n\n\n\n\n According to your request of said course it will cost about 13000|190 USD \n\n\n for further assistance you may call us at 18001809999 or visit our offices nearest to you. \n\n\n\n\n Our presence : \n Nerul \n Badlapur \n Thane \n Vashi \n Panvel \ns\n\nPlease visit our blog and subscribe for new update and releases"  
       msg.attach(MIMEText(body, 'plain'))
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.ehlo() 
       server.starttls()
       server.login(fromaddr,"eshub72@")
       text = msg.as_string()
       server.sendmail(fromaddr, toaddr, text)
       server.quit()
       print("Thank you for connecting us  \n check your mail for more details")
except Exception:
       print("Error in email id")



       

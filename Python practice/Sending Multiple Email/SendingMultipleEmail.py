import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("Moosali2367@gmail.com","robertdowny")
subject = "test python"
body = "I love Python"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ["musali2367@gmail.com"]
ob.sendmail("Moosali2367@gmail.com",listadd,message)
print("send mail")
ob.quit()

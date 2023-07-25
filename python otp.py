import random
import smtplib

def send_otp(email):
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    email_address = 'yourmailid@gmail.com'             
    email_password = 'yourpassword'                     
    server.login(email_address, email_password)
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)]) 
    message = f'Your OTP is {otp}'
    server.sendmail(email_address, email, message)
    server.quit()

    return otp
def verify_otp():
    email = input("Enter your email address: ")

    otp = send_otp(email)

    user_input = input("Enter the OTP sent to your email: ")
    if user_input == otp:
        print("OTP verified successfully!")
    else:
        print("Invalid OTP, please try again.")

verify_otp()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os, uuid, random

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_sender = 'no-reply@getmyclaims.com'
email_password = 'tzul utwx lyyn bmtu'

# username = 'dheeraj'
# user_email = 'dheerajroy8855@gmail.com'
# password = 'qwerty@123'

# sp_char = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '?' ]
# passwd = str(uuid.uuid4()).replace('-','')[:7]
# passwd = list(passwd + random.choice(sp_char))
# random.shuffle(passwd)
# password = ''.join(passwd)
# user_id=12345
# url = 'example.com'
# flight_id = 72271
# user_id = 12345


def partner_client_email(client_name, client_email, partner_name, flight_details, confirm_url):
    # Create the message
    msg = MIMEMultipart('alternative')
    msg['From'] = email_sender
    msg['To'] = client_email
    msg['Subject'] = 'Complete Your Flight Compensation Claim - GetMyClaims'

    # HTML message body
    html = f"""
    <html>
    <head>
    </head>
    <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
        <table style="border-spacing: 0;">
            <tr>
                <td style="padding: 0px;">
                    <div class="container" style="background-color: #ffffff; max-width: 600px; margin: 0 auto; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
                        <!-- Header Section with Logo -->
                        <div class="header">
                            <img src="cid:logo_image" style="width: 100%;"alt="logo">
                        </div>
                        <!-- Content Section -->
                        <div class="content" style="padding: 20px; color: #333333; font-size: 16px; line-height: 1.6;">
                            <p>Dear <strong style="color: #0047ab;">{client_name}</strong>,</p>
                            <p>We hope this email finds you well.</p>
                            
                            <p><strong style="color: #0047ab;">{partner_name}</strong> has initiated a flight compensation claim on your behalf through our partner program for your flight <strong>{flight_details}</strong>.</p>
                            
                            <p>To proceed with your claim, we need you to complete a few final steps:</p>
                            
                            <ol style="margin-left: 20px;">
                                <li><strong style="color: #0047ab;">Verify your personal information</strong></li>
                                <li><strong style="color: #0047ab;">Electronically sign the authorization form</strong></li>
                                <li><strong style="color: #0047ab;">Upload your boarding pass and any other relevant documents</strong></li>
                            </ol>
                            
                            <p>This information is necessary to process your compensation claim with the airline.</p>
                            
                            <div style="text-align: center; margin: 30px 0;">
                                <a href="{confirm_url}" style="background-color: #0047ab; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; font-weight: bold;">Complete Your Claim</a>
                            </div>
                            
                            <p>This link will expire in 7 days. If you do not wish to proceed with this claim, you can simply ignore this email.</p>
                            
                            <p>If you have any questions, please reply to this email or contact our support team.</p>
                            
                            <p>Thank you,<br>The GETMYCLAIMS.COM Team</p>
                        </div>
                        <!-- Footer Section -->
                        <div class="footer" style="text-align: center; padding: 20px; font-size: 14px; color: #888888; background-color: #f4f4f4; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
                            <p>&copy; 2024 GETMYCLAIMS.COM. All rights reserved.</p>
                        </div>
                    </div>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Attach the HTML message
    part = MIMEText(html, 'html')
    msg.attach(part)

    # Create the attachment 
    try:
        # Embed the logo image as a MIMEImage object
        with open('static/email1.png', 'rb') as img:
            logo_image = MIMEImage(img.read())
            logo_image.add_header('Content-ID', '<logo_image>')  # Reference it with "cid:logo_image" in the HTML
            msg.attach(logo_image)
    except Exception as e:
        print(f'Failed to attach logo: {e}')
    
    # Connect to the SMTP server and send the email
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(email_sender, email_password)
        server.sendmail(email_sender, msg['To'], msg.as_string())
        print(f'Email sent successfully to {client_email}!')
        return True
    except Exception as e:
        print(f'Failed to send email: {e}')
        return False
    finally:
        if server:
            server.quit()
def welcome_mail(user_id,username,user_email,password,url,flight_id,forms): #username,user_email,password
    from email.mime.base import MIMEBase
    from email import encoders
    # Create the message
    msg = MIMEMultipart('alternative')
    msg['From'] = email_sender
    msg['To'] = user_email
    msg['Subject'] = 'Welcome to GETMYCLAIMS.COM'

    # HTML message body
    html = f"""
    <html>
<head>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <table style="border-spacing: 0;">
        <tr>
            <td style="padding: 0px;">
                <div class="container" style="background-color: #ffffff; max-width: 600px; margin: 0 auto; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
                    <!-- Header Section with Logo -->
                    <div class="header">
                        <img src="cid:logo_image" style="width: 100%;"alt="logo">
                    </div>
                    <!-- Content Section -->
                    <div class="content" style="padding: 20px; color: #333333; font-size: 16px; line-height: 1.6;">
                        <p>Dear <strong style="color: #0047ab;">{ username }</strong>,</p>
                        <p>Welcome to <strong style="color: #0047ab;">GETMYCLAIMS.COM</strong>!</p>
                        <p>We are delighted to have you on board. <br><br> Your account has been created! <br><br> At GETMYCLAIMS.COM, we specialize in securing compensation for you if your flight is delayed, canceled, or if you are denied boarding. Our mission is to provide you with the best service in the market, and we pride ourselves on being reliable and efficient.</p>
                        
                        <p>Here’s what you can expect from us:</p>
                        <ul style="margin-left: 20px;">
                            <li><strong style="color: #0047ab;">Best in the Market</strong>: We are dedicated to offering top-notch service and ensuring you receive the compensation you deserve.</li>
                            <li><strong style="color: #0047ab;">Reliable</strong>: Our team is committed to providing accurate and timely assistance.</li>
                            <li><strong style="color: #0047ab;">No Charges</strong>: We don’t charge anything unless we successfully secure compensation for you.</li>
                        </ul>

                        <p><strong style="color: #0047ab;">Your Login Details:</strong></p>
                        <ul style="margin-left: 20px;">
                            <li><strong style="color: #0047ab;">Username</strong>: { user_email }</li>
                            <li><strong style="color: #0047ab;">Password</strong>: { password }</li>
                            <li><strong style="color: #0047ab;">Reference_ID</strong>: { flight_id }</li>
                        </ul>

                        <p>Please use these credentials to access your user dashboard and manage your claims.</p>

                        <p><strong style="color: #0047ab;">Next Steps:</strong></p>
                        <ol style="margin-left: 20px;">
                            <li><strong style="color: #0047ab;">Confirm Your Email</strong>: To change your password, please click <a href="{ url }">this link</a>.</li>
                            <li><strong style="color: #0047ab;">Find the Attachment</strong>: For your convenience, we have included an attachment with a consent form that you have signed. This form is necessary for us to proceed with your claims. Please review the attached signed consent form for your convenience.</li>
                        </ol>

                        <p>If you have any questions or need further assistance, don’t hesitate to reach out to our support team.</p>
                        <p>Thank you for choosing GETMYCLAIMS.COM. We look forward to helping you with your flight compensation needs.</p>
                        <p>Best regards,<br>The GETMYCLAIMS.COM Team</p>
                    </div>
                    <!-- Footer Section -->
                    <div class="footer" style="text-align: center; padding: 20px; font-size: 14px; color: #888888; background-color: #f4f4f4; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
                        <p>&copy; 2024 GETMYCLAIMS.COM. All rights reserved.</p>
                    </div>
                </div>
            </td>
        </tr>
    </table>
</body>
</html>

    """

    # Attach the HTML message
    part = MIMEText(html, 'html')
    msg.attach(part) 
    # Path to the attachment
    attachment_path = f'./uploads/{user_id}/'  # Replace with the path to your file

    # Create the attachment 
    try:
        # Embed the logo image as a MIMEImage object
        with open('static/email1.png', 'rb') as img:
            logo_image = MIMEImage(img.read())
            logo_image.add_header('Content-ID', '<logo_image>')  # Reference it with "cid:logo_image" in the HTML
            msg.attach(logo_image)

    except Exception as e:
        print(f'Failed to attach file: {e}')
    
    for form in forms:
        try:
            with open(attachment_path+form, 'rb') as attachment:
                part = MIMEBase('application', 'pdf')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(attachment_path+form)}'
                )
                msg.attach(part)
        except Exception as e:
            print(f'Failed to attach file: {e}')
    # Connect to the SMTP server and send the email
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(email_sender, email_password)
        server.sendmail(email_sender, msg['To'], msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

#old_user_script
def application_submitted(user_id,username,user_email,url,flight_id,forms): #username,user_email,password
    from email.mime.base import MIMEBase
    from email import encoders
    # Create the message
    msg = MIMEMultipart('alternative')
    msg['From'] = email_sender
    msg['To'] = user_email
    msg['Subject'] = 'Welcome to GETMYCLAIMS.COM'

    # HTML message body
    html = f"""
    <html>
<head>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <table style="border-spacing: 0; width: 100%;">
        <tr>
            <td style="padding: 0px;">
                <div class="container" style="background-color: #ffffff; max-width: 600px; margin: 0 auto; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
                    <!-- Header Section with Logo -->
                    <div class="header" style="background-color: #0047ab; color: #ffffff; text-align: center; padding: 5px; border-top-left-radius: 2px; border-top-right-radius: 2px;">
                        <img src="cid:logo_image" alt="logo" style="width: 100%; height: auto;">
                    </div>
                    <!-- Content Section -->
                    <div class="content" style="padding: 20px; color: #333333; font-size: 16px; line-height: 1.6;">
                        <p>Dear <strong style="color: #0047ab;">{ username }</strong>,</p>
                        <p>Welcome to <strong style="color: #0047ab;">GETMYCLAIMS.COM</strong>!</p>
                        <p>We are delighted to have you on board. At GETMYCLAIMS.COM, we specialize in securing compensation for you if your flight is delayed, canceled, or if you are denied boarding. Our mission is to provide you with the best service in the market, and we pride ourselves on being reliable and efficient.</p>
                        
                        <p>Here’s what you can expect from us:</p>
                        <ul style="margin-left: 20px;">
                            <li><strong style="color: #0047ab;">Best in the Market</strong>: We are dedicated to offering top-notch service and ensuring you receive the compensation you deserve.</li>
                            <li><strong style="color: #0047ab;">Reliable</strong>: Our team is committed to providing accurate and timely assistance.</li>
                            <li><strong style="color: #0047ab;">No Charges</strong>: We don’t charge anything unless we successfully secure compensation for you.</li>
                        </ul>

                        <p><strong style="color: #0047ab;">Your Application Has been submitted!:</strong></p>
                        <ul style="margin-left: 20px;">
                            <li><strong style="color: #0047ab;">Reference_ID</strong>: { flight_id }</li>
                        </ul>

                        <p>Please log-in with your credentials to access your user dashboard and manage your claims.</p>

                        <p><strong style="color: #0047ab;">Next Steps:</strong></p>
                        <ol style="margin-left: 20px;">
                            <li><strong style="color: #0047ab;">Confirm Your Email</strong>: To change your password, please click <a href="{ url }">this link</a>.</li>
                            <li><strong style="color: #0047ab;">Find the Attachment</strong>: For your convenience, we have included an attachment with a consent form that needs to be signed. This form is necessary for us to proceed with your claims. Please review the attached signed consent form for your convenience.</li>
                        </ol>

                        <p>If you have any questions or need further assistance, don’t hesitate to reach out to our support team.</p>
                        <p>Thank you for choosing GETMYCLAIMS.COM. We look forward to helping you with your flight compensation needs.</p>
                        <p>Best regards,<br>The GETMYCLAIMS.COM Team</p>
                    </div>
                    <!-- Footer Section -->
                    <div class="footer" style="text-align: center; padding: 20px; font-size: 14px; color: #888888; background-color: #f4f4f4; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
                        <p>&copy; 2024 GETMYCLAIMS.COM. All rights reserved.</p>
                    </div>
                </div>
            </td>
        </tr>
    </table>
</body>
</html>

    """

    # Attach the HTML message
    part = MIMEText(html, 'html')
    msg.attach(part) 
    # Path to the attachment
    attachment_path = f'./uploads/{user_id}/'  # Replace with the path to your file

    # Create the attachment 
    try:
        # Embed the logo image as a MIMEImage object
        with open('static/email1.png', 'rb') as img:
            logo_image = MIMEImage(img.read())
            logo_image.add_header('Content-ID', '<logo_image>')  # Reference it with "cid:logo_image" in the HTML
            msg.attach(logo_image)

    except Exception as e:
        print(f'Failed to attach file: {e}')
    
    for form in forms:
        try:
            with open(attachment_path+form, 'rb') as attachment:
                part = MIMEBase('application', 'pdf')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(attachment_path+form)}'
                )
                msg.attach(part)
        except Exception as e:
            print(f'Failed to attach file: {e}')
    # Connect to the SMTP server and send the email
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(email_sender, email_password)
        server.sendmail(email_sender, msg['To'], msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

def pass_reset(email,username,url):
    # Create the message
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email
    msg['Subject'] = 'Password Reset for GetMyClaims.com'

    # HTML message body with OTP & direct verification link
    html = f"""
    <html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <div class="container" style="background-color: #ffffff; max-width: 600px; margin: 0 auto; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
        <!-- Header Section with Logo -->
        <div class="header" style="background-color: #0047ab; color: #ffffff; text-align: center; padding: 5px; border-top-left-radius: 2px; border-top-right-radius: 2px;">
            <img src="cid:logo_image" alt="logo" style="width: 300px; height: auto;">
        </div>
        <!-- Content Section -->
        <div class="content" style="padding: 20px; color: #333333; font-size: 16px; line-height: 1.6;">
            <p style="margin: 0 0 15px;">Dear <strong style="color: #0047ab;">{username}</strong>,</p>
            <p style="margin: 0 0 15px;">We have received a request to change the password for your account at <strong style="color: #0047ab;">GETMYCLAIM.COM</strong>.</p>
            <p style="margin: 0 0 15px;">To proceed with the password change, please <a href="{url}" style="color: #0047ab; font-weight: bold; text-decoration: none;">click here</a> and enter your new password.</p>
            <p style="margin: 0 0 15px;">This email is valid for only 10 minutes.</p>
            <p style="margin: 0 0 15px;">If you did not request a password change, please ignore this email or contact our support team immediately.</p>
            <p style="margin: 0 0 15px;">If you have any questions or need further assistance, don’t hesitate to reach out to our support team.</p>
            <p style="margin: 0 0 15px;">Thank you for using GETMYCLAIMS.COM.</p>
            <p style="margin: 0 0 15px;">Best regards,<br>The GETMYCLAIMS.COM Team</p>
        </div>
        <!-- Footer Section -->
        <div class="footer" style="text-align: center; padding: 20px; font-size: 14px; color: #888888; background-color: #f4f4f4; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
            <p style="margin: 0;">&copy; 2024 GETMYCLAIMS.COM. All rights reserved.</p>
        </div>
    </div>
</body>
</html>

    """


    # Attach the HTML message
    msg.attach(MIMEText(html, 'html'))
    try:
        # Embed the logo image as a MIMEImage object
        with open('static/email1.png', 'rb') as img:
            logo_image = MIMEImage(img.read())
            logo_image.add_header('Content-ID', '<logo_image>')  # Reference it with "cid:logo_image" in the HTML
            msg.attach(logo_image)
            
    except Exception as e:
        print(f'Failed to attach file: {e}')

    # Connect to the SMTP server and send the email
    server = None

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(email_sender, email_password)
        server.sendmail(email_sender, msg['To'], msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()


# welcome_mail(user_id,username,user_email,password,url,flight_id)
# pass_reset(user_email,username,url)

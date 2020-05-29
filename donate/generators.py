from django.core.mail import send_mail
from .models import Donate
from django.urls import reverse
import string
import random
from django.core.mail import EmailMultiAlternatives


def generateCode(length=100):
    asciChar = string.ascii_letters + string.ascii_uppercase + \
        string.ascii_lowercase + string.digits
    return ''.join(random.choice(asciChar) for i in range(1, length))


def sendVerification(email, code, name):
    subject, from_email, to = 'Donasi Bersama Dontsation', 'donstation53@gmail.com', email
    text_content = 'This is an important message.'
    html_content = f'<div id=":og"><u></u> <div style="box-sizing:border-box;margin:0;padding:0;width:100%"> <table align="center" bgcolor="#EEEEEE" style="border-spacing:0;margin:0 auto;width:100%"> <tbody> <tr> <td style="padding:0"> <table align="center" bgcolor="#FFFFFF" style="margin:0 auto"> <tbody> <tr> <td colspan="2" height="30" style="font-size:30px;line-height:30px;margin:0;padding:0">&nbsp;</td> </tr> <tr style="vertical-align:top" valign="top"> <th style="width:640px;padding:5px 30px;font-weight:400" width="640"><a href="http://127.0.0.1:8000/" target="_blank"><img alt="Dontsation" height="25" src="https://i.imgur.com/EuVUtV9.png" style="margin:0;width:95px;border:0" width="95"></a> </th> <th style="width:640px;padding:5px 30px;font-weight:400;text-align:right" width="640"><a href="http://127.0.0.1:8000/" style="text-decoration:none;color:#414155;font-size:14px" target="_blank">Visit</a> </th> </tr> <tr> <td colspan="2" height="30" style="font-size:30px;line-height:30px;margin:0;padding:0">&nbsp;</td> </tr> </tbody> </table> <table align="center" bgcolor="#FFFFFF" style="border-spacing:0;margin:0 auto;border-top:1px solid #eeeeee;border-bottom:1px solid #eeeeee"> <tbody> <tr> <td height="40" style="font-size:40px;line-height:40px;margin:0;padding:0">&nbsp; </td> </tr> <tr style="vertical-align:top" valign="top"> <th style="width:640px;padding:0;padding-left:30px;padding-right:30px;color:#747487;font-size:15px;line-height:30px;font-weight:400;text-align:left" width="640"> <div style="margin-bottom:25px;font-size:15px"><img alt="" src="https://i.imgur.com/EuVUtV9.png" style="width:640px" width="640" tabindex="0"> </div> </th> </tr> <tr style="vertical-align:top" valign="top"> <th style="width:640px;padding:0;padding-left:30px;padding-right:30px;color:#747487;font-size:15px;line-height:30px;font-weight:400;text-align:left" width="640"> <div style="margin-bottom:15px;font-size:15px">Hai {name},</div> <div style="margin-bottom:15px;font-size:15px">Terimakasih telah mencoba untuk berdonasi di dontsation. semoga amal ibadah <b>{name}</b> diterima disisi-Nya. Ikutin langkah untuk mengirim donasi anda dibawah ini. </div> <div style="margin-bottom:25px;font-size:15px"> <ol> <li style="color:#747487;">Pergi ke ATM terdekat</li> <li style="color:#747487;">Transfer ke rekening: <b> 101-0002-3302-030</b></li> </ol> </div> <div style="margin-bottom:25px;font-size:15px;"><span style="color:#747487;"> Setelah melakukan pembayaran, salin code verifikasi dibawah ini </span> <blockquote style="color:#E63D4F"> {code} </blockquote> </div> <div style="margin-bottom:25px;font-size:20px;text-align:center;color:#747487;"> Atau klik button dibawah ini </div> </th> </tr> <tr style="vertical-align:top" valign="top"> <th style="width:640px;padding:0;padding-left:30px;padding-right:30px;color:#969aa1;font-size:14px;font-weight:400;text-align:left" width="640"> <center> <table bgcolor="#E63D4F" style="border-spacing:0;border-radius:3px;margin:0 auto;margin-bottom:25px;"> <tbody> <tr> <td style="padding:0"> <a href="http://127.0.0.1:8000/verify/?c={code}" style="border:0 solid #f5713a;display:inline-block;font-size:14px;padding:15px 50px 15px 50px;text-align:center;font-weight:700;text-decoration:none;color:#ffffff" target="_blank">Verifikasi</a> </td> </tr> </tbody> </table> </center> </th> </tr> </tbody> </table> </td> </tr> </tbody> </table> </div> </div>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # html = markdown.markdown(
    #     f"![Dontsation](https://i.imgur.com/EuVUtV9.png)\n\nHai {name}, Terimakasih telah mencoba untuk berdonasi di dontsation. semoga amal ibadah {name} diterima disisi-Nya.\n\n----\n## Cara Pembayaran\n1. Pergi ke ATM terdekat\n2. Transfer ke rekening: 101-0002-3302-030\n\n## Verifikasi\n### Cara Pertama\nSalin code verifikasi dibawah ini\n> {code}\n\n### Cara Kedua\n[KLIK INI](http://127.0.0.1:8000/verify/?c={code})")
    # send_mail('Donasi Bersama Dontsation',
    #           'donstation53@gmail.com',
    #           f'<p><img alt="Dontsation" src="https://i.imgur.com/EuVUtV9.png"/></p><p>Hai {name}, Terimakasih telah mencoba untuk berdonasi di dontsation. semoga amal ibadah {name} diterima disisi-Nya.</p><hr/><h2>Cara Pembayaran</h2><ol><li>Pergi ke ATM terdekat </li><li>Transfer ke rekening: 101-0002-3302-030 </li></ol><h2>Verifikasi</h2><h3>Cara Pertama</h3><p>Salin code verifikasi dibawah ini</p><blockquote><p>{code}</p></blockquote><h3>Cara Kedua</h3><p><a href="http://127.0.0.1:8000/verify/?c={code}">KLIK INI</a></p>',
    #           [email],
    #           )


def isCheck(code):
    try:
        donator = Donate.objects.get(barcode=code)
        donator.confirmation = 1
        donator.save()
        return True
    except Donate.DoesNotExist:
        pass
    return False

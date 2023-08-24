import asyncio
from aiosmtpd.controller import Controller
from email import message_from_bytes

class MailHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        # This part checks whether the mail coming in is actually
        # coming in to where it should, as in kianbrose.com which
        # is my domain. Technically not fully necessary but nice
        # to have.
        if not address.endswith('@kianbrose.com'):
            print("Address does not end with @kianbrose.com")
            return '550 not relaying to that domain'
        envelope.rcpt_tos.append(address)
        return '250 OK'
    async def handle_DATA(self, server, session, envelope):
        # This one if the sender, so if it was sent to
        # someone@gmail.com mail_from will be that
        print('Message from %s' % envelope.mail_from)

        # This is a string array of who it was sent to
        # like ['bob@xxxx.com','jeff@xxxx.com']
        # it can have a length of 1 if theres only 1 
        # person it was sent to
        print('Message for %s' % envelope.rcpt_tos)

        # If you want to print EVERYTHING in the mail
        # including useless information, use this
        #print('Message data:\n')
        #for ln in envelope.content.decode('utf8', errors='replace').splitlines():
        #    print(f'> {ln}'.strip())


        # This code is to just read the text part of the email
        # in other words the useful part that we actually, as in
        # the actual text inside the mail
        plain_text_part = None
        email_message = message_from_bytes(envelope.content)
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                plain_text_part = part.get_payload(decode=True).decode('utf-8')
                break
        if plain_text_part:
            # Do something with the plain text part
            print("Plain text content:")
            print(plain_text_part)


        # This is to finish the mail and see that it finished
        # it can be removed, just visual
        print()
        print('End of message')
        return '250 Message accepted for delivery'

# Here you start the actual server, hostname is your PRIVATE ipv4, and port has to be 25
# Change it to your actual local ipv4 or use localhost
controller = Controller(MailHandler(), hostname='192.168.10.10', port=25)
controller.start()
asyncio.get_event_loop().run_forever()

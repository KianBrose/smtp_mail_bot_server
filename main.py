import asyncio
from aiosmtpd.controller import Controller
from email import message_from_bytes

class MailHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        if not address.endswith('@kianbrose.com'):
            print("Rejected: Address doesn't end with @kianbrose.com")
            return '550 This server only accepts emails for @kianbrose.com'
        envelope.rcpt_tos.append(address)
        return '250 OK'
    
    async def handle_DATA(self, server, session, envelope):
        print('Received email from: %s' % envelope.mail_from)
        print('Recipients: %s' % ', '.join(envelope.rcpt_tos))

        email_message = message_from_bytes(envelope.content)
        plain_text_part = self.extract_plain_text(email_message)
        if plain_text_part:
            print("\nPlain text content:")
            print(plain_text_part)

        print('\nEnd of email')
        return '250 Message accepted for delivery'
    
    def extract_plain_text(self, email_message):
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode('utf-8')
        return None

async def start_server():
    handler = MailHandler()
    controller = Controller(handler, hostname='0.0.0.0', port=25)
    controller.start()
    print("SMTP server started and ready to receive emails.")
    print("You can send emails to this server.")
    print("Emails sent to addresses ending with @kianbrose.com will be accepted.")
    print("To stop the server, press Ctrl+C.")

async def main():
    server_task = asyncio.create_task(start_server())
    await server_task

if __name__ == '__main__':
    try:
        print("Welcome to the Friendly SMTP Server!")
        print("This server is designed for local testing and development purposes.")
        print("It provides a safe environment to test sending and receiving emails.")
        print("Let's get started:")
        print("1. Ensure you have an email client configured to send emails.")
        print("2. Set the SMTP server hostname to your local machine's IP address.")
        print("3. Use port 25 to connect to the server.")
        print("4. Send emails to addresses ending with @kianbrose.com.")
        print("   Emails to other addresses will be rejected.")
        print("5. To stop the server, press Ctrl+C.")
        
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSMTP server stopped. Thank you for testing!")

import firebase_admin
from firebase_admin import credentials, db


class FirebaseHandler:
    instance = None
    ref = db.reference('/')

    def __new__(cls):
        if cls.instance is None:
            service_account_info = credentials.Certificate("serviceAccountKey.json")

            firebase_admin.initialize_app(service_account_info, {
                'databaseURL': 'https://botnet-5fb37.firebaseio.com'
            })
            cls._instance = super(FirebaseHandler, cls).__new__(cls)
        return cls.instance

    @staticmethod
    async def add_email_to_firebase(sender_email_address: str, recipient_email_address: str, message: str):
        """sender_mail_address - string, recipient_email_address - string , message - string
        will be uploaded to the firebase server"""
        # Write data to a specific node
        data_to_write = {
            'Sender': sender_email_address,
            'Content': message
        }

        FirebaseHandler.ref.child(recipient_email_address).set(data_to_write)
        print("[+] Data written to Firebase.")

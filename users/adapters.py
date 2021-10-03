from allauth.account.adapter import DefaultAccountAdapter


class CustomAcountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        return f'http://localhost:3000/confirm-email/{emailconfirmation.key}'

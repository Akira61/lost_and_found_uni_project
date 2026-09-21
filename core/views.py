from django.shortcuts import render
from rest_framework.views import APIView

class ResetPasswordConfirmView(APIView):
    def get(self, request, uid, token):
        return render(request, "password_reset_confirm.html", {
            "uid": uid,
            "token": token,
        })

class UsernameResetConfirmView(APIView):
    def get(self, request, uid, token):
        return render(request, "username_reset_confirm.html", {
            "uid": uid,
            "token": token,
        })

class EmailActivationConfirmView(APIView):
    def get(self, request, uid, token):
        return render(request, "email_activation_confirm.html", {
            "uid": uid,
            "token": token,
        })

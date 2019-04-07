from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from . import models, serializers

class UserProfile(APIView):

    def get(self, request, format=None):

        user = request.user
        
        serializer = serializers.ListUserSerializer(
            user, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UpdateUserPoint(APIView):

    def post(self, request):

        user = request.user

        changed_point = request.data.get('changed_point', None)
        changed_coupon = request.data.get('changed_coupon', None)
        changed_cumulative_pay_amount = request.data.get('changed_cumulative_pay_amount', None)

        if changed_point is not None:

            user.point =  changed_point
            user.coupon_history =  changed_coupon
            user.cumulative_pay_amount =  changed_cumulative_pay_amount

            user.save()

            return Response(status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class DuplicateCheck(APIView):

    def get(self, request, format=None):

        usernameforcheck = request.query_params.get('usernameforcheck', None)

        founduser = models.User.objects.filter(
                username=usernameforcheck)

        serializer = serializers.ListUserSerializer(
            founduser, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DuplicateEmailCheck(APIView):

    def get(self, request, format=None):

        emailforcheck = request.query_params.get('emailforcheck', None)

        foundemail = models.User.objects.filter(
                email=emailforcheck)

        serializer = serializers.ListUserSerializer(
            foundemail, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DuplicateIdCheck(APIView):

    def get(self, request, format=None):

        idforcheck = request.query_params.get('idforcheck', None)

        foundid = models.User.objects.filter(
                social_id=idforcheck)

        serializer = serializers.ListUserSerializer(
            foundid, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ChangePassword(APIView):

    def put(self, request, username, format=None):

        user = request.user

        if user.username == username:

            current_password = request.data.get('current_password', None)

            if current_password is not None:

                passwords_match = user.check_password(current_password)

                if passwords_match:

                    new_password = request.data.get('new_password', None)

                    if new_password is not None:

                        user.set_password(new_password)

                        user.save()

                        return Response(status=status.HTTP_200_OK)

                    else:

                        return Response(status=status.HTTP_400_BAD_REQUEST)

                else:

                    return Response(status=status.HTTP_400_BAD_REQUEST)

            else:

                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
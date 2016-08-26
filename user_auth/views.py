import json

from django.http import HttpResponse

from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from user_auth.serializers import (
    UserSerializer
)

from user_auth import helper
from user_auth.models import User

from rest_framework.views import APIView


class CreateUserView(CreateAPIView):
    model = User
    serializer_class = UserSerializer

    def post(self, request):

        user_data = request.data

        user_data['role'] = "Normal User"
        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            user = serializer.save()

            """
            Creating social Details with provider name
            as Audetemi and provider_id as user_id
            """
            """
            This generates the OTP for the registered email
            and send the OTP to the users email.
            """
            # validated_otp_num = utils.opt_generator(user)

            # utils.send_opt_to_mail(user_data, validated_otp_num, user)

            token = helper.generate_oauth_token(
                self, user.phone_number,
                user_data.get('password'))

            if token.status_code != 200:
                return Response({'msg': 'Username or password is incorrect'},
                                status=status.HTTP_412_PRECONDITION_FAILED)

            return Response({
                'msg': 'Registration Successfully Please Verify Your Number',
                'token': json.loads(token._content)})

        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):

    model = User
    serializer_class = UserSerializer

    def post(self, request, format=None):

        if request.data:
            data = request.data

            phone_number = data.get('phone_number')
            password = data.get('password')

            user = User.objects.get(phone_number=phone_number)
            username = user.phone_number

            login_success_data = helper.generate_oauth_token(self, username, password)
            if login_success_data.status_code != 200:
                return Response(error_conf.INVALID_PASSWORD,
                                status=status.HTTP_412_PRECONDITION_FAILED)

            responce_dict = json.loads(login_success_data._content)

            if user.is_verified:
                responce_dict['is_verified'] = True
            else:
                responce_dict['is_verified'] = False

            serializer = UserSerializer(user)
            responce_dict['user'] = serializer.data

            return HttpResponse(json.dumps(responce_dict),
                                content_type='application/json')

        return Response(error_conf.NO_INPUT_DATA,
            status=status.HTTP_400_BAD_REQUEST)

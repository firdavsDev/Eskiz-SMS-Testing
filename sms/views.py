# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .helper import SendSMS

class SendSmsCodeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        configuration = SendSMS()
        phone_number = request.data.get('phone')
        if len(phone_number) == 12:

            code = configuration.generate_one_time_sms()

            result = configuration.send_sms(
                phone_number,
                code,
            )
            return Response(result)

        return Response('Phone number must be 12 digits')

send_code_api_view = SendSmsCodeAPIView.as_view()


import requests
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class FacebookBackend:
    def authenticate(self, request, code):
        """
        Facebook의 Authorization Code가 주어졌을 때
        facebook의 user_id에 해당하는  User가 있으면 해당 User리턴 없으면 생성
        :param request:
        :param code:
        :return:
        """

        def get_access_token(code):
            """
            Authorization code를 사용해 토큰을 받아옴
            :param code: 유저의 페이스북 인증 후 전달되는 Authorization code
            :return:
            """

            url = "https://graph.facebook.com/v3.0/oauth/access_token?"

            params = {
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': 'http://localhost:8000/members/facebook-login/',
                'client_secret': settings.FACEBOOK_APP_SECRET_CODE,
                'code': code,
            }
            response = requests.get(url, params=params)
            # 파이썬에 내장된 json모듈을 사용해서, JSON 형식의 텍스트를 파이썬 Object로 변환
            # response_dict = json.loads(response.text)
            response_dict = response.json()
            access_token = response_dict['access_token']
            return access_token

        def debug_token(token):
            debug_url = 'https://graph.facebook.com/debug_token?'
            debug_url_params = {
                'input_token': token,
                'access_token': settings.FACEBOOK_APP_ID + '|' + settings.FACEBOOK_APP_SECRET_CODE,
            }
            response = requests.get(debug_url, debug_url_params)
            return response.json()

        def get_user_info(token, fields=None):
            if not fields:
                fields = ['id', 'name', 'first_name', 'last_name', 'picture', ]
            else:
                fields = ','.join(list(fields))

            url = 'https://graph.facebook.com/v3.0/me'
            params = {
                'fields': fields,
                'access_token': token,
            }
            response = requests.get(url, params)

            return response.json()

        def create_user_from_facebook_user_info(user_info):
            facebook_user_id = user_info['id']
            first_name = user_info.get('first_name','')
            last_name = user_info.get('last_name','')
            url_img_profile = user_info['picture']['data']['url']

            user, user_created = User.objects.get_or_create(
                username=facebook_user_id,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                },
            )
            return user, user_created

        access_token = get_access_token(code)
        user_info = get_user_info(access_token)
        user, user_created = create_user_from_facebook_user_info(user_info)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExits:
            return None

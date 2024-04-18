from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from django.conf import settings
import jwt
from rest_framework.exceptions import AuthenticationFailed
import uuid


        
class jwtAuthentication(TokenAuthentication):
   
    def authenticate_credentials(self, key):
        #import pdb;pdb.set_trace()
        model = self.get_model()
        try:
            #token = model.objects.select_related('user').get(key=key)
            user = jwt.decode(key,"django-insecure-7ag3aue)q^+7xy1zrhvpxxv=us84=_@u^=nw+d3c6-jxhveh6u",algorithms="HS256")
            #usr_inst = User.objects.get(username=user["username"])
            user['is_authenticated'] = True
        except Exception as err:
            raise AuthenticationFailed('Invalid token.')
 
       
        except jwt.ExpiredSignatureError:
            return None
 
        return (user, key)
    def get_token_from_header(self, request):
        header = request.headers.get("Authorization")
        if header and header.startswith("Token "):
            return header.split(" ")[1]
        return None





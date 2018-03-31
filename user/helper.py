from user.models import *
from user.utils import *


def sign_up(request: HttpRequest):
    params = signup_request_to_dic(request)
    user = Profile.objects.create(
        
    )



def log_in(request: HttpRequest):
    print("A")
class authenticator:
    def authenticate_user(self,auth_type:str,user:str = None,password:str = None,token:str = None):
        if auth_type == 'username_password':
            if user == 'admin' and password == 'password':
                print(f"{user} authenticated through username and password")
                return True
            else:
                print("incorrect username/password")
                return False

        elif auth_type == 'google authentication':
            if token == 'ValidToken':
                print(f"User authenticated through google OAuth token")
                return True
            else:
                print("Invalid token")
                return False
        
        elif auth_type == "Facebook authentication":
            if token == 'ValidFBToken':
                print("login through facebook successful")
                return True
            else:
                print("Incorrect token")
                return False

from abc import ABC, abstractmethod
class authenticator(ABC):
    @abstractmethod
    def authenticate(self,credentials) ->bool:
        pass

class UsernamePasswordAuthentication(authenticator):
    def authenticate(self, credentials:dict)->bool:
        username = credentials.get("username")
        password = credentials.get("Password")

            if username == 'admin' and password == 'password':
                print(f"{user} authenticated through username and password")
                return True
            else:
                print("incorrect username/password")
                return False
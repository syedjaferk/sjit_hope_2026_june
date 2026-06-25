class RealObject:
    def perform_action(self):
        print("RealObject performing action")

class Proxy:
    def __init__(self, user):
        self._real_object = RealObject()
        self._user = user

    def perform_action(self):
        if self._user == "admin":
            self._real_object.perform_action()
        else:
            print("Access denied for non-admin user")

# Client code
admin_proxy = Proxy("admin")
admin_proxy.perform_action()

user_proxy = Proxy("user")
user_proxy.perform_action()
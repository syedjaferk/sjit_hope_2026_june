from locust import HttpUser, task, constant
import random

class UsernameCheckUser(HttpUser):
    wait_time = constant(0)

    @task(80)
    def existing_user(self):
        user_id = random.randint(1, 1000000)

        self.client.get(
            f"/usernames/user{user_id}",
            name="Existing Username Check"
        )

    @task(20)
    def non_existing_user(self):
        user_id = random.randint(
            1000001,
            2000000
        )

        self.client.get(
            f"/usernames/user{user_id}",
            name="Non Existing Username Check"
        )

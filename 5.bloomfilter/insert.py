from locust import HttpUser, task, constant
import uuid

class UsernameInsertUser(HttpUser):
    wait_time = constant(0)

    @task
    def insert(self):
        self.client.post(
            "/upload",
            json={
                "username": f"user-{uuid.uuid4()}"
            },
            name="Insert Username"
        )

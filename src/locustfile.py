from locust import HttpUser, task
from requests.auth import HTTPBasicAuth
import requests
import random
import os

with open("output.txt", "a") as f:
    f.write(f"_________________________________________________\n")

class NextcloudUser(HttpUser):
    auth = None
    users_list = list(range(1, 20))

    def on_start(self):
        random.shuffle(self.users_list)
        i = self.users_list.pop()
        self.user = 'user' + '{:d}'.format(i)
        self.password = 'Mj8VldcvKqBsI65'
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.verify_authentication()


    def verify_authentication(self):
        response = self.client.head("/remote.php/dav", auth=self.auth)
        if response.status_code != 200:
            with open("output.txt", "a") as f:
                f.write(f"Authentication failed for user {self.user}: {response.text}.\n")
            raise Exception(f"Authentication failed for user {self.user}")


    @task
    def propfind(self):
        try:
            response = self.client.request("PROPFIND", "/remote.php/dav", auth=self.auth)
            response.raise_for_status()
        except Exception as e:
            with open("output.txt", "a") as f:
                f.write(f"Error during PROPFIND request: {e} for user {self.user}.\n")
                

"""

    @task
    def upload_small(self):
        filename = "picture.png"
        with open("files_test/" + filename, 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                       auth=self.auth, data=f, name="/remote.php/dav/files/[user]/picture.png")

        if response.status_code != 201 and response.status_code != 204 :
            with open("output.txt", "a") as f:
                f.write(f"Error during PUT request: {response.status_code} for user {self.user}.\n")
            return

        for i in range(0,5):
            self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                            auth=self.auth, name="/remote.php/dav/files/[user]/picture.png")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                           auth=self.auth, name="/remote.php/dav/files/[user]/picture.png")




    @task
    def upload_medium(self):
        filename = "dataset.dat"
        with open("files_test/" + filename, 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                    auth=self.auth, data=f, name="/remote.php/dav/files/[user]/dataset.dat")

        if response.status_code != 201 and response.status_code != 204:
            with open("/mnt/locust/output.txt", "a") as f:
                f.write(f"Error during PUT request: {response.status_code} for user {self.user}.\n")
            return

        for i in range(0, 5):
            self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                            auth=self.auth, name="/remote.php/dav/files/[user]/dataset.dat")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                        auth=self.auth, name="/remote.php/dav/files/[user]/dataset.dat")


    @task
    def upload_large(self):
        filename = "lotr.mp4"
        with open("files_test/" + filename, 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                       auth=self.auth, data=f, name="/remote.php/dav/files/[user]/lotr.mp4")
	
        if response.status_code not in (201, 204):
            with open("/mnt/locust/output.txt", "a") as f:
                f.write(f"Error during PUT request: {response.status_code} for user {self.user}.\n")
            return

        
        self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                        auth=self.auth, name="/remote.php/dav/files/[user]/lotr.mp4")
        

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                        auth=self.auth, name="/remote.php/dav/files/[user]/lotr.mp4")
                        


"""

# Cloud-base-Springer

A repository dedicated for the final assignment of the Cloud Computing course.

## Overview

The exercise was about deploying, explaining and testing a local cloud-based storage system.
The proposed solution is a containerized instance of Nextcloud, linked to a MariaDB database.
All the tests were conducted with the softwere Locust. In the file `SPRINGER_repor.pdf` you can find all the details and explanations.

## How do deploy the system?

First of all make sure you have Docker installed with the following bash command:

```{bash, eval=FALSE}
docker --version
```

Then navigate to `src/` and install the images of Nextcloud and MariaDB with the command

```{bash, eval=FALSE}
sudo docker-compose up -d
```

As explained in the report, the `-d` flag ensures the running in the background of the system, but it can also be called without `-d` , for a more controlled environment of the system.

## Accessing the cloud

After deploying the system, you can open a web browser and navigate to the selected port in the `docker-compose.yaml` file, in this case port `8081`:

 - `http://localhost:8081/`
 
 This will open the cloud's interface from where many operations can be made.
 First of all log in with the selected credentials (also  defined in the same file), in this case:
 
  - username: `christian`
  - password: `Mj8VldcvKqBsI65`
  
Once logged in, the admin can: 

 - create new users (both users and admins)
 - manage existing users
 - change credentials
 - manage files (upload, access, delete)
 - personalize settings
 
Regular users can only change their credentials and manage their files. Their account is given to them by an admin.

## Testing

You create new users by running the command

```{bash, eval=FALSE}
chmod +x create_nextcloud_users.sh
./create_nextcloud_users.sh
```
This will create 20 new users named user1, user2, ecc. all with the same password (in this case the same of the admin's despite the fact that this is not secure and a proper admin should define separated and harder to guess passwords to ensure more protection at first). These accounts can be handed out to trusted people, which can then access the cloud, modify their credentials and have a user account to the cloud.

To test the performance of the system, one way is to make sure to have `Locust`installed by running the command

```{bash, eval=FALSE}
locust --version
```

After that, go to the `src/` directory and run the command

 - `locust -f locustfile.py --host=http://localhost:8081`
 
Keep in mind to change the last digits corresponding on the port selected when running the docker-compose file.

This will link Locust to Nextcloud, and the default port will be port `8089`, so to access Locust now open a web browser and navigate to

 - `http://localhost:8089/`
 
Keep in mind to not assign port 8089 when running the docker-compose file to avoid conflicts with the default setting of Locust and keep this port open for it.

Once there you can perform any test of performance from those in the `locustfile.py`, by taking the rest of them and putting them at the end of the file, like shown in the file.

For all the test, expect the large upload, the parameters used were

 - number of users: 10
 - deploy rate: 2
 
In the large upload case only 5 users were selected.

## Credits

This project was created by Christian Špringer (christian.springer228@gmail.com).


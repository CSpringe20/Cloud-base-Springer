#!/bin/bash

URL="http://localhost:8081/ocs/v1.php/cloud/users"
USERNAME="christian"
PASSWORD="R4njfkecicgmme"
PASSWORD_ENCODED="abc123abc!" 


for i in {1..20}; do
    USERID="user$i"
    docker exec -i -u 33 cloud_app_1 bash -c "export OC_PASS=$PASSWORD && /var/www/html/occ user:add $USERID --password-from-env"
done

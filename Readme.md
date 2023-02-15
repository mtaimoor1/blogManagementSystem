# Setting up the environment
Set up an virtual env and install the dependencies using the following command
```bash
pip install -r requirements.txt
```
After installation is finished, export the following environment variables
```bash
export PG_HOST='localhost'
export PG_DATABASE='blogDB'
export PG_USER='root'
export PG_PASS='password'
```
# Setting up the Postgres Database

To set up the database, go to the root project folder and run the following command
```bash
docker-compose up -d
```
After the database is up and running log in to pgadmin dashboard that is running on ***localhost:5050***. Use the credentials mentioned in the docker-compose file i.e. **user: ***admin@admin.com*** pass: ***root*****

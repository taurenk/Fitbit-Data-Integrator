# Fitbit-Data-Integrator
FDI is an ETL written in Python for automatically integrating Fitbit data into a datastore for mining and analytics. 


Fitbit Data Warehouse is an ETL tool for continuously integrating user's fitbit data into a PostgreSQL warehouse. 
The aim is to create a scalable data store in an effort to mine Fitbit data.

## Env Vars
```
    CLIENT_ID=
    CLIENT_SECRET=
    DB_NAME=
    DB_URL=
    DB_USERNAME=
    DB_PASSWORD=
    PYTHONUNBUFFERED=1
```

## PostgreSQL Setup

```
    CREATE TABLE users (
        id			serial PRIMARY KEY,
        fullname		varchar(64) NOT NULL,
        email		varchar(64) NOT NULL,
        refresh_token   	varchar(128),
        last_refresh	DATE
    );
    
    CREATE TABLE hrdata (
        id		serial PRIMARY KEY,
        user_id serial references users(id),
        date	DATE,
        time	TIME,
        heart_rate int
    );
    
    // Test Data
    INSERT INTO users (fullname, email, refresh_token, last_refresh) VALUES ('Tauren', 't@gmail.com', '123', '09/13/2015');
    INSERT INTO hrdata (user_id, date, time, heart_rate) VALUES (1, '10/13/2015', '00:30:00', 65);
    SELECT * FROM users,hrdata;
```
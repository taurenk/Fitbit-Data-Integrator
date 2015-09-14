# Fitbit-Data-Integrator
FDI is an ETL written in Python for automatically integrating Fitbit data into a datastore for mining and analytics. 


Fitbit Data Warehouse is an ETL tool for continuously integrating user's fitbit data into a PostgreSQL warehouse. 
The aim is to create a scalable data store in an effort to mine Fitbit data.

#### Notes/Thoughts/Observations
1. hrdata table
    - If a user wears there fitbit for a fullday and we use the "1min" time series, 
    we would have 1440 entries for just that day [1440 mins == 24 hours]. 
2. Summary table
    - need to add a summary table that either exists as join table between users and hr data or sits independently. 
    -  Summary data in object "heartRateZones":[{
								"caloriesOut":1598.0272,"max":97,"min":30,"minutes":604,"name":"Out of Range"},
								{"caloriesOut":581.2576,"max":136,"min":97,"minutes":78,"name":"Fat Burn"},
								{"caloriesOut":69.608,"max":165,"min":136,"minutes":6,"name":"Cardio"},
								{"caloriesOut":0,"max":220,"min":165,"minutes":0,"name":"Peak"}
								],"restingHeartRate":56}}]
    - Could use this aggregating data for research
3. Age/day-time join table
    - As more data points get added (steps, water, etc) we may want a join table that contains a user's age + current 
     day for the daily data set. that could help in data aggregations/pipes

 
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
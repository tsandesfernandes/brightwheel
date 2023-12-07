# home assessment

## notes
I went with a very simple approach using lists and dicts
Initially I tried to use the s3 creds but the creds provided wont work
I setup a docker postgres image running on port 5455

a quick check if data was inserted
```
postgres=# select distinct source from assessment;
  source  
----------
 Nevada
 Oklahoma
```
I didnt do any additional validation, just made sure the insert was working
To me data didnt make much sense, so make data standard wasnt straight forward

I skipped texas dataset on purpose since it was asked 2 hours for this exercise

I spent most of time trying to understand the data instead of coding

to run the job needs to set up a local postgres running on 5455 with the user and password from the load_data file

## considerations

for full refresh like mentioned in the doc I would change for a delete insert or upsert based on some unique field
Didnt think in scaling for this exercise, but it can be done changing to pyspark

## running

it's a pretty simple job
just need to call load_data with the csv files in the same folder
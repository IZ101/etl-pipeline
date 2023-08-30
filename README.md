## ETL Pipeline v.1

### Building an ETL pipeline that carries out the following tasks:
- Extracts transactional data from redshift warehouse
- Cleans transactional data and removes duplicates
- Loads transformed data to Bootcamp's s3 bucket

### Requirements
- The minimum requirement is Python v.3+

### Instructions on how to execute the code
- Install all the libraries you will need to execute main.py

        pip3 install -r requirements.txt

- Copy the .env.example file to .env and fill out the environment vars
- Run the main.py script. You will need to import dotenv and load the environment variables

        python3 main.py

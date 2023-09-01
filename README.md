## ETL Pipeline v2

### Introduction
You will build an ETL pipeline to perform the range of tasks as follows:
- Extract transactional data from two tables online_transactions and stock_code from Redshift
- Join the tables and clean any missing data for customer id, stock code and stock description columns
- Transform the data by finding and removing full duplicates
- Load the transformed data to an s3 bucket

### Requirements
  The minimum requirements:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)
- Docker for Windows: 
  - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
  - Manual installation steps for older WSL version: [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

### Instructions on how to execute the code
- Copy the `.env.example` file to `.env` and fill out the environment vars.

- Make sure you are executing the code from the folder where you have your main.py file and you have Docker Desktop running.


To run it locally first build the image.

```bash
  docker image build -t etl .
```

Then run the etl job using docker:
```bash
  docker run --env-file .env etl
```
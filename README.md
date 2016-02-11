## Important Notice
When using pgadmin, the execution time at status bar is including data transfer time, unfortunately, postgre-9.2_vs_mariadb-10.0.22 is using pgadmin status bar execution time to compare with mysql server execution time which is unfair. I will update the correct benchmark soon.

## Get Config
- postgresql: `show all;`
- mysql: `show variables;`

## How to Benchmark
1. Using similar table structure: located at {db}.sql
2. Use python script to generate sql insert data
3. Open sqlyog to benchmark MariaDB(MySQL)
4. Open pgAdmin to benchmark PostgreSQL
5. All setting are using default: setting related file can be found at {benchmark_folder}/{db}_config.txt

## To Do
Automate benchmark process with python, however need to make sure the benchmark time is using raw execution time, without the transfer time + python script time.

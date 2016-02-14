## Introduction
The intention of this benchmark script is a starting of decentralized database benchmark tool. The script might be not complete in feature but slowly we can enhance it. 

This repo structure ultimately still have a lot to be changed, feel free to criticize in an open opinion way or use it for your own benchmark.

## Advised benchmark procedure
- Put benchmark environment detail to `{folder}/readme.md`
- Use docker container to perform benchmark, only 1 container running at 1 time
- Install anaconda with MySQLdb + psycopg2 package to execute benchmark remotely

## How to Benchmark
1. Use similar table structure: located at {db}.sql
2. `python word_list_generate.py` to generate new sql insert script
3. `python benchmark.py` to start benchmark
  - currently have to manually edit hardcoded value to perform benchmark

## To Do
- No need to comment & uncomment benchmark.init(): to detect if exist database don't create or drop and create
- pass argv optionally to benchmark mysql/mariadb/postgres 
- Include more features to benchmark: index, joining, disk usage
- exclude transfer time in benchmark by passing a param: also has to make sure databases raw execute time is measuring in same way internally
- Script or other methods to make all three database in same/similar config, this should be optional to run.
- More database to benchmark, preferably nosql database
- Decouple read query(q1 - q6) to another file, write query and database in pit query should be configurable too
- In benchmark summary should auto populate query used or query version, script version or commit version
- Benchmark should summarized all database summary and generate a html result with chart(preferably with JS)

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
- Make python 3 compatible
- No need to comment & uncomment benchmark.init()
- pass argv optionally to benchmark mysql/mariadb/postgres 

### Result
![chart](chart.png?raw=true "Chart")

- mariadb(mysql) write (10000 rows): from insert.sql, run 10x time accumulate to 100000 rows
    1. 0.281s
    2. 0.131s
    3. 0.165s
    4. 0.146s
    5. 0.248s
    6. 0.141s
    7. 0.136s
    8. 0.208s
    9. 0.157s
    10. 0.155s

- postgresql write (10000 rows): from insert.sql, run 10x time accumulate to 100000 rows
    1. 0.227s
    2. 0.256s
    3. 0.215s
    4. 0.227s
    5. 0.194s
    6. 0.195s
    7. 0.203s
    8. 0.205s
    9. 0.174
    10. 0.182s

### simple query
taking average of multiple time query

1. `SELECT * FROM testing LIMIT 1000`
    - mariadb(mysql):0.007s
    - postgresql: 0.047s

2. `SELECT * FROM testing WHERE int_col > 5000 LIMIT 1000`
    - mariadb(mysql):0.007s
    - postgresql: 0.044s

3. `SELECT * FROM testing WHERE int_col + int_col2 > 12345`
    - mariadb(mysql): 0.008s
    - postgresql: 0.045s

4. `SELECT COUNT(*) FROM testing WHERE int_col + int_col2 > 12345`
    - mariadb(mysql): 0.040s
    - postgresql: 0.021s

5. `SELECT * FROM testing WHERE int_col > 5000 ORDER BY word_col ASC LIMIT 1000`
    - mariadb(mysql): 0.106s
    - postgresql: 0.093s

6. `SELECT * FROM testing WHERE word_col LIKE '%lim%' ORDER BY word_col DESC LIMIT 1000`
    - mariadb(mysql): 0.093s
    - postgresql: 0.058s

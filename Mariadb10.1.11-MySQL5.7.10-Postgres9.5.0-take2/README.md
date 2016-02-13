### Vagrant Setup
- Ubuntu wily werewolf (15.10): "ubuntu/wily64"
- 1 core CPU, 100% execution cap
- 1024 MB memory

### Docker Image
- mariadb:10.1.11
- mysql:5.7.0
- postgres:9.5.0

### Postgres Result
- average write time: 77.2ms/10000rows
- average query time (q1): 3.05ms
- average query time (q2): 3.67ms
- average query time (q3): 3.95ms
- average query time (q4): 159.54ms
- average query time (q5): 223.2ms
- average query time (q6): 188.91ms

### MySQL Result
- average write time: 58.95ms/10000rows
- average query time (q1): 4.5ms
- average query time (q2): 4.23ms
- average query time (q3): 5.02ms
- average query time (q4): 272.6ms
- average query time (q5): 632.92ms
- average query time (q6): 574.28ms

### MariaDB Result
- average write time: 49.62ms/10000rows
- average query time (q1): 3.85ms
- average query time (q2): 4.28ms
- average query time (q3): 4.8ms
- average query time (q4): 250.34ms
- average query time (q5): 5506.49ms
- average query time (q6): 501.29ms

### query read
```json
{
  "q1" : "SELECT * FROM testing LIMIT 1000",
  "q2" : "SELECT * FROM testing WHERE int_col > 5000 LIMIT 1000",
  "q3" : "SELECT * FROM testing WHERE int_col + int_col2 > 12345 LIMIT 1000",
  "q4" : "SELECT COUNT(*) FROM testing WHERE int_col + int_col2 > 12345",
  "q5" : "SELECT * FROM testing WHERE int_col > 5000 ORDER BY word_col ASC LIMIT 1000",
  "q6" : "SELECT * FROM testing WHERE word_col LIKE '%lim%' ORDER BY word_col DESC LIMIT 1000"
}
```

import time
current_milli_time = lambda: time.time() * 1000
import MySQLdb
import psycopg2


class Benchmark:
    def __init__(self, dbtype, arr_dict):
        self.time_unit = 'ms'
        self.read_query = {
            "q1": "SELECT * FROM testing LIMIT 1000",
            "q2": "SELECT * FROM testing WHERE int_col > 5000 LIMIT 1000",
            "q3": "SELECT * FROM testing WHERE int_col + int_col2 > 12345 LIMIT 1000",
            "q4": "SELECT COUNT(*) FROM testing WHERE int_col + int_col2 > 12345",
            "q5": "SELECT * FROM testing WHERE int_col > 5000 ORDER BY word_col ASC LIMIT 1000",
            "q6": "SELECT * FROM testing WHERE word_col LIKE '%lim%' ORDER BY word_col DESC LIMIT 1000"
        }
        self.query = {}
        if dbtype == 'mariadb':
            self.pre = 'ma'
            self.db_initfile = 'mysql.sql'
            self.query['truncate'] = 'TRUNCATE TABLE testing'
            self.query['config'] = 'show variables;'
        elif dbtype == 'mysql':
            self.pre = 'my'
            self.db_initfile = 'mysql.sql'
            self.query['truncate'] = 'TRUNCATE TABLE testing'
            self.query['config'] = 'show variables;'
        elif dbtype == 'postgres':
            self.pre = 'pg'
            self.db_initfile = 'postgres.sql'
            self.query['truncate'] = 'TRUNCATE TABLE testing RESTART IDENTITY'
            self.query['config'] = 'show all;'

        self.host = arr_dict['host']
        self.user = arr_dict['user']
        self.passwd = arr_dict['passwd']
        self.db = 'benchmark'
        self.write_dir = 'benchmark'

    def init(self):
        if self.pre == 'pg':
            self.pg_init()
        else:
            self.my_init()

    def my_init(self):
        mc = self._connect()
        r = mc.cursor()
        with open(self.db_initfile, 'r') as myfile:
            data = myfile.read().replace('\n', ' ')
        r.execute(data)
        r.close()
        print("mysql benchmark table + DB init successfully")

    def pg_init(self):
        pc = self._connect()
        pc.set_isolation_level(0)  # PostgreSQL can not drop databases within a transaction,
        r = pc.cursor()
        with open(self.db_initfile, 'r') as myfile:
            query = myfile.read().replace('\n', ' ')
        query = query.split(';')  # postgres create database is strict
        r.execute(query[0] + ';')
        r.close()
        pc = self._connect_db()
        r = pc.cursor()
        r.execute(query[1] + ';')
        r.close()
        pc.commit()
        print("postgres benchmark table + DB successfully")

    def truncate(self):
        conn = self._connect_db()
        r = conn.cursor()
        r.execute(self.query['truncate'])
        r.close()
        conn.commit()
        conn.close()

    def write(self):
        self.truncate()
        with open('sql/insert.sql', 'r') as myfile:
            query = myfile.read().replace('\n', '')
        iter = 100
        wf = open(self.write_dir + '/' + self.pre + '_write.txt', 'wb')
        for x in range(0, iter):
            conn = self._connect_db()
            r = conn.cursor()
            t1 = current_milli_time()
            r.execute(query)
            t2 = current_milli_time()
            time_used = t2 - t1
            wf.write(str(time_used) + '\n')
            r.close()
            conn.commit()
            conn.close()
        wf.close()

    def read(self):
        for key in self.read_query:
            self._query(self.read_query[key], key)

    def _query(self, query, filename):
        iter = 100
        wf = open(self.write_dir + '/' + self.pre + '_' + filename + '.txt', 'wb')
        for x in range(0, iter):
            conn = self._connect_db()
            r = conn.cursor()
            t1 = current_milli_time()
            r.execute(query)
            t2 = current_milli_time()
            time_used = t2 - t1
            wf.write(str(time_used) + '\n')
            r.close()
            conn.close()
        wf.close()

    def config(self):
        wf = open(self.write_dir + '/' + self.pre + '_config.txt', 'wb')
        conn = self._connect_db()
        r = conn.cursor()
        r.execute(self.query['config'])
        for row in r:
            wf.write(str(row[0]) + ': ' + str(row[1]) + '\n')
        r.close()
        conn.close()
        wf.close()

    def summary(self):
        wf = open(self.write_dir + '/' + self.pre + '_summary.txt', 'wb')
        f = open(self.write_dir + '/' + self.pre + '_write.txt', 'r')
        total_time = 0
        total_line = 0
        for line in f:
            line = line.strip()
            if line != '':
                total_line = total_line + 1
                total_time = total_time + float(line)
        avg_time = total_time / total_line
        wf.write('average write time: ' + str(avg_time) + self.time_unit + '/10000rows\n')
        f.close()

        for key in self.read_query:
            f = open(self.write_dir + '/' + self.pre + '_' + key + '.txt', 'r')
            total_time = 0
            total_line = 0
            for line in f:
                line = line.strip()
                if line != '':
                    total_line = total_line + 1

        wf.close()

    def _connect(self):
        if self.pre == 'pg':
            return psycopg2.connect(host=self.host, user=self.user, password=self.passwd)
        else:
            return MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd)

    def _connect_db(self):
        if self.pre == 'pg':
            return psycopg2.connect(host=self.host, user=self.user, password=self.passwd)
        else:
            return MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)

dict_connection = {
    'host': 'uvm',
    'user': 'root',
    'passwd': 'root'
}
benchmark_db = 'mysql'
if benchmark_db == 'postgres':
    dict_connection['user'] = 'postgres'
    dict_connection['passwd'] = 'postgres'

benchmark = Benchmark(benchmark_db, dict_connection)
# benchmark.init() # comment benchmark.init() to disable initialize database + table
benchmark.config()
benchmark.write()
benchmark.read()
benchmark.summary()

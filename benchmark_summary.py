from __future__ import division

def summary(prefix="my", time_unit='ms'):
    wf = open('benchmark/'+prefix+'_summary.txt', 'wb')
    f = open('benchmark/'+prefix + '_write.txt', 'r')
    total_time = 0
    total_line = 0
    for line in f:
        line = line.strip()
        if line != '':
            total_line = total_line + 1
            total_time = total_time + int(line)
    avg_time = total_time/total_line
    wf.write('average write time: '+ str(avg_time) + time_unit + '/10000rows\n')
    f.close()

    q_max = 6
    for x in range(0, q_max):
        i = x+1
        f = open('benchmark/'+prefix + '_q'+str(i)+'.txt', 'r')
        total_time = 0
        total_line = 0
        for line in f:
            line = line.strip()
            if line != '':
                total_line = total_line + 1
                total_time = total_time + int(line)
        avg_time = total_time/total_line
        wf.write('average query time (query '+ str(i) +'): '+ str(avg_time) + time_unit + '\n')
        f.close()
    wf.close()

summary("my")
summary("pg")

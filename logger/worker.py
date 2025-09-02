import time, os, json

LOG_SOURCE = os.environ.get('LOG_SOURCE','/tmp/backend_events.log')
OUTFILE = os.environ.get('OUTFILE','/tmp/collected_logs.txt')

def tail_file(path):
    try:
        with open(path,'r') as f:
            # seek to end and then yield new lines
            f.seek(0,2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                yield line
    except FileNotFoundError:
        while True:
            time.sleep(1)

if __name__ == '__main__':
    print('Logger worker started. Reading from', LOG_SOURCE)
    for line in tail_file(LOG_SOURCE):
        try:
            obj = json.loads(line)
        except Exception:
            obj = {"raw": line.strip()}
        with open(OUTFILE,'a') as fout:
            fout.write(json.dumps(obj) + "\n")

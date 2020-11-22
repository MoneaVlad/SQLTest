import time
from time import sleep

def test_function():
    pass

IP = '127.0.0.1'
PORT = 5432

QPS = 250
TEST_DURATION = 10 * 60

if __name__ == "__main__":
    for second in range(TEST_DURATION):

        start_time = int(round(time.time() * 1000))
        for query in range(QPS):
            test_function()

        end_time = int(round(time.time() * 1000))

        sleep_time = (1000.0 - float(end_time - start_time))/1000.0
        print(f"[Iteration: {second + 1}/{TEST_DURATION}] Sleeping for: {sleep_time}", )
        sleep(sleep_time)



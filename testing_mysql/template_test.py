import time
from time import sleep



# testing_mysql.write_test.test_one_write
import testing_mysql.write_test

# testing_mysql.read_test.test_one_read
import testing_mysql.read_test

test_function = testing_mysql.write_test.test_one_write

IP = '127.0.0.1'
PORT = 3306

QPS = 10
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



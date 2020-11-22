import socket
from concurrent.futures import ThreadPoolExecutor
import time
from time import sleep
import docker

IP = '127.0.0.1'
PORT = 5432

QPS = 250
TEST_DURATION = 10 * 60


def create_one_connection(address, port):
	sock = socket.socket()
	sock.connect((address, port))
	sock.close()


if __name__ == "__main__":
	for second in range(TEST_DURATION):

		start_time = int(round(time.time() * 1000))
		for query in range(QPS):
			create_one_connection(IP, PORT)

		end_time = int(round(time.time() * 1000))
		
		sleep_time = (1000.0 - float(end_time - start_time))/1000.0
		print(f"[Iteration: {second + 1}/{TEST_DURATION}] Sleeping for: {sleep_time}", )
		sleep(sleep_time)



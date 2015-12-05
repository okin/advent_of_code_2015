import multiprocessing
import sys
from hashlib import md5


def mine_advent_coin(secret, zeroes=5):
    starting_zeroes = zeroes * '0'
    with multiprocessing.Pool(processes=2) as pool:
        in_gen = generate_input(secret)
        for number, found_hash in pool.imap(compute, in_gen, chunksize=128):
            if number % 1000 == 0:
                print('.', end='')
            if found_hash.startswith(starting_zeroes):
                break

    return number, found_hash


def generate_input(secret):
    for i in range(sys.maxsize):
        yield i, secret + str(i)


def compute(params):
    number, text = params
    return number, compute_hash(text)


def compute_hash(text):
    h = md5()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


if __name__ == '__main__':
    number, found_hash = mine_advent_coin('ckczppom')
    print(number)

    number, found_hash = mine_advent_coin('ckczppom', 6)
    print(number)

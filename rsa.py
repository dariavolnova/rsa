import random
from math import gcd

def get_primes(limit=10**6):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def coprime(a, b):
    return gcd(a, b) == 1

def inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def get_keys(prime_list):
    p = random.choice(prime_list)
    q = random.choice(prime_list)
    while q == p:
        q = random.choice(prime_list)

    n = p * q
    totient = (p - 1) * (q - 1)

    e = 65537
    if not coprime(e, totient):
        for i in range(3, totient, 2):
            if coprime(i, totient):
                e = i
                break

    d = inverse(e, totient)
    return (e, n), (d, n)

def encrypt(text, pub_key):
    e, n = pub_key
    return [pow(ord(char), e, n) for char in text]

def decrypt(code, priv_key):
    d, n = priv_key
    return ''.join(chr(pow(c, d, n)) for c in code)

if __name__ == "__main__":
    msg = input("Введите сообщение для шифрования: ")

    print("Генерация ключей...")
    prime_list = get_primes()
    pub_key, priv_key = get_keys(prime_list)

    encrypted_msg = encrypt(msg, pub_key)
    decrypted_msg = decrypt(encrypted_msg, priv_key)

    print("\nОткрытый ключ (e, n):", pub_key)
    print("Закрытый ключ (d, n):", priv_key)
    print("Зашифрованное сообщение:", encrypted_msg)
    print("Расшифрованное сообщение:", decrypted_msg)
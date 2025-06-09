import unittest
from rsa import get_primes, get_keys, encrypt, decrypt, coprime, inverse

class TestRSA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prime_list = get_primes(10000)  # Ограничим ради скорости
        cls.public_key, cls.private_key = get_keys(cls.prime_list)

    def test_encrypt_decrypt_basic(self):
        text = "Hello, RSA!"
        encrypted = encrypt(text, self.public_key)
        decrypted = decrypt(encrypted, self.private_key)
        self.assertEqual(text, decrypted)

    def test_encrypt_decrypt_empty_string(self):
        text = ""
        encrypted = encrypt(text, self.public_key)
        decrypted = decrypt(encrypted, self.private_key)
        self.assertEqual(text, decrypted)

    def test_encrypt_decrypt_one_char(self):
        text = "A"
        encrypted = encrypt(text, self.public_key)
        decrypted = decrypt(encrypted, self.private_key)
        self.assertEqual(text, decrypted)

    def test_encrypted_type(self):
        encrypted = encrypt("RSA", self.public_key)
        self.assertTrue(all(isinstance(c, int) for c in encrypted))

    def test_keys_are_coprime(self):
        e, n = self.public_key
        d, _ = self.private_key
        p1, p2 = [n // d for d in self.prime_list if n % d == 0][:2]
        phi = (p1 - 1) * (p2 - 1)
        self.assertTrue(coprime(e, phi))

    def test_inverse_modulo(self):
        a = 17
        m = 3120
        inv = inverse(a, m)
        self.assertEqual((a * inv) % m, 1)

    def test_different_keys_unique(self):
        pub2, priv2 = get_keys(self.prime_list)
        self.assertNotEqual(self.public_key, pub2)
        self.assertNotEqual(self.private_key, priv2)

    def test_long_text(self):
        text = "RSA тест с длинной строкой" * 10
        encrypted = encrypt(text, self.public_key)
        decrypted = decrypt(encrypted, self.private_key)
        self.assertEqual(text, decrypted)

if __name__ == "__main__":
    unittest.main()

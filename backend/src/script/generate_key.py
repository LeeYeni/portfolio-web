from cryptography.fernet import Fernet

# 키 생성
key = Fernet.generate_key()
print(key.decode())
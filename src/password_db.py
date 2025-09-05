import sqlite3

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


class PasswordDb:
    ITERATIONS = 6_0000  # PBKDF2迭代次数
    MASTER_KEY_LENGTH = 32  # 主密钥长度
    DB_KEY_LENGTH = 32  # 数据库密钥长度
    SALT_LENGTH = 16  # 盐值长度
    DB_IV_LENGTH = 12  # 数据库密钥加密IV长度

    def __init__(self, path: str):
        # 链接数据库并获取游标
        self.db_connection = sqlite3.connect(path)
        self.cursor = self.db_connection.cursor()

    def init_new_db(self, master_password: str):
        # 生成随机盐值
        salt = get_random_bytes(PasswordDb.SALT_LENGTH)
        # 从主密码和盐值派生主密钥
        master_key = PBKDF2(
            master_password,
            salt,
            dkLen=PasswordDb.MASTER_KEY_LENGTH,
            count=PasswordDb.ITERATIONS,
            hmac_hash_module=SHA256,
        )
        # 生成随机数据库密钥
        db_key = get_random_bytes(PasswordDb.DB_KEY_LENGTH)

        # 使用主密钥加密数据库密钥，使用AES-GCM模式
        db_key_iv = get_random_bytes(PasswordDb.DB_IV_LENGTH)
        cipher = AES.new(master_key, AES.MODE_GCM, nonce=db_key_iv)
        encrypted_db_key, db_key_tag = cipher.encrypt_and_digest(db_key)

        # 创建元数据表
        self.cursor.execute(
            """
            CREATE TABLE meta(
                id               INTEGER PRIMARY KEY CHECK (id = 1),
                salt             BLOB    NOT NULL,
                db_key_iv        BLOB    NOT NULL,
                db_key_tag       BLOB    NOT NULL,
                encrypted_db_key BLOB    NOT NULL,
                kdf_iterations   INTEGER NOT NULL
            )"""
        )

        # 写入元数据
        self.cursor.execute(
            """
            INSERT INTO meta
            (id, salt, db_key_iv, db_key_tag, encrypted_db_key, kdf_iterations)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (1, salt, db_key_iv, db_key_tag, encrypted_db_key, PasswordDb.ITERATIONS),
        )

        # 创建密码数据表
        self.cursor.execute(
            """
            CREATE TABLE passwords(
                id                INTEGER PRIMARY KEY AUTOINCREMENT,
                encrypted_rec_key BLOB NOT NULL,
                rec_key_iv        BLOB NOT NULL,
                rec_key_tag       BLOB NOT NULL,
                json_iv           BLOB NOT NULL,
                json_tag          BLOB NOT NULL,
                encrypted_json    BLOB NOT NULL
            )"""
        )

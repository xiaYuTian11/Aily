import base64
import hashlib
from urllib.parse import quote, unquote


class CryptoService:
    @staticmethod
    def base64_encode(content: str) -> str:
        return base64.b64encode(content.encode('utf-8')).decode('utf-8')

    @staticmethod
    def base64_decode(content: str) -> str:
        return base64.b64decode(content.encode('utf-8')).decode('utf-8')

    @staticmethod
    def md5(content: str) -> str:
        return hashlib.md5(content.encode('utf-8')).hexdigest()

    @staticmethod
    def sha(content: str, algorithm: str = "sha256") -> str:
        algorithms = {
            "sha1": hashlib.sha1,
            "sha256": hashlib.sha256,
            "sha512": hashlib.sha512,
        }
        if algorithm not in algorithms:
            raise ValueError(f"不支持的算法: {algorithm}")
        return algorithms[algorithm](content.encode('utf-8')).hexdigest()

    @staticmethod
    def url_encode(content: str) -> str:
        return quote(content, safe='')

    @staticmethod
    def url_decode(content: str) -> str:
        return unquote(content)
import json
from typing import Tuple, Optional


class JsonService:
    @staticmethod
    def format(content: str, indent: int = 2) -> str:
        data = json.loads(content)
        return json.dumps(data, indent=indent, ensure_ascii=False)

    @staticmethod
    def compress(content: str) -> str:
        data = json.loads(content)
        return json.dumps(data, separators=(',', ':'), ensure_ascii=False)

    @staticmethod
    def validate(content: str) -> Tuple[bool, Optional[str]]:
        try:
            json.loads(content)
            return True, None
        except json.JSONDecodeError as e:
            return False, str(e)
from datetime import datetime
from typing import Optional, Dict


class EncodingService:
    @staticmethod
    def base_convert(value: str, from_base: int, to_base: int) -> str:
        decimal = int(value, from_base)
        if to_base == 10:
            return str(decimal)
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        result = ""
        while decimal:
            result = digits[decimal % to_base] + result
            decimal //= to_base
        return result or "0"

    @staticmethod
    def timestamp_convert(
        timestamp: Optional[int], datetime_str: Optional[str], fmt: str
    ) -> Dict:
        if timestamp:
            dt = datetime.fromtimestamp(timestamp)
            return {"datetime": dt.strftime(fmt), "timestamp": timestamp}
        elif datetime_str:
            dt = datetime.strptime(datetime_str, fmt)
            return {"datetime": datetime_str, "timestamp": int(dt.timestamp())}
        else:
            now = datetime.now()
            return {"datetime": now.strftime(fmt), "timestamp": int(now.timestamp())}

    @staticmethod
    def unicode_convert(content: str, direction: str) -> str:
        if direction == "to_unicode":
            return content.encode("unicode_escape").decode("ascii")
        else:
            return content.encode("ascii").decode("unicode_escape")
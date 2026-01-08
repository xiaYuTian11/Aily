import re
import difflib
from typing import List, Dict


class TextService:
    @staticmethod
    def diff(text1: str, text2: str) -> str:
        d = difflib.unified_diff(text1.splitlines(), text2.splitlines(), lineterm='')
        return '\n'.join(d)

    @staticmethod
    def regex_test(pattern: str, text: str, flags: str) -> List[str]:
        flag = 0
        if 'i' in flags:
            flag |= re.IGNORECASE
        if 'm' in flags:
            flag |= re.MULTILINE
        if 's' in flags:
            flag |= re.DOTALL
        return re.findall(pattern, text, flag)

    @staticmethod
    def stats(content: str) -> Dict:
        return {
            "chars": len(content),
            "chars_no_space": len(content.replace(' ', '')),
            "words": len(content.split()),
            "lines": len(content.splitlines()) or 1
        }
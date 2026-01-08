import httpx

async def _google_translate(text: str, source: str, target: str) -> str:
    """Google翻译"""
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": source, "tl": target, "dt": "t", "q": text}
    async with httpx.AsyncClient(timeout=10) as client:
        res = await client.get(url, params=params)
        data = res.json()
        return "".join([item[0] for item in data[0] if item[0]])

async def _mymemory_translate(text: str, source: str, target: str) -> str:
    """MyMemory翻译 - 免费1000字/天"""
    lang_map = {"zh": "zh-CN", "en": "en-GB"}
    url = "https://api.mymemory.translated.net/get"
    params = {"q": text, "langpair": f"{lang_map.get(source, source)}|{lang_map.get(target, target)}"}
    async with httpx.AsyncClient(timeout=10) as client:
        res = await client.get(url, params=params)
        data = res.json()
        return data["responseData"]["translatedText"]

async def translate(text: str, source: str = "auto", target: str = "en") -> str:
    """翻译，Google优先，MyMemory备用"""
    providers = [_google_translate, _mymemory_translate]
    for provider in providers:
        try:
            return await provider(text, source, target)
        except:
            continue
    raise Exception("所有翻译服务均不可用")
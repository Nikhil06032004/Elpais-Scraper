from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="auto", target="en")

def translate_to_english(text: str) -> str:
    if not text:
        return text
    try:
        return translator.translate(text)
    except Exception as e:
        print(f"[Translation Error] {e}")
        return text

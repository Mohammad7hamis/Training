def process_text(text):
    # دالة لتنظيف النص
    def clean_text():
        return " ".join(text.strip().lower().split())

    # دالة لحساب عدد الكلمات
    def count_words(cleaned):
        return len(cleaned.split())

    cleaned = clean_text()
    word_count = count_words(cleaned)

    print(f"Cleaned text: {cleaned}")
    print(f"Word count: {word_count}")

process_text("   Hello   WORLD   from   Python   ")

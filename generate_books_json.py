import os
import json

BOOKS_DIR = "books"
OUTPUT = "books.json"

books_list = []

for category in os.listdir(BOOKS_DIR):
    category_path = os.path.join(BOOKS_DIR, category)

    if not os.path.isdir(category_path):
        continue

    for book_folder in os.listdir(category_path):
        book_path = os.path.join(category_path, book_folder)

        if not os.path.isdir(book_path):
            continue

        json_path = os.path.join(book_path, "book.json")

        if not os.path.exists(json_path):
            print(f"[IGNORADO] sem book.json: {book_folder}")
            continue

        try:
            with open(json_path, encoding="utf-8") as f:
                data = json.load(f)

            books_list.append({
                "title": data.get("title", book_folder),
                "category": category,
                "folder": book_folder
            })

            print(f"[OK] {category}/{book_folder}")

        except Exception as e:
            print(f"[ERRO] {book_folder}: {e}")

# salva
with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(books_list, f, indent=2, ensure_ascii=False)

print("\n✅ books.json gerado com sucesso!")
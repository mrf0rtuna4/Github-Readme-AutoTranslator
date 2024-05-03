import os
from deep_translator import GoogleTranslator
import re

print("Current working directory:", os.getcwd())


def read_readme():
    print("Прочитал файлик ого")
    with open("README.md", "r", encoding="utf-8") as file:
        return file.read()


def update_localizations():
    print("Starting update_localizations...")
    readme_content = read_readme()
    selected_langs = os.getenv("LANGS")
    print("Selected langs:", selected_langs)

    no_links_content = re.sub(r"\[([^]]+)]\(([^)]+)\)", r"\1", readme_content)

    languages = [lang.strip() for lang in selected_langs.split(",")]
    files = []

    if not os.path.exists("dist"):
        os.makedirs("dist")

    for lang in languages:
        try:
            translated_content = GoogleTranslator(
                source='auto', target=lang).translate(text=no_links_content)

            with open(f"dist/{lang}.md", "w", encoding="utf-8") as file:
                file.write(translated_content)
            print(f"Localization for {lang} updated.")
            files.append(f"dist/{lang}.md")
        except Exception as e:
            print(f"Failed to translate to {lang}: {str(e)}")

    print("update_localizations finished.")
    return files


update_localizations()

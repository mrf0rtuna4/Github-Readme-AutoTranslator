Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
<div align="center">
  <img src="https://img.shields.io/github/v/release/mrf0rtuna4/Git-Markdown-AutoTranslator">
  <img src="https://img.shields.io/github/actions/workflow/status/mrf0rtuna4/Git-Markdown-AutoTranslator/development.yml">
</div>


> [!WARNING]
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`.github/workflows/translate.yml`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

```yml
name: Generate Localized File  # The name of your action

on:
  workflow_dispatch:  # Manual start (if needs)
  push:  # Run when committing to a branch
    branches: [ main ] # Set the name of your branch if required
    paths: [ 'README.md' ] # Start translating only if file changed in current push
    
jobs:
  translate:  # Task name
    runs-on: ubuntu-latest  # Running on an Ubuntu image
    steps:
      - name: Checkout code  # Step: code check
        uses: actions/checkout@v2  # Using an action to test the code

      - name: Run translation  # Step: start the translation
        uses: mrf0rtuna4/Git-Markdown-AutoTranslator@v2.3.1  # Using an action to translate
        with:
          FILES: 'README.md' # The *.md files to be translate
          LANGS: 'english,italian,dutch,spanish' # List of languages to be translated

      - name: Push to GitHub  # Step: Submit changes to GitHub
        uses: crazy-max/ghaction-github-pages@v3.1.0  # Using an action to publish to GitHub Pages
        with:
          target_branch: translations  # The branch to which the changes will be sent
          build_dir: 'dist'  # The directory with the collected files
        env:
          GITHUB_TOKEN: ${{ secrets.GTK }}  # Transferring a GitHub access token
```

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`LANGS`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know../docs/languages.md)


Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

- `FILES`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`LANGS`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`DEBUG`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`True`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
- `MAX_LINELENGTH_`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`MAX_THREADS`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
- `PROVIDER` / `provider`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`deep-translator`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`GoogleTranslator`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`GoogleTranslator`, `PonsTranslator`, `LingueeTranslator`, `MyMemoryTranslator`, `YandexTranslator`, `MicrosoftTranslator`, `QcriTranslator`, `DeeplTranslator`, `LibreTranslator`, `PapagoTranslator`, `ChatGptTranslator`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`BaiduTranslator`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`google`, `deepl`, `libre`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`chatgpt`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
- `SOURCE_LANGUAGE` / `source_language`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`auto`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`en`.
- `PROVIDER_OPTIONS` / `provider_options`: oggetto JSON facoltativo con argomenti del costruttore specifici del provider. Ciò è utile per le esecuzioni locali, ma le azioni GitHub in genere dovrebbero invece passare i segreti attraverso le variabili di ambiente.
- `VALIDATE_PROVIDER` / `validate_provider`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`true`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

| Provider | Environment variables |
| --- | --- |
| `YandexTranslator` | `YANDEX_API_KEY` |
| `MicrosoftTranslator` | `MICROSOFT_API_KEY`, `MICROSOFT_REGION` |
| `QcriTranslator` | `QCRI_API_KEY` |
| `DeeplTranslator` | `DEEPL_API_KEY`, `DEEPL_USE_FREE_API` |
| `LibreTranslator` | `LIBRE_API_KEY`, `LIBRE_USE_FREE_API`, `LIBRE_CUSTOM_URL` |
| `PapagoTranslator` | `PAPAGO_CLIENT_ID`, `PAPAGO_SECRET_KEY` |
| `ChatGptTranslator` | `OPENAI_API_KEY`, `OPENAI_MODEL` |
| `BaiduTranslator` | `BAIDU_APP_ID`, `BAIDU_APP_KEY` |

> [!WARNING] 
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.`MAX_LINELENGTH_`Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.


Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

```yml
      - name: Run translation
        with:
          FILES: 'README.md' 
          LANGS: 'italian,english'
          provider: 'GoogleTranslator'
          source_language: 'auto'
```

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

```yml
      - name: Run translation with DeepL
        uses: mrf0rtuna4/Git-Markdown-AutoTranslator@v2.3.1
        with:
          FILES: 'README.md'
          LANGS: 'de,fr'
          provider: 'DeeplTranslator'
          source_language: 'en'
          validate_provider: 'true'
        env:
          DEEPL_API_KEY: ${{ secrets.DEEPL_API_KEY }}
          DEEPL_USE_FREE_API: 'true'
```

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
<div align="center">
  <a href="https://github.com/mrf0rtuna4/Git-Markdown-AutoTranslator/blob/translations_indev/ru_README.md">
      <img src="https://img.shields.io/badge/Язык-Русский-blue" alt="Русский" />
  </a>
  <a href="https://github.com/mrf0rtuna4/Git-Markdown-AutoTranslator/blob/translations_indev/ja_README.md">
      <img src="https://img.shields.io/badge/言語-日本語-blue" alt="日本語" />
  </a>
  <a href="https://github.com/mrf0rtuna4/Git-Markdown-AutoTranslator/blob/translations_indev/it_README.md">
      <img src="https://img.shields.io/badge/Lingua-Italiano-blue" alt="Italiano" />
  </a>
  <a href="https://github.com/mrf0rtuna4/Git-Markdown-AutoTranslator/blob/translations_indev/uk_README.md">
      <img src="https://img.shields.io/badge/Мова-Українська-blue" alt="Українська" />
  </a>
  <a href="https://github.com/mrf0rtuna4/Git-Markdown-AutoTranslator/blob/translations_indev/ar_README.md">
      <img src="https://img.shields.io/badge/لغة-العربية-blue" alt="العربية" />
  </a>
</div>

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.LICENSEError 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
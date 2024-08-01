# GitHub Leesmij-autovertaler
<div align="center">
  <img src="https://img.shields.io/github/v/release/mrf0rtuna4/Github-Readme-AutoTranslator">
  <img src="https://img.shields.io/github/actions/workflow/status/mrf0rtuna4/Github-Readme-AutoTranslator/example.yml">
</div>


> [!WAARSCHUWING]
> Wij gebruiken alleen VERTALING DeepL
>
> Dit kan de kwaliteit van de vertaling beïnvloeden. Het kan er ook voor zorgen dat het systeem uw bestandsgegevens verkeerd identificeert.

Deze GitHub-actie genereert en pusht automatisch gelokaliseerde versies van uw README.md-bestand op basis van de ondersteunde talen.

## Gebruik

Om deze actie te gebruiken, maakt u een workflowbestand (bijvoorbeeld `.github/workflows/translate.yml`) in uw repository met de volgende inhoud:

```yml
name: Generate Localized Readme  # The name of your action

on:
  workflow_dispatch:  # Manual start
  push:  # Run when committing to a branch
    branches:
    - master # Set the name of your branch if required
    paths: # Start translating only if readme file changed in current push
    - 'README.MD'
    - 'README.md'
    - 'readme.md'
    - 'Readme.md'

jobs:
  translate:  # Task name
    runs-on: ubuntu-latest  # Running on an Ubuntu image
    steps:
      - name: Checkout code  # Step: code check
        uses: actions/checkout@v2  # Using an action to test the code

      - name: Run translation  # Step: start the translation
        uses: mrf0rtuna4/Github-Readme-AutoTranslator@v1.3.0  # Using an action to translate
        env:
          LANGS: 'english,italian,dutch,spanish' # List of languages to be translated

      - name: Push to GitHub  # Step: Submit changes to GitHub
        uses: crazy-max/ghaction-github-pages@v3.1.0  # Using an action to publish to GitHub Pages
        with:
          target_branch: translations  # The branch to which the changes will be sent
          build_dir: 'dist'  # The directory with the collected files
        env:
          GITHUB_TOKEN: ${{ secrets.GTK }}  # Transferring a GitHub access token
```

Vervang `LANGS` door een door komma's gescheiden lijst met talen die u wilt genereren.
<details>
<summary>Beschikbare talen voor vertaling (volledige referenties)</summary>

```yaml
    'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'assamese', 'aymara', 'azerbaijani', 'bambara', 'basque', 
    'belarusian', 'bengali', 'bhojpuri', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 
    'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dhivehi', 'dogri', 'dutch', 'english', 'esperanto', 
    'estonian', 'ewe', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'guarani', 
    'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'ilocano', 
    'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'kinyarwanda', 'konkani', 'korean', 
    'krio', 'kurdish (kurmanji)', 'kurdish (sorani)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lingala', 'lithuanian', 'luganda', 
    'luxembourgish', 'macedonian', 'maithili', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'meiteilon (manipuri)',
    'mizo', 'mongolian', 'myanmar', 'nepali', 'norwegian', 'odia (oriya)', 'oromo', 'pashto', 'persian', 'polish', 'portuguese', 
    'punjabi', 'quechua', 'romanian', 'russian', 'samoan', 'sanskrit', 'scots gaelic', 'sepedi', 'serbian', 'sesotho', 'shona', 
    'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'tatar',
    'telugu', 'thai', 'tigrinya', 'tsonga', 'turkish', 'turkmen', 'twi', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 
    'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'
```
</details>

<details>
<summary>Beschikbare talen voor vertaling (korte adressen)</summary>

```yaml
'af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 'ny',
'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'dv', 'doi', 'nl', 'en', 'eo', 'et', 'ee', 'tl', 'fi', 'fr', 'fy', 'gl',
'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja',
'jw', 'kn', 'kk', 'km', 'rw', 'gom', 'ko', 'kri', 'ku', 'ckb', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lg', 'lb', 'mk',
'mai', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mni-Mtei', 'lus', 'mn', 'my', 'ne', 'no', 'or', 'om', 'ps', 'fa', 'pl',
'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'nso', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su',
'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
```

</details>


## Configuratie

U kunt deze actie configureren met behulp van de volgende invoer:

- `langs`: een door komma's gescheiden lijst met talen die moeten worden gegenereerd.

## Voorbeeld

Als u bijvoorbeeld README-bestanden voor de Servische, Italiaanse en Engelse taal wilt genereren, ziet uw configuratie er als volgt uit:

```yml
      - name: Run translation
        env:
          LANGS: 'serbian,italian,english'
```

En u kunt zien hoe u actie kunt ondernemen door op deze widgets te klikken:
<div align="center">
  <a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations_indev/ru.md">
      <img src="https://img.shields.io/badge/Язык-Руский-blue" alt="Руский" />
  </a>
  <a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations_indev/ja.md">
      <img src="https://img.shields.io/badge/言語-日本語-blue" alt="日本語" />
  </a>
  <a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations_indev/it.md">
      <img src="https://img.shields.io/badge/Lingua-Italiano-blue" alt="Italiano" /> </a>
<a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations_indev/uk.md">
<img src="https://img.shields.io/badge/Мова-Українська-blue" alt="Українська" />
</a>
<a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations_indev/ar.md">
<img src="https://img.shields.io/badge/لغة-العربية-blue" alt="العربية" />
</a>
</div>

## Licentie

Dit project is gelicentieerd onder de MIT-licentie - zie het bestand [LICENSE](LICENSE) voor meer informatie.
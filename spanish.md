# GitHub Readme AutoTranslator
<div align="center">
<img src="https://img.shields.io/github/v/release/mrf0rtuna4/Github-Readme-AutoTranslator">
<img src="https://img.shields.io/github/actions/workflow/status/mrf0rtuna4/Github-Readme-AutoTranslator/example.yml">
</div>

> [!WARNING]
> Solo utilizamos TRANSLATION DeepL
>
> Esto puede afectar la calidad de la traducción. También puede hacer que el sistema identifique incorrectamente los datos de su archivo.

Esta acción de GitHub genera y envía automáticamente versiones localizadas de su archivo README.md según los idiomas admitidos.

## Uso

Para usar esta acción, cree un archivo de flujo de trabajo (por ejemplo, `.github/workflows/translate.yml`) en su repositorio con el siguiente contenido:

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

Reemplace `LANGS` con una lista separada por comas de los idiomas que desea generar.
<details>
<summary>Idiomas disponibles para traducción (completar) referencias)</summary>

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
<summary>Idiomas disponibles para traducción (breve direcciones)</summary>

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

## Configuración

Puede configurar esta acción utilizando las siguientes entradas:

- `langs`: una lista separada por comas de los idiomas que se generarán.

## Ejemplo

Por ejemplo, si desea generar archivos README para los idiomas serbio, italiano e inglés, su configuración se vería así:

```yml
      - name: Run translation
        env:
          LANGS: 'serbian,italian,english'
```

Puede ver cómo funciona la acción haciendo clic en estos widgets:
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

## Licencia

Este proyecto tiene licencia MIT. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.
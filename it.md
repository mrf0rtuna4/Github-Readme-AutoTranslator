<a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations/russian.md">
    <img src="https://img.shields.io/badge/Язык-Русский-blue" alt="Русский" />
  </a>
  <a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations/italian.md">
    <img src="https://img.shields.io/badge/Lingua-Italiana-blue" alt="Italiana" />
  </a>

# Traduttore automatico Leggimi GitHub

Questa azione GitHub genera e invia automaticamente versioni localizzate del file README.md in base alle lingue supportate.

## Utilizzo

Per utilizzare questa azione, crea un file di flusso di lavoro (ad esempio, `.github/workflows/translate.yml`) nel tuo repository con il seguente contenuto:

```yml
name: Generate Localized Readme  # The name of your action

on:
  schedule:  # Scheduled start
    - cron: "0 */24 * * *"  # Every 24 hours

  workflow_dispatch:  # Manual start
  push:  # Run when committing to a branch
    branches:
    - master # Set the name of your branch if required

jobs:
  translate:  # Task name
    runs-on: ubuntu-latest  # Running on an Ubuntu image
    steps:
      - name: Checkout code  # Step: code check
        uses: actions/checkout@v2  # Using an action to test the code

      - name: Run translation  # Step: start the translation
        uses: mrf0rtuna4/Github-Readme-AutoTranslator@v1.2.0  # Using an action to translate

          # List of languages to be translated
          LANGS: 'serbian,italian,english'

      - name: Push to GitHub  # Step: Submit changes to GitHub
        uses: crazy-max/ghaction-github-pages@v3.1.0  # Using an action to publish to GitHub Pages
        with:
          target_branch: translations  # The branch to which the changes will be sent
          build_dir: 'dist'  # The directory with the collected files
        env:
          GITHUB_TOKEN: ${{ secrets.GTK }}  # Transferring a GitHub access token
```

Sostituisci "LANGS" con un elenco di lingue separate da virgole che desideri generare.
Lingue disponibili per la traduzione:
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

## Configurazione

È possibile configurare questa azione utilizzando i seguenti input:

- `langs`: un elenco di lingue separate da virgole da generare.
- `github_token`: token GitHub per l'autenticazione.

## Esempio

Ad esempio, se desideri generare file README per le lingue serba, italiana e inglese, la tua configurazione sarebbe simile a questa:

```yml
      - name: Run translation
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          LANGS: 'serbian,italian,english'
```

## Licenza

Questo progetto è concesso in licenza con la licenza MIT. Per i dettagli, consulta il file [LICENSE](LICENSE).
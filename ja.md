<a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations/russian.md">
<img src="https://img.shields.io/badge/Язык-Русский-blue" alt="Русский" />
</a>
<a href="https://github.com/mrf0rtuna4/Github-Readme-AutoTranslator/blob/translations/italian.md">
<img src="https://img.shields.io/badge/Lingua-Italiana-blue" alt="Italiana" />

# GitHub Readme AutoTranslator

この GitHub アクションは、サポートされている言語に基づいて、README.md ファイルのローカライズされたバージョンを自動的に生成してプッシュします。

## 使用方法

このアクションを使用するには、次の内容を含むワークフロー ファイル (例: `.github/workflows/translate.yml`) をリポジトリに作成します。

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

`LANGS` を、生成する言語のカンマ区切りリストに置き換えます。

翻訳に使用できる言語:

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

## 構成

次の入力を使用して、このアクションを構成できます。

- `langs`: 生成する言語のカンマ区切りリスト。

- `github_token`: 認証用の GitHub トークン。

## 例

たとえば、セルビア語、イタリア語、英語の README ファイルを生成する場合、構成は次のようになります:

```yml
      - name: Run translation
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          LANGS: 'serbian,italian,english'
```

## ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。
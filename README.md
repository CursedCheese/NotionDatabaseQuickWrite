# NotionDatabaseQuickWrite
Add data to Notion's database at high speed using Wox (Especially for Windows user. because Alfred is not available).

This code is almost just a combination of the contents of the two sites below. I would like to thank the two sites for providing us with the original information.

+ https://www.hanatare-papa.jp/entry/technology-notion-1_4
+ https://00m.in/BqXQp

This code uses Wox to add data to the database at high speed. To use, place this repository in `AppData/Local/Wox/Plugins/`. Set your Python UUID in `plugins.py`.
In `notion_database_writer.py`, set the `NOTION_API_KEY` portion to your Notion integration token and set the `DATABASE_ID` to the ID obtained from your database link.
In Wox, you can enter text using the `ActionKeyword` command in `plugins.py`.

If it does not work, please refer to the status code so that it can be displayed.

Wox: https://github.com/Wox-launcher/Wox/releases \
Notion API: https://developers.notion.com/ \
Status codes: https://developers.notion.com/reference/status-codes

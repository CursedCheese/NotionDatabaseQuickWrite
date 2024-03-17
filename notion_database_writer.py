import requests
from wox import Wox

class Main(Wox):

    def query(self, user_input):
        return [{
            'Title': 'input: ' + user_input + ')',
            'SubTitle': '入力内容',
            'IcoPath': 'img\\Notion_icon.png',
            'JsonRPCAction': {
                'method': 'action',
                'parameters': [user_input],
                'dontHideAfterAction': False
            }
        }]
    
    def action(self, user_input):
        NOTION_API_KEY = 'secret_?????????????'
        DATABASE_ID = '????????????????????????????'  # Database ID(you can get it from the URL of the database page.)

        url = 'https://api.notion.com/v1/pages'

        headers =  {
            'Notion-Version': '2022-06-28',
            'Authorization': 'Bearer ' + NOTION_API_KEY,
            'Content-Type': 'application/json',
        }

        # The format of the json should match the part of the database to be filled.
        json_data = {
            'parent': { 'database_id': DATABASE_ID },
            'properties': {
                '名前': {
                    'title': [
                        {
                            'text': {
                                'content': user_input
                            }
                        }
                    ]
                },
            },
        }

        response = requests.post(url, headers=headers, json=json_data)
        # If it does not work, remove the comment out and check the cause of the error.
        if response.status_code == 200:
            pass
            # print('Success!')
        else:
            error_details = response.json()
            error_code = error_details.get('code')
            error_message = error_details.get('message')
            # print(f'Error: {error_code} - {error_message}')

if __name__ == '__main__':
    Main()

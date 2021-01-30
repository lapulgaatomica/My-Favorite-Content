import unittest
from flask import current_app, url_for
from app import create_app, database
from app.models import DailymailColumn
from datetime import datetime

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        database.create_all()
        self.client = self.app.test_client(use_cookies=True)
        self.column = DailymailColumn(link='https://www.test.com',
            title='test title',
            columnist='test columnist')
        database.session.add(self.column)
        database.session.commit()

    def tearDown(self):
        database.session.remove()
        database.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_column_content(self):
        self.assertEqual(f'{self.column.link}', 'https://www.test.com')
        self.assertEqual(f'{self.column.title}', 'test title')
        self.assertEqual(f'{self.column.columnist}', 'test columnist')
        self.assertTrue(isinstance(self.column.date_added, datetime))

    def test_columns_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('test title' in response.get_data(as_text=True))

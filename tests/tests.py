import unittest
from flask import current_app
from app import create_app, database


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        database.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        database.session.remove()
        database.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
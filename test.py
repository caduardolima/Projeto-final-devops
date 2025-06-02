import unittest
from app import app

class DifferentTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_post_not_allowed_on_items(self):
        response = self.client.post('/items')
        self.assertEqual(response.status_code, 405)

    def test_protected_route_unauthorized(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)
        self.assertIn("msg", response.json)

    def test_swagger_ui_access(self):
        response = self.client.get('/swagger/')
        self.assertIn(response.status_code, [200, 301, 302])

if __name__ == '__main__':
    unittest.main()

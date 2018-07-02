from django.test import TestCase


class MyTestCase(TestCase):
    def test_home(self):
        resp = self.client.get('/')
        data = resp.json()
        self.assertEqual(data['status'], 'OK')
        self.assertGreaterEqual(data['value'], 1)
        self.assertLessEqual(data['value'], 10)

    def test_hello(self):
        resp = self.client.get('/hello/')
        self.assertContains(resp, "Hello Joe!")

    # def test_always_ok(self):
    #     self.assertAlmostEqual(0.1 + 0.2, 0.3)
    #     pass
    #
    # def test_always_not_ok1(self):
    #     1 / 0
    #
    # def test_always_not_ok2(self):
    #     x = 21398766 * 362452
    #     self.assertEqual(128376666, x)
    #     # assert x == 128376666

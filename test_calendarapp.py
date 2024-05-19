import unittest
from calendarapp import CalendarApp
class TestCalendarApp(unittest.TestCase):
    def test_init(self):
        app = CalendarApp()
        self.assertTrue(app)
    def test_select_day(self):
        app = CalendarApp()
        app.select_day(19)
        self.assertEqual(app.get_selected_day(19), 19)
if __name__ == '__main__':
    unittest.main()



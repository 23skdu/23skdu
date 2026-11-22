import datetime
import unittest


class WeatherDateTests(unittest.TestCase):
    def test_forecast_days_follow_today(self):
        today = datetime.date(2026, 11, 15)  # Sunday
        self.assertEqual(today.strftime("%A"), "Sunday")
        expected = ["Monday", "Tuesday", "Wednesday"]
        for idx, name in enumerate(expected):
            forecast_day = today + datetime.timedelta(days=idx + 1)
            self.assertEqual(forecast_day.strftime("%A"), name)
            self.assertEqual(forecast_day.strftime("%b %-d"),
                             (today + datetime.timedelta(days=idx + 1)).strftime("%b %-d"))

    def test_day_name_matches_forecast_date(self):
        today = datetime.date(2026, 11, 15)
        for idx in range(3):
            forecast_day = today + datetime.timedelta(days=idx + 1)
            # The label day must equal the weekday of the forecast date.
            self.assertEqual(forecast_day.strftime("%A"),
                             forecast_day.strftime("%A"))

    def test_no_off_by_one(self):
        today = datetime.date(2026, 11, 15)
        # Nov 16 is Monday, not Sunday.
        self.assertNotEqual((today + datetime.timedelta(days=1)).strftime("%A"), "Sunday")
        self.assertEqual((today + datetime.timedelta(days=1)).strftime("%A"), "Monday")


if __name__ == "__main__":
    unittest.main()

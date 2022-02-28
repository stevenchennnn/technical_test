# -*- coding: utf-8 -*-

import requests

from datetime import timedelta, datetime
from constants import common_constants
from logger.logger import logger

"""
Task 2 Start

1. Capture the related API endpoint  (Checked)
2. Send a request using this API endpoint with your preferred language (Checked)
3. Test the request response status is whether successful or not (Checked)
4. Extract the relative humidity (e,g, 60 - 85%) for the day after tomorrow from the API response 
   (e.g. if today is Monday, then extract the relative humidity for Wednesday) (Checked)

"""


class TestTask2:

    def test_check_response(self):

        # Send requests
        response = requests.get(common_constants.ApiTestData.ApiUrl)
        logger.info("Response Status = %s", response.status_code)
        # Make sure api is not a bad request
        assert response.status_code != 400

        # Check response status 
        assert response.status_code == 200

        # Save response as json format
        datas = response.json()
        logger.info("Response Body =%s", datas)

        # Get the day after tomorrow date
        current_date = datetime.now()
        the_day_after_tmr = current_date + timedelta(days=2)

        # Change String to specific format
        format_the_day_after_tmr = the_day_after_tmr.strftime("%Y%m%d")

        # Parse result
        for data in datas['weatherForecast']:
            if data['forecastDate'] == format_the_day_after_tmr:
                logger.info("The day after tmr forecastMinrh = %s, forecastMaxrh = %s", data['forecastMinrh']['value'],
                            data['forecastMaxrh']['value'])
                assert data['forecastMinrh']['value']
                assert data['forecastMaxrh']['value']

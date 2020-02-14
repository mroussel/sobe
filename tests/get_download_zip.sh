#!/bin/bash

curl -X GET \
-H "Content-Type: application/x-www-form-urlencoded" \
--output /tmp/out.png \
"http://localhost:5000/get_download_zip?file_url=https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
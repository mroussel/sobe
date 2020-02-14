#!/bin/bash

curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "file_url=https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" \
http://localhost:5000/request_download 


curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "file_url=https://download.sysinternals.com/files/Handle.zip" \
http://localhost:5000/request_download 


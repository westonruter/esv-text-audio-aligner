#!/bin/bash

echo "Open http://127.0.0.1:8000/read-along/ in your browser"

cd data
python -m SimpleHTTPServer 8000


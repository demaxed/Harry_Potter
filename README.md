pip install -r requiremets.txt

activate envirement

To run server use runs scripts

Start commands:
#!/bin/sh
Linux и Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
chmod +x run_linux.sh
./run_linux.sh

Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
run_windows.bat
# Flask load balancing with redis for session management on Ubuntu Server
## Steps:
1. Setup redis server.
2. Run flask app app.py from server1 and server2 folder with port 5001 and 5002 respectively.
3. Install nginx and place "load_balancing" file inside /etc/nginx/sites-enabled/ and start the nginx server
4. Check the apis serving http://127.0.0.1:5000
5. /set and /get the uniform session accross the servers and servers are load balanced in round-robin fashion.

* Installations
  ```sh
  sudo apt install nginx
  pip3 install flask flask_session redis
  ```
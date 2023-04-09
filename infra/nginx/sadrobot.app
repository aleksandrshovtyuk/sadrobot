server {
       listen 80;
       listen [::]:80;

       server_name sadrobot.app 195.140.146.18;

       root /var/www/sadrobot.app;
       index index.html;

       location / {
               try_files $uri $uri/ =404;
       }
}

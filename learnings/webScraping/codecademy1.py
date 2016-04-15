# Log in to the server.  This can be done only once.                   
wget --save-cookies cookies.txt \
     --post-data 'user_login=konatalaramesh@gmail.com&password=' \
     http://server.com/auth.php

# Now grab the page or pages we care about.
wget --load-cookies cookies.txt \
     -p http://server.com/interesting/article.php
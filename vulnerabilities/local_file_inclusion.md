# Local File Inclusion

Originally I thought that local file inclusion was just tricking web servers into exposing files. This vulnerability is more than just that. It also includes running files on the web server.

In some capture the flag events, these show up in web applications for a pages that show the contents of files. These pages often have a url similar to `http://target.thm/some/page?path=/var/www/html/secret.txt`.

The problem is that users can alter the path parameter and often times the server side code doesn't validate it. Nothing is stopping the user from typing `http://target.thm/some/page?path=/etc/passwd` and seeing what users are on the server.

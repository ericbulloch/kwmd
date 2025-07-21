# Local File Inclusion (LFI)

Originally I thought that local file inclusion was just tricking web servers into exposing files. This vulnerability is more than just that. It also includes running files on the web server.

In some capture the flag events, these show up in web applications for a pages that show the contents of files. These pages often have a url similar to `http://target.thm/some/page?path=/var/www/html/secret.txt`.

The problem is that users can alter the path parameter and often times the server side code doesn't validate it. Nothing is stopping the user from typing `http://target.thm/some/page?path=/etc/passwd` and seeing what users are on the server.

I can attach a fuzzer to this page and try to find any and all well-know sensitive files on a server. The ability to read files on a server greatly increases the attack surface because now I can examine code and find vulnerabilties in those files as well.

## Filtering

I can't stress this enough, filtering is good but it is not an optimal solution. Time after time, developers try to filter what can be input by users and bad actors keep finding ways to bypass the filtering.

I recently finished a capture the flag event that contained a LFI vulnerability. The url was something like `http://mysite.thm/test.php?path=/var/www/html/someFile.php`. The code was printing the contents of the file in the path parameter.

I saw the path and tried to get the `/etc/passwd` contents to print to the screen. I started with `http://mysite.thm/test.php?path=/etc/password` and `http://mysite.thm/test.php?path=../../../../etc/passwd`. Both urls returned an error message that the provided paths were not allowed. This let me know that the server was doing some validation and the paths I provided were failing.

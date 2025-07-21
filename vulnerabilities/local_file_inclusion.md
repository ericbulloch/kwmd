# Local File Inclusion (LFI)

Originally I thought that local file inclusion was just tricking web servers into exposing files. This vulnerability is more than just that. It also includes running files on the web server.

In some capture the flag events, these show up in web applications for a pages that show the contents of files. These pages often have a url similar to `http://target.thm/some/page?path=/var/www/html/secret.txt`.

The problem is that users can alter the path parameter and often times the server side code doesn't validate it. Nothing is stopping the user from typing `http://target.thm/some/page?path=/etc/passwd` and seeing what users are on the server.

I can attach a fuzzer to this page and try to find any and all well-know sensitive files on a server. The ability to read files on a server greatly increases the attack surface because now I can examine code and find vulnerabilties in those files as well.

## Filtering

I can't stress this enough, filtering is good but it is not an optimal solution. Time after time, developers try to filter what can be input by users and bad actors keep finding ways to bypass the filtering.

I recently finished a capture the flag event that contained a LFI vulnerability. The url was something like `http://mysite.thm/test.php?path=/var/www/html/someFile.php`. The code was printing the contents of the file in the path parameter.

I saw the path and tried to get the `/etc/passwd` contents to print to the screen. I started with `http://mysite.thm/test.php?path=/etc/password` and `http://mysite.thm/test.php?path=/var/www/html/../../../etc/passwd`. Both urls returned an error message that the provided paths were not allowed. This let me know that the server was doing some validation and the paths I provided were failing.

I decided to take another approach and view the contents of the file that I was on. I changed the url to `http://mysite.thm/test.php?path=/test.php` and saw the following contents:

```php
<!DOCTYPE HTML>
<html>
<head>
    <title>Test page</title>
    <h1>Test Page. Do not deploy</h1>
 
    </button></a> <a href="/test.php?view=/var/www/html/someFile.php"><button>Here is a button</button></a><br>
        <?php
          function containsStr($str, $substr) {
            return strpos($str, $substr) !== false;
          }
          if(isset($_GET["path"])){
            if(!containsStr($_GET['path'], '../..') && containsStr($_GET['path'], '/var/www/html')) {
              include $_GET['path'];
            } else {
              echo 'Sorry, Thats not allowed';
            }
          }
        ?>
    </div>
</body>

</html>
```

This filtering is very similar to what a lot of developers do. They believe they have restricted all requests to files in the `/var/www/html` directory. This filtering is very easy to bypass.

First, I need to make sure that `/var/www/html` is part of my path and my path can't include `../..`. The following is a valid request that will bypass the filtering and display the contents of the `/etc/passwd` file:

`http://mysite.thm/test.php?path=/var/www/html/..//..//..//etc/passwd`

Linux will change the `//` to a single `/` character. That path will bypass the filtering and gloriously show the contents of `/etc/passwd` on the page.

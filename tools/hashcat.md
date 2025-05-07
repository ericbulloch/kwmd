# hashcat

The hashcat tool is used to crack hashes. It makes use of a dictionary file to test the hashes against.

## Examples

I have listed some examples where I have used hashcat in a capture the flag event.

### JWT (JSON Web Token)

If a developer uses a weak secret for the signature of a JWT, then I can crack it using hashcat. In this example I am going to pull down a list of commong jwt secrets and have hashcat use that list against a JWT that has a weak secret.

I download the list of common JWT secrets using the following command:

`wget https://raw.githubusercontent.com/wallarm/jwt-secrets/master/jwt.secrets.list`

In this example, I am testing the following JWT:

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o`

I save that JWT in a file called jwt.txt. I then run the following command to test the JWT against the jwt.secrets.list file that was downloaded earlier. Here is the command:

`hashcat -m 16500 -a 0 jwt.txt jwt.secrets.list`

After a bit the following output shows up:

```bash
Dictionary cache hit:
* Filename..: jwt.secrets.list
* Passwords.: 103965
* Bytes.....: 1231757
* Keyspace..: 103965

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o:secret
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: JWT (JSON Web Token)
Hash.Target......: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMj...hfEd2o
Time.Started.....: Wed May  7 07:08:25 2025 (0 secs)
Time.Estimated...: Wed May  7 07:08:25 2025 (0 secs)
Guess.Base.......: File (jwt.secrets.list)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   155.6 kH/s (10.31ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 2048/103965 (1.97%)
Rejected.........: 0/2048 (0.00%)
Restore.Point....: 0/103965 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....:  -> everybody knows it
```

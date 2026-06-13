# Wordlists Reference

> All SecLists paths assume default Kali install: `/usr/share/seclists/`
> Install if missing: `sudo apt install seclists`

---

## Wordlist Subtraction

> Remove already-tried entries from a larger wordlist to avoid repeating work.

### One-liner
```bash
# Remove entries in tried.txt from big_list.txt → output to remaining.txt
grep -vxFf tried.txt big_list.txt > remaining.txt
```

### Multiple already-tried lists
```bash
# Remove entries from any number of already-tried lists using process substitution
grep -vxFf <(cat tried1.txt tried2.txt tried3.txt) big_list.txt > remaining.txt
```

### Reusable bash function
> Add to `~/.bashrc` or `~/.zshrc`, then run `source ~/.bashrc`

```bash
# Usage: wordlist_subtract <big_list> <output> <tried_list1> [tried_list2 ...]
wordlist_subtract() {
    if [ "$#" -lt 3 ]; then
        echo "Usage: wordlist_subtract <big_list> <output> <tried_list1> [tried_list2 ...]"
        return 1
    fi
    local big_list="$1"
    local output="$2"
    shift 2
    local tried=("$@")
    grep -vxFf <(cat "${tried[@]}") "$big_list" > "$output"
    local before after removed
    before=$(wc -l < "$big_list")
    after=$(wc -l < "$output")
    removed=$((before - after))
    echo "[*] Original:  $before entries"
    echo "[*] Removed:   $removed entries"
    echo "[*] Remaining: $after entries → $output"
}
```

**Example usage:**
```bash
wordlist_subtract /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt \
                  remaining.txt \
                  common.txt directory-list-2.3-small.txt
```

### Notes
- `-x` ensures whole-line exact matching; partial matches are not removed
- `-F` treats entries as fixed strings — safe for wordlists containing regex metacharacters
- Process substitution `<(cat ...)` avoids creating a temp file for the tried lists
- The output file will not be sorted; order from the big list is preserved

---

## Directory & File Enumeration

| Situation | Wordlist | Notes |
|-----------|----------|-------|
| Quick first pass | `Discovery/Web-Content/common.txt` | ~4k entries; fast |
| Standard scan | `Discovery/Web-Content/directory-list-2.3-medium.txt` | ~220k entries; default choice |
| Thorough scan | `Discovery/Web-Content/directory-list-2.3-big.txt` | ~1.2M entries; slow but thorough |
| API endpoints | `Discovery/Web-Content/api/api-endpoints.txt` | API-specific paths |
| API endpoints (large) | `Discovery/Web-Content/api/objects.txt` | Object/resource names for REST APIs |
| PHP-specific | `Discovery/Web-Content/PHP.fuzz.txt` | PHP file names and paths |
| IIS / ASP.NET | `Discovery/Web-Content/IIS.fuzz.txt` | IIS-specific paths |
| Backup & sensitive files | `Discovery/Web-Content/raft-medium-files.txt` | Files including extensions |
| Sensitive directories | `Discovery/Web-Content/raft-medium-directories.txt` | Clean dir names, no extensions |
| Config & secrets | `Discovery/Web-Content/quickhits.txt` | Common sensitive file paths; good add-on pass |
| Parameter fuzzing | `Discovery/Web-Content/burp-parameter-names.txt` | Hidden GET/POST parameter names; use with ffuf `-w` or Arjun |

**Recommended extension list for `-x` flag:**
```
php,html,htm,asp,aspx,txt,bak,old,zip,conf,config,log,xml,json,sql,env
```

---

## Subdomain Discovery

| Situation | Wordlist | Notes |
|-----------|----------|-------|
| Fast pass | `Discovery/DNS/subdomains-top1million-5000.txt` | Top 5k; very fast |
| Standard | `Discovery/DNS/subdomains-top1million-20000.txt` | Top 20k; good balance |
| Thorough | `Discovery/DNS/subdomains-top1million-110000.txt` | Top 110k; thorough |
| VHost fuzzing | `Discovery/DNS/subdomains-top1million-5000.txt` | Same list works for vhost brute |

---

## Username Lists

| Situation | Wordlist | Notes |
|-----------|----------|-------|
| General brute-force | `Usernames/top-usernames-shortlist.txt` | ~100 common usernames |
| Larger username list | `Usernames/Names/names.txt` | First names; good for AD environments |
| AD format variants | `Usernames/Names/familyNames-USA-Top1000.txt` | Combine with first names to build AD usernames |
| xato breach usernames | `Usernames/xato-net-10-million-usernames.txt` | Real-world breach usernames |
| xato (smaller) | `Usernames/xato-net-10-million-usernames-dup-removed.txt` | Deduplicated version |

**Build AD username formats from a names list:**
```bash
# Given first.txt and last.txt, generate common AD formats
while IFS= read -r first; do
    while IFS= read -r last; do
        echo "${first}.${last}"              # john.smith
        echo "${last}.${first}"              # smith.john
        echo "${first:0:1}${last}"           # jsmith
        echo "${last}${first:0:1}"           # smithj
        echo "${first:0:1}.${last}"          # j.smith
        echo "${first}"                      # john
        echo "${last}"                       # smith
    done < last.txt
done < first.txt | sort -u > ad_usernames.txt
```

---

## Password Lists

| Situation | Wordlist | Notes |
|-----------|----------|-------|
| General purpose | `Passwords/Leaked-Databases/rockyou.txt` | The standard; always try first |
| Common web passwords | `Passwords/Common-Credentials/10-million-password-list-top-10000.txt` | Top 10k most common |
| Corporate patterns | `Passwords/Common-Credentials/best110.txt` | Curated common passwords |
| Default credentials | `Passwords/Default-Credentials/default-passwords.txt` | Vendor defaults |
| Credential pairs | `Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt` | FTP default user:pass pairs |

**Common password spray patterns to try manually:**
```
Season+Year     → Summer2023! Winter2024!
Company+Year    → Acme2023! Acme2024!
Welcome patterns → Welcome1 Welcome1! Welcome@1
Common defaults  → Password1 Password1! P@ssw0rd Admin123!
```

---

## SNMP

| Situation | Wordlist | Notes |
|-----------|----------|-------|
| Community string brute-force | `Discovery/SNMP/common-snmp-community-strings.txt` | ~120 common strings; hits `public`/`private`/`manager` etc. |
| Larger community list | `Discovery/SNMP/snmp.txt` | Broader list for thorough sweeps |

```bash
# Brute-force community strings with onesixtyone
onesixtyone -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings.txt -i targets.txt
```

---

## CMS-Specific

| CMS | Wordlist | Notes |
|-----|----------|-------|
| WordPress plugins | `Discovery/Web-Content/CMS/wordpress.fuzz.txt` | WP paths and plugin names |
| WordPress users | via WPScan | `wpscan --url http://target --enumerate u` |
| Joomla | `Discovery/Web-Content/CMS/joomla.txt` | Joomla paths and components |
| Drupal | `Discovery/Web-Content/CMS/drupal.txt` | Drupal paths and modules |

---

## Kerberos / Active Directory

| Situation | Wordlist | Notes |
|-----------|----------|-------|
| Username enumeration | `Usernames/Names/names.txt` | Use with Kerbrute userenum |
| AD username format list | `Usernames/xato-net-10-million-usernames-dup-removed.txt` | Real-world formats |
| Password spray | `Passwords/Common-Credentials/best110.txt` + seasonal patterns | One password at a time |
| AS-REP / TGS cracking | `Passwords/Leaked-Databases/rockyou.txt` | Start here; add rules |

---

## Fuzzing / Injection Lists

> Use these with ffuf `-w` for targeted injection fuzzing instead of hand-crafting payloads.

| Category | Wordlist | Notes |
|----------|----------|-------|
| SQL injection | `Fuzzing/SQLi/Generic-SQLi.txt` | Generic SQLi payloads; good ffuf starting point |
| SQL injection (blind) | `Fuzzing/SQLi/Generic-BlindSQLi.fuzz.txt` | Time-based and boolean blind payloads |
| XSS | `Fuzzing/XSS/XSS-Jhaddix.txt` | Large XSS payload list |
| XSS (simple) | `Fuzzing/XSS/XSS-BruteLogic.txt` | Shorter; faster for initial testing |
| LFI | `Fuzzing/LFI/LFI-Jhaddix.txt` | Comprehensive LFI path list |
| LFI (short) | `Fuzzing/LFI/LFI-gracefulsecurity-linux.txt` | Linux-specific; smaller and faster |
| Special chars | `Fuzzing/special-chars.txt` | Input validation / WAF detection |
| SSTI | `Fuzzing/template-engines-expression.txt` | Template injection detection payloads |

---

## Custom Wordlist Generation

### CeWL — scrape words from a target website
```bash
# Basic scrape (depth 2)
cewl http://target.com -d 2 -m 5 -w cewl_output.txt

# With email harvesting
cewl http://target.com -d 2 -m 5 --email -w cewl_output.txt

# Combine with rockyou for a targeted list
cat cewl_output.txt rockyou.txt > combined.txt
```

### Hashcat rules — mutate a wordlist
```bash
# Apply best64 rules (append numbers, symbols, capitalize)
hashcat --stdout wordlist.txt -r /usr/share/hashcat/rules/best64.rule > mutated.txt

# Apply d3ad0ne rules (more aggressive; good for corporate passwords)
hashcat --stdout wordlist.txt -r /usr/share/hashcat/rules/d3ad0ne.rule > mutated.txt
```

### Extract usernames from an email list
```bash
# Pull everything before @ from a list of emails
cut -d '@' -f1 emails.txt | sort -u > usernames.txt
```

### Build a list from a pattern
```bash
# Generate Season+Year combinations 2020-2025
for season in Spring Summer Autumn Winter Fall; do
    for year in 2020 2021 2022 2023 2024 2025; do
        echo "${season}${year}"
        echo "${season}${year}!"
        echo "${season}@${year}"
    done
done > seasonal_passwords.txt
```

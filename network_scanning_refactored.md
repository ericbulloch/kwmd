# Network Scanning — Refactored Example

This is the refactored "Network Scanning" section from `commands.md` using granular subsection headers (Option 1) for better referenceability.

---

## Network Scanning

### Nmap — Full Port Enumeration

```bash
# Fast full TCP — find all open ports first
nmap -p- --min-rate 5000 -T4 $IP -oA nmap_alltcp
```

### Nmap — Service and Version Detection

```bash
# Targeted version + default scripts against open ports
nmap -sV -sC -p 22,80,443,445 $IP -oA nmap_targeted

# Aggressive (version, scripts, OS detection) — noisy, use after initial scan
nmap -A $IP -oA nmap_aggressive

# Output all formats at once (-oA)
nmap -sV -sC -p- $IP -oA full_scan
```

### Nmap — UDP Port Scanning

```bash
# UDP top 20 (slow — run in background)
nmap -sU --top-ports 20 $IP -oA nmap_udp
```

### Nmap — Vulnerability Scanning

```bash
# Vuln scripts against a specific port
nmap --script vuln -p 445 $IP

# NSE script category
nmap --script "smb-*" -p 139,445 $IP
```

### Nmap — Network Discovery

```bash
# Ping sweep
nmap -sn 192.168.1.0/24
```

### RustScan — Faster Initial Port Discovery

```bash
# Fast all-port scan then pipe to nmap
rustscan -a $IP --ulimit 5000 -- -sV -sC

# Specify port range
rustscan -a $IP -r 1-65535 --ulimit 5000

# Scan subnet
rustscan -a 192.168.1.0/24 --ulimit 5000
```

### Masscan — Fastest (Use for Large Ranges)

```bash
# Full TCP sweep
masscan -p1-65535 $IP --rate=10000 -oL masscan_results.txt

# Top ports only
masscan -p80,443,445,22,3389,8080 192.168.1.0/24 --rate=5000
```

---

## Benefits of This Structure

1. **Clear, Referenceable Anchors** - You can now link to:
   - `[Nmap Full Port Enumeration](commands.md#nmap--full-port-enumeration)`
   - `[Nmap Service Detection](commands.md#nmap--service-and-version-detection)`
   - `[Nmap UDP Scanning](commands.md#nmap--udp-port-scanning)`
   - `[Nmap Vulnerability Scanning](commands.md#nmap--vulnerability-scanning)`
   - `[Nmap Network Discovery](commands.md#nmap--network-discovery)`
   - `[RustScan](commands.md#rustscan--faster-initial-port-discovery)`
   - `[Masscan](commands.md#masscan--fastest-use-for-large-ranges)`

2. **Scannable** - Users can quickly find what they need

3. **Methodology Alignment** - Each step in `methodology.md` can reference a specific subsection instead of a broad "Network Scanning" section

4. **Consistency** - The naming pattern (`ToolName — Use Case`) is consistent throughout

---

## Example Cross-Reference from methodology.md

In `methodology.md` line 114-119 (Port Scanning section), you could now link like this:

```markdown
### Port Scanning

See [Nmap Full Port Enumeration](commands.md#nmap--full-port-enumeration), 
[Nmap Service Detection](commands.md#nmap--service-and-version-detection), 
[RustScan](commands.md#rustscan--faster-initial-port-discovery), 
and [Masscan](commands.md#masscan--fastest-use-for-large-ranges) 
for command syntax and examples.

1. **Fast full TCP scan** — scan all 65535 ports quickly to find open ports
```

This gives a direct link to exactly the commands the user needs without having to search through the entire Network Scanning section.

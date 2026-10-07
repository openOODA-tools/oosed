# oosed

> **Capability-bounded stream editor and text transformer for the openOODA era.**  
> *A drop-in `sed` alternative written in pure openOODA, featuring negative-trust capability security, pattern substitutions, in-place bounded file writes (`FsWriteCap`), and a first-class Model Context Protocol (MCP) surface.*

Part of [openOODA-tools](https://github.com/openOODA-tools).

---

## 1. Installation

`oosed` has zero runtime dependencies. It compiles to a standalone native binary linked directly with libc.

### Universal Web Installer
Installs the standalone native binary to `/usr/local/bin` (or `~/.local/bin`):

```bash
curl -fsSL https://openooda-tools.github.io/oosed/install.sh | bash
```

### Debian / Ubuntu (APT)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/oosed/install.sh | bash -s -- --apt

# Or manual package install
sudo dpkg -i oosed_0.1.0-1_amd64.deb
```

### Fedora / RHEL / CentOS (DNF)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/oosed/install.sh | bash -s -- --dnf

# Or manual RPM install
sudo dnf install ./oosed-0.1.0-1.fc44.x86_64.rpm
```

### Arch Linux (PKGBUILD)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/oosed/install.sh | bash -s -- --arch

# Or manual build via packaging/PKGBUILD
cd packaging && makepkg -si
```

### Clean Uninstaller
To cleanly remove `oosed` and any installed package manager entries:

```bash
# Automated via standalone uninstaller
curl -fsSL https://openooda-tools.github.io/oosed/uninstall.sh | bash

# Or via installer flag
curl -fsSL https://openooda-tools.github.io/oosed/install.sh | bash -s -- --uninstall

# Or preview removal without making changes (dry-run)
curl -fsSL https://openooda-tools.github.io/oosed/uninstall.sh | bash -s -- --dry-run
```

---

## 2. Usage & Features

### Stream Editing & In-Place Writes
Perform stream transformations on standard input or files:

```bash
# Substitute first occurrence of pattern
echo "hello world" | oosed 's/world/universe/'

# Global substitution across line
echo "apple banana apple" | oosed 's/apple/orange/g'

# Delete matching lines
cat input.txt | oosed '/deprecated/d'

# Quiet mode with selective printing
cat input.txt | oosed -n '/ERROR/p'

# Safe in-place modification (gated by FsWriteCap)
oosed -i 's/v1.0.0/v1.0.1/g' config.oot
```

### Model Context Protocol (MCP) Mode
`oosed` speaks JSON-RPC 2.0 MCP over stdio for LLM coding agents:

```bash
oosed --mcp
```

#### MCP Tools Provided:
- `stream_replace`: Replace string patterns in arbitrary text blocks.
  - Parameters: `text` (string), `pattern` (string), `replacement` (string), `global` (boolean)
- `execute_script`: Apply standard sed scripts (`s/pat/repl/g`, `/pat/d`) on text.
  - Parameters: `text` (string), `script` (string)

---

## 3. Capability Security & Verification

`oosed` enforces strict Object Capability Discipline (OCap):
- **FsReadCap**: Strictly bounded read access to input files.
- **FsWriteCap**: Required exclusively when `-i` / `--in-place` writing is explicitly commanded.
- **Zero Ambient Authority**: Zero network sockets, zero child process spawning, zero unprompted disk writes.
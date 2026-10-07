Name:           oosed
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-bounded stream editor and text transformer
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosed
Source0:        oosed-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosed is a sovereign, capability-bounded file viewer and cat replacement written
in pure openOODA, featuring syntax highlighting via oote themes, line numbering,
range slicing, blank squeezing, box borders, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosed
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosed-uninstall

%files
/usr/bin/oosed
/usr/bin/oosed-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign release: syntax highlighting, oote palettes, and MCP stdio surface

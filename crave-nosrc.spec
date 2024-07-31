# No SOURCE spec-file

#
# Crave
#

%define oname crave

Summary:    Crave
Name:       crave
Version:    0.2
Release:    1
License:    MPL-2.0
Group:      Productivity
URL:        https://crave.io/

Source0:    crave-0.2-7029-linux-aarch64.bin
Source1:    crave-0.2-7029-linux-amd64.bin
Source2:    %{oname}.png

BuildRequires:  openssh
BuildRequires:  rsync
BuildRequires:  openssl
ExclusiveArch:  x86_64 aarch64

%description
Unofficial Community Build. Build any open source project in seconds

%prep
cd %_builddir

%build
#nobuild

%install
if [ "$(uname -m)" = "x86_64" ]; then
    install -D %{SOURCE0} %{buildroot}%{_bindir}/crave
elif [ "$(uname -m)" = "aarch64" ]; then
    install -D %{SOURCE1} %{buildroot}%{_bindir}/crave
fi

%post

%postun

%clean

%files
%defattr(-,root,root)
%{_bindir}/*
%dir

Requires: openssh, rsync, openssl

%changelog
* Wed Jul 31 2024 tex - 0.2-1pclos2024
- new version

* Sun Jul 21 2024 tex - 0.2-1pclos2024
- new version

* Thu Jul 18 2024 tex - 0.2-1pclos2024
- new version


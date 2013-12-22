Summary:	GNU Privacy Guard - secure communication and data storage
Name:		gnupg
Version:	1.4.16
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/GnuPG/gnupg/%{name}-%{version}.tar.bz2
# Source0-md5:	6df73c57d3ece1dd36dc2a7679f00fb0
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libcap-devel
BuildRequires:	libusb-compat-devel
BuildRequires:	openldap-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%package plugin-keys-curl
Summary:	GnuPG plugin for allow talk to a HTTP/FTP keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-curl
GnuPG plugin for allow talk to a HTTP(S)/FTP(S) keyserver.

%package plugin-keys-finger
Summary:	GnuPG plugin for allow talk to a FINGER keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-finger
GnuPG plugin for allow talk to a FINGER keyserver.

%package plugin-keys-hkp
Summary:	GnuPG plugin for allow talk to a HKP keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-hkp
GnuPG plugin for allow talk to a HKP keyserver.

%package plugin-keys-ldap
Summary:	GnuPG plugin for allow talk to a LDAP keyserver
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys-ldap
GnuPG plugin for allow talk to a LDAP keyserver.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub scripts
%configure \
	--enable-ldap		\
	--with-capabilities	\
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/ru/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/gpg.ru.1 $RPM_BUILD_ROOT%{_mandir}/ru/man1/gpg.1

%find_lang %{name}

rm -f $RPM_BUILD_ROOT{%{_datadir}/gnupg/{FAQ,faq.html},%{_infodir}/dir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,OpenPGP}
%attr(755,root,root) %{_bindir}/gpg
%attr(755,root,root) %{_bindir}/gpg-zip
%attr(755,root,root) %{_bindir}/gpgsplit
%attr(755,root,root) %{_bindir}/gpgv
%dir %{_libexecdir}/gnupg
%dir %{_datadir}/gnupg
%{_datadir}/gnupg/options.skel
%{_mandir}/man1/gpg.1*
%{_mandir}/man1/gpg-zip.1*
%{_mandir}/man1/gpgv.1*
%{_mandir}/man7/gnupg.7*
%lang(ru) %{_mandir}/ru/man1/gpg.1*
%{_infodir}/gnupg1.info*

%files plugin-keys-finger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_finger

%files plugin-keys-hkp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_hkp

%files plugin-keys-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_curl

%files plugin-keys-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_ldap


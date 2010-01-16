%define upstream_name    XML-Twig
%define upstream_version 3.33

Name:          perl-%{upstream_name}
Version:       %perl_convert_version %{upstream_version}
Release:       %mkrel 1

Summary:        A perl module for processing huge XML documents in tree mode
License:        Artistic
Group:          Development/Perl
Url:            http://www.xmltwig.com/xmltwig/
Source0:        http://www.xmltwig.com/xmltwig/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Handler::YAWriter)
# for tests
BuildRequires:	perl(HTML::Tree)
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl(Unicode::Map8)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(XML::XPath)
BuildRequires:	perl(XML::XPathEngine)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
XML::Twig is a Perl module that subclasses XML-Parser to allow easy
processing of XML documents of all sizes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
# TODO: maintainer: package them if requested...
%{__perl} Makefile.PL INSTALLDIRS=vendor << EOF
n
n
n
EOF
%make

%check
%make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%{perl_vendorlib}/XML
%{_mandir}/*/*
%{_bindir}/*

%define module  XML-Twig
%define name    perl-%{module}
%define version 3.32
%define release %mkrel 2

Name:          %{name}
Version:       %{version}
Release:       %{release}
Summary:        A perl module for processing huge XML documents in tree mode
License:        Artistic
Group:          Development/Perl
Source:         http://www.xmltwig.com/xmltwig/%{module}-%{version}.tar.bz2
Url:            http://www.xmltwig.com/xmltwig/
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Handler::YAWriter)
# for tests
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-Unicode-Map8
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-XML-XPath
BuildRequires:	perl-XML-XPathEngine
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
XML::Twig is a Perl module that subclasses XML-Parser to allow easy
processing of XML documents of all sizes.

%prep
%setup -q -n %{module}-%{version}

%build
# TODO: maintainer: package them if requested...
%{__perl} Makefile.PL INSTALLDIRS=vendor << EOF
n
n
n
EOF
%make

%check
%{__make} test

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


%define modname	XML-Twig
%define modver	3.52

Summary:	A perl module for processing huge XML documents in tree mode
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	Artistic
Group:		Development/Perl
Url:		http://www.mirod.org/xmltwig/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIROD/XML-Twig-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	expat
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::Handler::YAWriter)
# for tests
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTML::Tree)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(IO::CaptureOutput)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(LWP)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl(Unicode::Map8)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(XML::XPath)
BuildRequires:	perl(XML::XPathEngine)
BuildRequires:	perl(XML::Filter::BufferText)
BuildRequires:	perl(XML::SAX::Writer)

%description
XML::Twig is a Perl module that subclasses XML-Parser to allow easy
processing of XML documents of all sizes.

%prep
%setup -qn %{modname}-%{modver}

%build
# TODO:	maintainer:	package them if requested...
%__perl Makefile.PL INSTALLDIRS=vendor << EOF
n
n
n
EOF
%make

%check
%make test || :

%install
%makeinstall_std

%files
%{_bindir}/*
%{perl_vendorlib}/XML
%{_mandir}/man1/*
%{_mandir}/man3/*


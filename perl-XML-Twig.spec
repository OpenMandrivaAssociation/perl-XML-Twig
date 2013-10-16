%define upstream_name    XML-Twig
%define upstream_version 3.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A perl module for processing huge XML documents in tree mode
License:	Artistic
Group:		Development/Perl
Url:		http://www.mirod.org/xmltwig/
Source0:	http://www.mirod.org/xmltwig/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::Handler::YAWriter)
# for tests
BuildRequires:	perl(HTML::Tree)
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl(Unicode::Map8)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(XML::XPath)
BuildRequires:	perl(XML::XPathEngine)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(IO::CaptureOutput)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(XML::Filter::BufferText)
BuildRequires:  perl(XML::SAX::Writer)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  expat

BuildArch:	noarch

%description
XML::Twig is a Perl module that subclasses XML-Parser to allow easy
processing of XML documents of all sizes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
# TODO: maintainer: package them if requested...
%__perl Makefile.PL INSTALLDIRS=vendor << EOF
n
n
n
EOF
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/XML
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.380.0-5mdv2012.0
+ Revision: 765855
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 3.380.0-3
+ Revision: 763287
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.380.0-2
+ Revision: 667460
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.380.0-1
+ Revision: 643498
- update to new version 3.38

* Tue Oct 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.370.0-1mdv2011.0
+ Revision: 585097
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 3.350.0-2mdv2011.0
+ Revision: 564758
- rebuild for perl 5.12.1

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.350.0-1mdv2011.0
+ Revision: 551211
- update to 3.35

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 3.340.0-1mdv2010.1
+ Revision: 493490
- update to 3.34

* Sat Jan 16 2010 Jérôme Quelin <jquelin@mandriva.org> 3.330.0-1mdv2010.1
+ Revision: 492161
- update to 3.33

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 3.320.0-1mdv2010.0
+ Revision: 401830
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.32-3mdv2009.1
+ Revision: 351657
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.32-2mdv2009.0
+ Revision: 224674
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.32-1mdv2008.1
+ Revision: 109549
- update to new version 3.32

* Fri Nov 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.31-1mdv2008.1
+ Revision: 107224
- update to new version 3.31
- update to new version 3.31

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.30-1mdv2008.1
+ Revision: 106666
- update to new version 3.30

* Mon Apr 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.29-2mdv2008.0
+ Revision: 19378
-New version


* Sat Dec 23 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-12-23 00:18:54 (101855)
- add some build deps for tests

* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org>
+ 2006-12-19 14:08:20 (99693)
Import perl-XML-Twig

* Wed Jul 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.26-1mdv2007.0
- New version 3.26

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.25-1mdv2007.0
- New release 3.25

* Mon Nov 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.23-1mdk
- new release (fix some bugs) 
- make test in %%check
- fix directory ownership
- better summary
- %%mkrel

* Tue Oct 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.22-1mdk
- New release 3.22

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.21-1mdk
- New release 3.21

* Fri Apr 15 2005 Guillaume Rousse <guillomovitch@mandrake.org> 3.17-1mdk
- New release 3.17
- buildrequires perl-XML-Handler-YAWriter
- spec cleanup

* Wed Feb 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.16-1mdk
- 3.16
- new utilities xml_*

* Thu Jan 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.15-2mdk
- Remove arch-dependent directories

* Tue Apr 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.15-1mdk
- new version
- let spechelper do its job
- dir ownership


Summary:	Musepack encoder
Name:		mppenc
Version:	1.16
Release:	%mkrel 7
License:	LGPL
Group:		Sound
Source0:	http://files.musepack.net/source/mppenc-%{version}.tar.bz2
URL:		http://www.musepack.net/
BuildRequires:	nasm
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This program handles encoding of the MPC format, which is an audio
compression format with a strong emphasis on high quality. It's not
lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much
smaller MPC file. It is based on the MPEG-1 Layer-2 / MP2 algorithms,
but since 1997 it has rapidly developed and vastly improved and is now
at an advanced stage in which it contains heavily optimized and
patentless code.

%prep
%setup -q %{name}-%{version} 

%build
cmake -DCMAKE_INSTALL_PREFIX:=%{_prefix}
	    
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.16-7mdv2011.0
+ Revision: 620406
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.16-6mdv2010.0
+ Revision: 430104
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.16-5mdv2009.0
+ Revision: 252992
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.16-3mdv2008.1
+ Revision: 136609
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.16-3mdv2007.0
+ Revision: 110441
- drop requires

* Thu Jan 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.16-2mdv2007.1
+ Revision: 110371
- fix requires

* Thu Jan 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.16-1mdv2007.1
+ Revision: 110086
- Import mppenc


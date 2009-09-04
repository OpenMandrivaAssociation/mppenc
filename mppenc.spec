Summary:	Musepack encoder
Name:		mppenc
Version:	1.16
Release:	%mkrel 6
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



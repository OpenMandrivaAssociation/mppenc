Summary:	Musepack encoder
Name:		mppenc
Version:	1.16
Release:	9
License:	LGPLv2.1+
Group:		Sound
Url:		https://www.musepack.net/
Source0:	http://files.musepack.net/source/mppenc-%{version}.tar.bz2
Patch0:		mppenc-1.16-cflags.patch
BuildRequires:	cmake

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
%setup -q
%patch0 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc Changelog
%{_bindir}/%{name}


Summary:	Sensors plugin for gkrellm
Summary(pl):	Wtyczka monitorowania czujników dla gkrellm
Name:		gkrellm-sensors
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/gklmsensors/gklmsensors-%{version}.tar.bz2
Requires:	gkrellm
BuildRequires:	gkrellm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		%{_usr}/X11R6
%define		_mandir		%{_prefix}/man

%description
A GKrellM plugin wich allows you to monitor your sensors.

%description -l pl
Wtyczka GKrellM pozwalaj±ca monitorowaæ czujniki.

%prep
%setup -q -n gklmsensors

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -D sensors.so $RPM_BUILD_ROOT%{_libdir}/gkrellm/sensors.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Change*
%attr(755,root,root) %{_libdir}/gkrellm/*.so

# TODO: CFLAGS, problems with gkrellm-2.2.xx at amd64 arch
Summary:	Sensors plugin for gkrellm
Summary(pl):	Wtyczka monitorowania czujników dla gkrellm
Name:		gkrellm-sensors
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gklmsensors/gklmsensors-%{version}.tar.bz2
# Source0-md5:	88c76ceb05cedb7cdb56dd92a52ae540
URL:		http://sourceforge.net/projects/gklmsensors/
BuildRequires:	gkrellm-devel >= 2.0
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

install -D sensors.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/sensors.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Change*
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/*.so

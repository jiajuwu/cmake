Name:hello
Version:1.0
Release:1%{?dist}
Summary:hello is a test program.

Group:Development/Tools
License:GPL
URL:
Source0:

BuildRequires:gcc
Requires:

%description
The hellorpm program is a test.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog


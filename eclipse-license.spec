%{?_javapackages_macros:%_javapackages_macros}
%global license_ver 1.0.0
%global qualifier v20131003-1638
%global gittag license-%{license_ver}.%{qualifier}

Name:      eclipse-license
Version:   %{license_ver}
Release:   2%{?dist}
Summary:   Shared license feature for Eclipse

License:   EPL
URL:       http://wiki.eclipse.org/CBI
Source0:   http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{gittag}.tar.bz2

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: tycho-extras
BuildRequires: feclipse-maven-plugin

%description
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%prep
%setup -q -n %{gittag}

%build
xmvn -o clean verify

%install
xmvn -o org.fedoraproject:feclipse-maven-plugin:install \
  -DsourceRepo=org.eclipse.license.repo/target/repository/ \
  -DtargetLocation=%{buildroot}%{_javadir}/%{name}/eclipse

%files
%doc org.eclipse.license/epl-v10.html
%{_javadir}/%{name}

%changelog
* Thu Mar 13 2014 Mat Booth <fedora@matbooth.co.uk> - 1.0.0-2
- Use Xmvn.

* Thu Mar 13 2014 Mat Booth <fedora@matbooth.co.uk> - 1.0.0-1
- Initial version of license shared feature.


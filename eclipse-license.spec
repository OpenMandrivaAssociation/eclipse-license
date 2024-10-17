%{?_javapackages_macros:%_javapackages_macros}
%global license_ver 1.0.1
%global qualifier v20140414-1359
%global gittag org.eclipse.license-license-%{license_ver}.%{qualifier}

Name:      eclipse-license
Version:   %{license_ver}
Release:   5%{?dist}
Summary:   Shared license feature for Eclipse

License:   EPL
URL:       https://wiki.eclipse.org/CBI
Source0:   http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{gittag}.tar.bz2

BuildArch: noarch

BuildRequires: tycho
BuildRequires: tycho-extras
BuildRequires: eclipse-filesystem

Requires: eclipse-filesystem

%description
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%prep
%setup -q -n %{gittag}

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc org.eclipse.license/epl-v10.html

%changelog
* Tue Aug 26 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-5
- Build/install with xmvn
- Require eclipse-filesystem

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-3
- Update to latest upstream.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Use Xmvn.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Initial version of license shared feature.


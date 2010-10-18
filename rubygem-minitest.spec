# Generated from minitest-1.7.2.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname minitest
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: minitest/unit is a small and fast replacement for ruby's huge and slow test/unit
Name: rubygem-%{gemname}
Version: 1.7.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/bfts
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: rubygems
Requires: rubygem(rubyforge) >= 2.0.4
Requires: rubygem(minitest) >= 1.6.0
Requires: rubygem(hoe) >= 2.6.0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
minitest/unit is a small and fast replacement for ruby's huge and slow
test/unit. This is meant to be clean and easy to use both as a regular
test writer and for language implementors that need a minimal set of
methods to bootstrap a working unit test suite.
mini/spec is a functionally complete spec engine.
mini/mock, by Steven Baker, is a beautifully tiny mock object framework.
(This package was called miniunit once upon a time)


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct 18 2010 : Sergio Rubio <rubiojr@frameos.org> - 1.7.2-1
- Initial package

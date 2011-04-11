#
# spec file for package rubygem-ruote-kit
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           rubygem-ruote-kit
Version:        2.2.1
Release:        1
%define mod_name ruote-kit
#
Group:          Development/Languages/Ruby
License:        MIT
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
BuildRequires:  rubygem-sinatra >= 1.0
Requires:       rubygem-sinatra >= 1.0
BuildRequires:  rubygem-sinatra-respond_to >= 0.5.0
Requires:       rubygem-sinatra-respond_to >= 0.5.0
BuildRequires:  rubygem-haml >= 3.0.25
Requires:       rubygem-haml >= 3.0.25
BuildRequires:  rubygem-rufus-json >= 0.2.5
Requires:       rubygem-rufus-json >= 0.2.5
BuildRequires:  rubygem-ruote >= 2.2.0
Requires:       rubygem-ruote >= 2.2.0
#
Url:            http://github.com/tosch/ruote-kit
Source:         %{mod_name}-%{version}.gem
#
Summary:        ruote workflow engine, wrapped in a loving rack embrace
%description

ruote workflow engine, wrapped in a loving rack embrace

%package doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
%description doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%package testsuite
Summary:        Test suite for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
%description testsuite
Test::Unit or RSpec files, useful for developers.

%prep
%build
%install
%gem_install %{S:0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%exclude %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/spec
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec

%files doc
%defattr(644,root,root,755)
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%files testsuite
%defattr(644,root,root,755)
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/spec

%changelog

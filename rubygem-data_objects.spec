# Generated from data_objects-0.10.7.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	data_objects

Summary:	DataObjects basic API and shared driver specifications
Name:		rubygem-%{rbname}

Version:	0.10.7
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/do
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Provide a standard and simplified API for communicating with RDBMS from Ruby

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/error
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/error/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/error
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/error/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/typecast
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/typecast/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.markdown

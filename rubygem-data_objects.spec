
%define	rbname	data_objects

Summary:	DataObjects basic API and shared driver specifications
Name:		rubygem-%{rbname}

Version:	0.10.14
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/do
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Provide a standard and simplified API for communicating with RDBMS from Ruby.

%files
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/error/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/error/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/typecast/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
#-------------------------------------------------------------------------------------

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.markdown
#-------------------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install







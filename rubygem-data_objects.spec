
%define	rbname	data_objects

Summary:	DataObjects basic API and shared driver specifications
Name:		rubygem-%{rbname}

Version:	0.10.14
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/do
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Provide a standard and simplified API for communicating with RDBMS from Ruby.

%files
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/data_objects/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/data_objects/error/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/data_objects/spec/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/data_objects/spec/lib/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/error/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/data_objects/spec/shared/typecast/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
#-------------------------------------------------------------------------------------

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
%{gem_dir}/gems/%{rbname}-%{version}/*.markdown
#-------------------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install







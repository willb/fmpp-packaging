%global fmpp_version 0.9.14

Name:           fmpp
Version:        %{fmpp_version}
Release:        1%{?dist}
Summary:        FreeMarker-based text file PreProcessor 

License:        BSD
URL:            http://fmpp.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/fmpp/fmpp_%{version}.tar.gz
Patch0:		fmpp-0.9.14-build.xml.patch

BuildRequires:  jpackage-utils

BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(bsh:bsh)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildRequires:  mvn(xml-apis:xml-apis) 

BuildRequires:  jpackage-utils

Requires:  mvn(oro:oro)
Requires:  mvn(org.freemarker:freemarker)
Requires:  mvn(bsh:bsh)
Requires:  mvn(xml-resolver:xml-resolver)
Requires:  mvn(xml-apis:xml-apis) 

BuildArch:	noarch


%description

FMPP is a general-purpose text file preprocessor tool that uses
FreeMarker templates. It is particularly designed for HTML
preprocessor, to generate complete (static) homepages: directory
structure that contains HTML-s, image files, etc. But of course it can
be used to generate source code or whatever text files. FMPP is
extendable with Java classes to pull data from any data sources
(database, etc.) and embed the data into the generated files.

%prep
%setup -q -n %{name}_%{fmpp_version}
%patch0 -p1 

find lib -name \*.jar -delete

%build
ant compile jar docs


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}
cp lib/fmpp.jar %{buildroot}/%{_javadir}

%files
%doc LICENSE.txt
%{_javadir}/fmpp.jar


%changelog

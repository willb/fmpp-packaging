%global fmpp_version 0.9.14

Name:           fmpp
Version:        %{fmpp_version}
Release:        1%{?dist}
Summary:        FreeMarker-based text file PreProcessor 

License:        BSD
URL:            http://fmpp.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/fmpp/fmpp_%{version}.tar.gz
Source1:	http://repo1.maven.org/maven2/net/sourceforge/fmpp/fmpp/%{fmpp_version}/fmpp-%{fmpp_version}.pom
Patch0:		fmpp-0.9.14-build.xml.patch

BuildRequires:  jpackage-utils
BuildRequires:	java-devel

BuildRequires:	ant

BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildRequires:  mvn(xml-apis:xml-apis) 

Requires:	jpackage-utils
Requires:	java-devel

Requires:  mvn(oro:oro)
Requires:  mvn(org.freemarker:freemarker)
Requires:  mvn(org.beanshell:bsh)
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

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{name}_%{fmpp_version}
%patch0 -p1 

find lib -name \*.jar -delete

pushd lib/forbuild/classes/imageinfo 
rm *.class 
cp Imageinfo.java.dontcheck ImageInfo.java
popd

%build

pushd lib/forbuild/classes/imageinfo
javac ImageInfo.java
popd

ant compile jar docs

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}
mkdir -p %{buildroot}/%{_mavenpomdir}
mkdir -p %{buildroot}/%{_javadocdir}/%{name}

cp lib/fmpp.jar %{buildroot}/%{_javadir}
cp %{SOURCE1} %{buildroot}/%{_mavenpomdir}/JPP-fmpp.pom
cp -rp docs/* %{buildroot}/%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt README.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt README.txt
%{_javadocdir}/%{name}

%changelog

* Thu Jan 2 2014 William Benton <willb@redhat.com> - 0.9.14-1
- initial package


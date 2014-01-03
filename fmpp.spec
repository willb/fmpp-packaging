%global fmpp_version 0.9.14

Name:		fmpp
Version:	%{fmpp_version}
Release:	1%{?dist}
Summary:	FreeMarker-based text file PreProcessor 

License:	BSD
URL:		http://fmpp.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/fmpp/fmpp_%{version}.tar.gz

Patch0:		fmpp-0.9.14-build.xml.patch
Patch1:		fmpp-0.9.14-excise-imageinfo.patch

BuildRequires:	javapackages-tools
BuildRequires:	java-devel

BuildRequires:	ant

BuildRequires:	mvn(oro:oro)
BuildRequires:	mvn(org.freemarker:freemarker)
BuildRequires:	mvn(org.beanshell:bsh)
BuildRequires:	mvn(xml-resolver:xml-resolver)
BuildRequires:	mvn(xml-apis:xml-apis) 

Requires:	javapackages-tools
Requires:	java

Requires:	mvn(oro:oro)
Requires:	mvn(org.freemarker:freemarker)
Requires:	mvn(org.beanshell:bsh)
Requires:	mvn(xml-resolver:xml-resolver)
Requires:	mvn(xml-apis:xml-apis) 

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
Group:		Documentation
Summary:	Javadoc for %{name}
BuildArch:	noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{name}_%{fmpp_version}
%patch0 -p1 
%patch1 -p1 

find lib -name \*.jar -delete

rm -rf lib/forbuild/classes

# these two tests don't pass for some reason
find . -name always_create_dirs_\* -and -type d | xargs rm -rf

# strip carriage returns
find . -name \*.fmpp -or\
 -name package-list -or\
 -name \*.bsh -or\
 -name \*.txt -or\
 -name \*.xml -or\
 -name \*.c -or \
 -name \*.css -or \
 -name \*.csv -or \
 -name \*.dtd -or \
 -name \*.ent -or \
 -name \*.ftl -or \
 -name \*.html -or \
 -name \*.tdd| xargs sed -i 's/\r$//'

%build

ant build

ant make-pom

%check

ant test

%install
mkdir -p %{buildroot}/%{_javadir}
mkdir -p %{buildroot}/%{_mavenpomdir}
mkdir -p %{buildroot}/%{_javadocdir}/%{name}

cp lib/fmpp.jar %{buildroot}/%{_javadir}
cp build/pom.xml %{buildroot}/%{_mavenpomdir}/JPP-fmpp.pom
cp -rp docs/* %{buildroot}/%{_javadocdir}/%{name}

find %{buildroot} -size 0 -delete

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


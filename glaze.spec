#
# Conditional build:
%bcond_with	avx2	# Use AVX2 intrinsics

Summary:	Extremely fast JSON and interface library for modern C++
Name:		glaze
Version:	5.2.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/stephenberry/glaze/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	50f0636337a812a71cc18b9058ad83dd
URL:		https://github.com/stephenberry/glaze
BuildRequires:	cmake >= 3.21
BuildRequires:	libstdc++-devel >= 6:11
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.742
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Extremely fast, in memory, JSON and interface library for modern C++.

%package devel
Summary:	Extremely fast JSON and interface library for modern C++
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:11
BuildArch:	noarch

%description devel
Extremely fast, in memory, JSON and interface library for modern C++.

%prep
%setup -q

%build
%cmake -B build \
	-Dglaze_INSTALL_CMAKEDIR:PATH="%{_datadir}/cmake/glaze" \
	-DBUILD_TESTING:BOOL=OFF \
	-Dglaze_DEVELOPER_MODE:BOOL=OFF \
	-Dglaze_ENABLE_FUZZING:BOOL=OFF \
	%{cmake_on_off avx2 glaze_ENABLE_AVX2}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/glaze
%{_datadir}/cmake/glaze

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-hammock
Version  : 0.2.4
Release  : 29
URL      : https://files.pythonhosted.org/packages/c0/4c/a0af8e8c868268a3a24b686e2b82ba6803e0c8c8da3ed89d1099b324ef90/hammock-0.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/4c/a0af8e8c868268a3a24b686e2b82ba6803e0c8c8da3ed89d1099b324ef90/hammock-0.2.4.tar.gz
Summary  : rest like a boss
Group    : Development/Tools
License  : MIT
Requires: pypi-hammock-python = %{version}-%{release}
Requires: pypi-hammock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(requests)

%description
::
_                                   _
| |                                 | |
| |__  _____ ____  ____   ___   ____| |  _
|  _ \(____ |    \|    \ / _ \ / ___) |_/ )
| | | / ___ | | | | | | | |_| ( (___|  _ (
|_| |_\_____|_|_|_|_|_|_|\___/ \____)_| \_)

%package python
Summary: python components for the pypi-hammock package.
Group: Default
Requires: pypi-hammock-python3 = %{version}-%{release}

%description python
python components for the pypi-hammock package.


%package python3
Summary: python3 components for the pypi-hammock package.
Group: Default
Requires: python3-core
Provides: pypi(hammock)
Requires: pypi(requests)

%description python3
python3 components for the pypi-hammock package.


%prep
%setup -q -n hammock-0.2.4
cd %{_builddir}/hammock-0.2.4
pushd ..
cp -a hammock-0.2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401839
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

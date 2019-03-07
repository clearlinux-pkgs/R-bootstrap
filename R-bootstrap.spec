#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bootstrap
Version  : 2017.2
Release  : 5
URL      : https://cran.r-project.org/src/contrib/bootstrap_2017.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bootstrap_2017.2.tar.gz
Summary  : Functions for the Book "An Introduction to the Bootstrap"
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-bootstrap-lib
BuildRequires : clr-R-helpers

%description
for the book "An Introduction to the Bootstrap" by B. Efron and
        R. Tibshirani, 1993, Chapman and Hall. This package is
        primarily provided for projects already based on it, and for
        support of the book. New projects should preferentially use the
        recommended package "boot".

%package lib
Summary: lib components for the R-bootstrap package.
Group: Libraries

%description lib
lib components for the R-bootstrap package.


%prep
%setup -q -c -n bootstrap

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530471482

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530471482
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bootstrap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bootstrap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bootstrap
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bootstrap|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bootstrap/DESCRIPTION
/usr/lib64/R/library/bootstrap/INDEX
/usr/lib64/R/library/bootstrap/LICENSE
/usr/lib64/R/library/bootstrap/Meta/Rd.rds
/usr/lib64/R/library/bootstrap/Meta/data.rds
/usr/lib64/R/library/bootstrap/Meta/features.rds
/usr/lib64/R/library/bootstrap/Meta/hsearch.rds
/usr/lib64/R/library/bootstrap/Meta/links.rds
/usr/lib64/R/library/bootstrap/Meta/nsInfo.rds
/usr/lib64/R/library/bootstrap/Meta/package.rds
/usr/lib64/R/library/bootstrap/NAMESPACE
/usr/lib64/R/library/bootstrap/NEWS
/usr/lib64/R/library/bootstrap/R/bootstrap
/usr/lib64/R/library/bootstrap/R/bootstrap.rdb
/usr/lib64/R/library/bootstrap/R/bootstrap.rdx
/usr/lib64/R/library/bootstrap/data/Rdata.rdb
/usr/lib64/R/library/bootstrap/data/Rdata.rds
/usr/lib64/R/library/bootstrap/data/Rdata.rdx
/usr/lib64/R/library/bootstrap/data/datalist
/usr/lib64/R/library/bootstrap/help/AnIndex
/usr/lib64/R/library/bootstrap/help/aliases.rds
/usr/lib64/R/library/bootstrap/help/bootstrap.rdb
/usr/lib64/R/library/bootstrap/help/bootstrap.rdx
/usr/lib64/R/library/bootstrap/help/paths.rds
/usr/lib64/R/library/bootstrap/html/00Index.html
/usr/lib64/R/library/bootstrap/html/R.css
/usr/lib64/R/library/bootstrap/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bootstrap/libs/bootstrap.so
/usr/lib64/R/library/bootstrap/libs/bootstrap.so.avx2
/usr/lib64/R/library/bootstrap/libs/bootstrap.so.avx512

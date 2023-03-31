Name:		texlive-europasscv
Version:	56829
Release:	2
Summary:	Unofficial class for the new version of the Europass curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/europasscv
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/europasscv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/europasscv.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is an unofficial LaTeX implementation of the
Europass CV, the standard model for curriculum vitae as
recommended by the European Commission. It includes the major
style updates that came out in 2013, featuring a neater, more
compact and somewhat fancier layout.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/europasscv
%doc %{_texmfdistdir}/doc/latex/europasscv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

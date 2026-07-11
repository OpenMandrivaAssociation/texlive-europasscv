%global tl_name europasscv
%global tl_revision 56829

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Unofficial class for the new version of the Europass curriculum vitae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/europasscv
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/europasscv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/europasscv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class is an unofficial LaTeX implementation of the Europass CV, the
standard model for curriculum vitae as recommended by the European
Commission. It includes the major style updates that came out in 2013,
featuring a neater, more compact and somewhat fancier layout.


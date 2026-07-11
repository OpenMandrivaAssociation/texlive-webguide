%global tl_name webguide
%global tl_revision 77050

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Brief guide to LaTeX tools for Web publishing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/webguide
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/webguide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/webguide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The documentation constitutes an example of the package's own
recommendations (being presented both in PDF and HTML).


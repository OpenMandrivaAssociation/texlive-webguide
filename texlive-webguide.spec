# revision 15878
# category Package
# catalog-ctan /info/webguide
# catalog-date 2008-04-19 22:54:02 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-webguide
Version:	20080419
Release:	1
Summary:	Brief Guide to LaTeX Tools for Web publishing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/webguide
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/webguide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/webguide.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The documentation constitutes an example of the package's own
recommendations (being presented both in PDF and HTML).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/webguide/README
%doc %{_texmfdistdir}/doc/latex/webguide/expeg.6
%doc %{_texmfdistdir}/doc/latex/webguide/expeg6.mps
%doc %{_texmfdistdir}/doc/latex/webguide/webguide.css
%doc %{_texmfdistdir}/doc/latex/webguide/webguide.html
%doc %{_texmfdistdir}/doc/latex/webguide/webguide.pdf
%doc %{_texmfdistdir}/doc/latex/webguide/webguide.ps.gz
%doc %{_texmfdistdir}/doc/latex/webguide/webguide.tex
%doc %{_texmfdistdir}/doc/latex/webguide/webguide0x.gif

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

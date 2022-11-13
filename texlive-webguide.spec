Name:		texlive-webguide
Version:	25813
Release:	1
Summary:	Brief Guide to LaTeX Tools for Web publishing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/webguide
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/webguide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/webguide.doc.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/webguide/webguide.tex
%doc %{_texmfdistdir}/doc/latex/webguide/webguide0x.gif

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

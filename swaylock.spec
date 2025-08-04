Summary:	Screen locker for Wayland
Name:		swaylock
Version:	1.8.3
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/swaywm/swaylock/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	decec6b2ea2eceeaf832a441bc36e769
Source1:	%{name}.pamd
URL:		https://github.com/swaywm/swaylock
BuildRequires:	bash-completion
BuildRequires:	cairo-devel
BuildRequires:	fish-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc
BuildRequires:	wayland-devel >= 1.20.0
BuildRequires:	wayland-protocols >= 1.25
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	wayland >= 1.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
swaylock is a screen locking utility for Wayland compositors. It is
compatible with any Wayland compositor which implements the following
Wayland protocols:

- wlr-layer-shell
- wlr-input-inhibitor
- xdg-output
- xdg-shell

%package -n bash-completion-swaylock
Summary:	Bash completion for swaylock
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-swaylock
Bash completion for swaylock.

%package -n fish-completion-swaylock
Summary:	fish-completion for swaylock
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-swaylock
fish-completion for swaylock.

%package -n zsh-completion-swaylock
Summary:	ZSH completion for swaylock
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-swaylock
ZSH completion for swaylock.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/%{name}
%attr(755,root,root) %{_bindir}/swaylock
%{_mandir}/man1/swaylock.1*

%files -n bash-completion-swaylock
%defattr(644,root,root,755)
%{bash_compdir}/swaylock

%files -n fish-completion-swaylock
%defattr(644,root,root,755)
%{fish_compdir}/swaylock.fish

%files -n zsh-completion-swaylock
%defattr(644,root,root,755)
%{zsh_compdir}/_swaylock

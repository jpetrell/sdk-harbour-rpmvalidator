# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-bad

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    A RPM to test the rpmvalidation.sh script which does not follow the rules
Version:    0.2
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-bad.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qt5-qtdeclarative-systeminfo
Requires:   nemo-qml-plugin-social-qt5
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(sailfishapp) >= 0.0.10
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  desktop-file-utils
Obsoletes:      harbour-good

%description
Short description of my SailfishOS Application


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# create some files in location we don't allow
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/
touch %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf

mkdir -p %{buildroot}/home/nemo/.conf/%{name}/
touch %{buildroot}/home/nemo/.conf/%{name}/%{name}.conf

touch %{buildroot}/%{_bindir}/%{name}-suid
touch %{buildroot}/%{_bindir}/%{name}-bin

touch %{buildroot}/%{_datadir}/%{name}/.DS_Store
touch %{buildroot}/%{_datadir}/%{name}/.some-tmp-vim-file.txt.swp
touch %{buildroot}/%{_datadir}/%{name}/some-backup-file.txt~
touch %{buildroot}/%{_datadir}/%{name}/.some-dot-backup-file.txt~

mkdir -p %{buildroot}/%{_datadir}/%{name}/.git
mkdir -p %{buildroot}/%{_datadir}/%{name}/.svn
mkdir -p %{buildroot}/%{_datadir}/%{name}/.hg
mkdir -p %{buildroot}/%{_datadir}/%{name}/.bzr
mkdir -p %{buildroot}/%{_datadir}/%{name}/.cvs

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%attr(4755,-,-) %{_bindir}/%{name}-suid
%attr(0755,-,-) %{_bindir}/%{name}-bin
%{_datadir}/%{name}/qml
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/.DS_Store
%{_datadir}/%{name}/.some-tmp-vim-file.txt.swp
%{_datadir}/%{name}/some-backup-file.txt~
%{_datadir}/%{name}/.some-dot-backup-file.txt~
%{_datadir}/%{name}/.git
%{_datadir}/%{name}/.svn
%{_datadir}/%{name}/.hg
%{_datadir}/%{name}/.bzr
%{_datadir}/%{name}/.cvs
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%attr(0644,nemo,nemo) /home/nemo/.conf/harbour-bad/%{name}.conf
%{_sysconfdir}/harbour-bad/%{name}.conf
# >> files
# << files

%post
/bin/true

%postun
/bin/true

%pre
/bin/true

%preun
/bin/true

%verifyscript
/bin/true


%define version  0.5.1
%define release  %mkrel 1 

Name:		     plasma-applet-stasks
Version:	     %{version}
Release:	     %{release}
License:	     GPLv2+
Url:		     https://www.kde.org/ 
Group:		     Graphical desktop/KDE
Source0:	     99739-stasks-0.5.1.tar.gz
Summary:         Plasmoid that allow to improve taskbar eye candy
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:   kdelibs4-devel
BuildRequires:   kdebase4-workspace-devel
Provides:        plasma-applet
Requires:        kdebase4-runtime

%description 
Plasmoid that allow to improve taskbar eye candy

%files 
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_stasks.so
%_kde_datadir/kde4/services/plasma-applet-stasks.desktop

#-----------------------------------------------------------------------------

%prep
%setup -q -n stasks-%version

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot

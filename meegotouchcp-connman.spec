# 
# Do not Edit! Generated by:
# spectacle version 0.18
# 
# >> macros
# << macros

Name:       meegotouchcp-connman
Summary:    MeegoTouchControlPanel wifi Plugin
Version:    0.0.11
Release:    1
Group:      System/GUI/Other
License:    Apache License
URL:        http://www.meego.com
Source0:    %{name}-%{version}.tar.bz2
Source100:  meegotouchcp-connman.yaml
Requires:   connman
Requires:   meego-handset-cpwifi-branding
BuildRequires:  pkgconfig(QtCore) >= 4.6.0
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtOpenGL)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(meegotouch)
BuildRequires:  pkgconfig(meegotouch-controlpanel)
BuildRequires:  doxygen


%description
This is a plugin for meegotouch-controlpanel that does wifi



%package libconnman-qt
Summary:    A library for accessing some of connman's functionality through qt
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libconnman-qt
This library is used by meegotouchcp-connman and others to work with connman


%package libconnman-qt-devel
Summary:    Development files for libconnman-qt
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description libconnman-qt-devel
This package contains the files necessary to develop
applications using libconnman-qt


%package branding-upsteam
Summary:    MeeGo wifi controlpanel applet theme files
License:    Restricted
Group:      System/GUI/Other
Requires:   %{name} = %{version}-%{release}
Provides:   meego-handset-cpwifi-branding

%description branding-upsteam
Theme assets for the MeeGo wifi control panel applet


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
export PATH=$PATH:/usr/lib/qt4/bin
qmake install_prefix=/usr
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
export INSTALL_ROOT=%{buildroot}
# << install pre
%make_install 

# >> install post
# << install post







%post libconnman-qt -p /sbin/ldconfig

%postun libconnman-qt -p /sbin/ldconfig







%files
%defattr(-,root,root,-)
%{_libdir}/duicontrolpanel/meegotouchcp-connman.desktop
%{_libdir}/duicontrolpanel/applets/libwifiapplet.so
# >> files
# << files


%files libconnman-qt
%defattr(-,root,root,-)
%{_libdir}/libconnman-qt.so.*
# >> files libconnman-qt
# << files libconnman-qt

%files libconnman-qt-devel
%defattr(-,root,root,-)
%{_usr}/include/manager.h
%{_usr}/include/service.h
%{_usr}/include/networkitemmodel.h
%{_usr}/include/networklistmodel.h
%{_usr}/include/commondbustypes.h
%{_usr}/include/technologybutton.h
%{_usr}/include/offlinebutton.h
%{_usr}/lib/pkgconfig/connman-qt.pc
%{_usr}/lib/libconnman-qt.so
# >> files libconnman-qt-devel
# << files libconnman-qt-devel

%files branding-upsteam
%defattr(-,root,root,-)
%{_datadir}/themes/base/meegotouch/duicontrolpanel/style/confirmremovepagestyle.css
%{_datadir}/themes/base/meegotouch/duicontrolpanel/style/listpagestyle.css
%{_datadir}/themes/base/meegotouch/duicontrolpanel/style/networkitemstyle.css
%{_datadir}/themes/base/meegotouch/duicontrolpanel/style/passwordpagestyle.css
%{_datadir}/themes/base/meegotouch/duicontrolpanel/style/mcp.css
%{_datadir}/themes/base/meegotouch/duicontrolpanel/style/libwifi.css
%{_datadir}/themes/base/meegotouch/duicontrolpanel/images/device-settings-bodytext-bg-dn.png
%{_datadir}/themes/base/meegotouch/duicontrolpanel/images/device-settings-bodytext-bg.png
%{_datadir}/themes/base/meegotouch/duicontrolpanel/images/device-settings-header-bg.png
%{_datadir}/themes/base/meegotouch/libwifiapplet/libwifiapplet.conf
# >> files branding-upsteam
# << files branding-upsteam


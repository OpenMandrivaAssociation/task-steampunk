Summary:	Metapackage for various Steampunk themes, widgets etc
Name:		task-steampunk
Version:	3.0
Release:	2
Group:		Graphical desktop/Other
License:	Creative Commons Attribution-ShareAlike
Url:		https://www.rosalinux.com
Requires:	%{name}-kde4
Requires:	plymouth-theme-steampunk
BuildArch:	noarch

%description
Metapackage for various Steampunk themes, widgets etc.

%files

#----------------------------------------------------------------------------

%package kde4
Summary:	Metapackage for various KDE4 Steampunk themes, widgets etc
Group:		Graphical desktop/KDE
Requires:	%{name}-kde4
Requires:	kde4-style-steampunk-aurorae
Requires:	kde4-style-steampunk-colors
Requires:	kde4-style-steampunk-cursors
Requires:	kde4-style-steampunk-kdm
Requires:	kde4-style-steampunk-ksplash
Requires:	kde4-style-steampunk-wallpapers
Requires:	kde4-style-steampunk-yakuake
Requires:	plasma-applet-steamtime
Requires:	plasma-applet-timekeeper
Requires:	plasma-desktoptheme-steampunk

%description kde4
Metapackage for various KDE4 Steampunk themes, widgets etc

%files kde4

#----------------------------------------------------------------------------

%prep

%build

%install


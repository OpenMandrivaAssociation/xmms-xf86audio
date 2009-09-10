%define name	xmms-xf86audio
%define summary	Enable XMMS control via XF86Audio keysyms (acme)
%define version	0.4.3
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
License:	GPL
Source0:	http://www.devin.com/xmms-xf86audio/download/%{name}-%{version}.tar.bz2
URL:		http://www.devin.com/xmms-xf86audio/
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libxmms-devel
Requires:	xmms

%description
This is xf86audio-xmms, a plugin for XMMS to enable control over XMMS playback
via the XF86Audio* keysyms, as produced by some keyboards with media-control
keys.

This plugin was written in response to demand from the users of Acme, GNOME2's
multimedia key manager.  While Acme manages the association of appropriate
keyboard scancodes with the media-control scancodes, it does not know how to
individually control the various media players.  Instead, it arranges the
mapping and expects those media players to listen for the XF86Audio keysyms.
I produced a patch against XMMS to do just that, but I'm also providing this
plugin to do the same job, since it's easier for end users than patching the
XMMS sources (indeed, this plugin's source is nearly identical to the patch).

%prep
rm -rf $RPM_BUILD_ROOT
%setup -n %{name}-%{version}
perl -p -i -e "s!PLUGINDIR=!PLUGINDIR=$RPM_BUILD_ROOT/!" Makefile

%build
%make

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README
/usr/lib/xmms/General/libxf86audio.so


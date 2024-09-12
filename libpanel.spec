%define api 1
%define major 0

# The name libpanel is taken by ncurses. While
# "%mklibname panel" clashes with a core package.
%define libname %mklibname panel-1
%define oldlibname %mklibname panel 1 0
%define giradwaitaname %mklibname panel-gir %{api}
%define devname %mklibname panel-1 -d

Name:		libpanel
Version:	1.7.1
Release:	1
Summary:	A dock/panel library for GTK 4
License:	LGPLv3
Group:		Development/GNOME and GTK+
URL:		https://gitlab.gnome.org/GNOME/libpanel/
Source0:	https://gitlab.gnome.org/GNOME/libpanel/-/archive/%{version}/libpanel-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	vala
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)

%description
Libpanel helps you create IDE-like applications using GTK 4 and libadwaita.
It has widgets for panels, docks, columns and grids of pages. Primarily, it's
design and implementation focus around GNOME Builder and Drafting projects.

#------------------------------------------------

%package -n %{libname}
Summary:	A GTK4/libadwaita library to develop IDE-like application
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
This package provides the shared library for libpanel, a library to
help with developing IDE using GTK4/GNOME.

#------------------------------------------------

%package -n %{giradwaitaname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{giradwaitaname}
GObject Introspection interface description for %{name}.

#------------------------------------------------

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/GNOME and GTK4
Requires:	%{libname} = %{version}-%{release}
Requires:	%{giradwaitaname} = %{version}-%{release}

%description -n	%{devname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson

%meson_build

%install
%meson_install

%find_lang %name

%files -n %{libname} -f %{name}.lang
%{_libdir}/libpanel-%{api}.so.%{api}*

%files -n %{giradwaitaname}
%{_libdir}/girepository-1.0/Panel-%{api}.typelib

%files -n %{devname}
%doc %{_datadir}/doc/panel-1.0/
%{_includedir}/libpanel-1
%{_libdir}/libpanel-1.so
%{_libdir}/pkgconfig/libpanel-1.pc
%{_datadir}/gir-1.0/Panel-1.gir
%{_datadir}/vala/vapi/libpanel-1.deps
%{_datadir}/vala/vapi/libpanel-1.vapi
%{_iconsdir}/hicolor/scalable/actions/panel-*

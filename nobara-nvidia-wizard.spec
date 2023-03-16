BuildArch:              noarch

Name:          nobara-nvidia-wizard
Version:       1.1
Release:       1%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
Summary:       Nobara's Nvidia Installation/Removal Wizard


URL:           https://github.com/CosmicFusion/cosmo-nvidia-wizard

Source0:        %{name}-%{version}.tar.gz

BuildRequires:	wget
Requires:      /usr/bin/bash
Requires:	python3
Requires:	python
Requires:	gtk3
Requires: 	glib2


# App Deps
Requires:	python3-gobject
Requires:	nobara-login
Requires:	nobara-login-config
Requires:	papirus-icon-theme

%install
tar -xf %{SOURCE0}
mv usr %{buildroot}/
mv etc %{buildroot}/
mkdir -p %{buildroot}/usr/share/licenses/nobara-nvidia-wizard
wget https://raw.githubusercontent.com/CosmicFusion/cosmo-nvidia-wizard/main/LICENSE.md -O %{buildroot}/usr/share/licenses/nobara-nvidia-wizard/LICENSE

%description
Nobara's Nvidia Installation/Removal Wizard	
%files
%attr(0644, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard"
%attr(0644, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/process.ui"
%attr(0644, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/main.ui"
%attr(0755, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/gpu-utils"
%attr(0755, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/end.sh"
%attr(0755, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/install.sh"
%attr(0755, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/remove.sh"
%attr(0755, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/main.py"
%attr(0755, root, root) "/etc/nobara/scripts/cosmo-nvidia-wizard/process.py"
%attr(0755, root, root) "/usr/bin/nobara-nvidia-wizard"
%attr(0644, root, root) "/usr/share/applications/nobara-nvidia-wizard.desktop"
%attr(0644, root, root) "/usr/share/licenses/nobara-nvidia-wizard/LICENSE"

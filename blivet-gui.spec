Summary: Tool for data storage configuration
Name: blivet-gui
Version: 2.1.11
Release: 1%{?dist}
Source0: http://github.com/storaged-project/blivet-gui/releases/download/%{version}/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Applications/System
BuildArch: noarch
URL: http://github.com/storaged-project/blivet-gui

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: blivet-gui-runtime = %{version}-%{release}

%description
Graphical (GTK) tool for manipulation and configuration of data storage
(disks, LVMs, RAIDs) based on blivet library.

%package -n blivet-gui-runtime
Summary: blivet-gui runtime

BuildRequires: python3-devel
BuildRequires: gettext >= 0.18.3
BuildRequires: python3-setuptools

Requires: python3
Requires: python3-gobject
Requires: gettext
Requires: python3-blivet >= 1:3.1.2
Requires: gtk3
Requires: PolicyKit-authentication-agent
Requires: python3-pid
Requires: libreport
Requires: adwaita-icon-theme

%description -n blivet-gui-runtime
This package provides a blivet-gui runtime for applications that want to use
blivet-gui without actually installing the application itself.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

desktop-file-validate %{buildroot}/%{_datadir}/applications/blivet-gui.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/blivet-gui.appdata.xml

mkdir -p %{buildroot}/%{_localstatedir}/log/blivet-gui

%find_lang %{name}

%files -n blivet-gui
%{_datadir}/applications/blivet-gui.desktop
%{_datadir}/appdata/blivet-gui.appdata.xml

%files -n blivet-gui-runtime -f %{name}.lang
%{_mandir}/man1/blivet-gui.1*
%{python3_sitelib}/*
%{_datadir}/polkit-1/actions/org.fedoraproject.pkexec.blivet-gui.policy
%{_datadir}/icons/hicolor/*/apps/blivet-gui.png
%{_datadir}/blivet-gui
%{_bindir}/blivet-gui
%{_bindir}/blivet-gui-daemon
%{_localstatedir}/log/blivet-gui
%{_sysconfdir}/libreport/events.d/blivet-gui_event.conf

%changelog
* St čec 31 2019 Vojtech Trefny <vtrefny@redhat.com> - 2.1.11-1
- Create only one tag per release (vtrefny)
- Update README (vtrefny)
- Check if action still exists before trying to remove it (#1706378) (vtrefny)
- Correctly display LUKS with integrity (#1729888) (vtrefny)
- Use 'direct' device property to (dis)allow mountpoint selection (vtrefny)
- Do not allow to set mountpoints for devices with children (#1667644) (vtrefny)
- Fix return type of BlivetUtils.get_disks (#1658893) (vtrefny)

* Wed Dec 12 2018 Vojtech Trefny <vtrefny@redhat.com> - 2.1.10-1
- Use 'pycodestyle' instead of 'pep8' (vtrefny)
- Enable name validity checks in AddDialog (#1649364) (vtrefny)
- Fix suggesting names for btrfs subvolumes (#1648631) (vtrefny)
- Do not show MD arrays in disks section (vtrefny)
- Ignore PEP8 W504 warning ("line break after binary operator") (vtrefny)
- Sync spec with downstream (vtrefny)

* Wed Sep 26 2018 Vojtech Trefny <vtrefny@redhat.com> - 2.1.9-1
- Add some extra parameters to the lsblk in log (vtrefny)
- Fix crash when adding device with same min and max size (#1623189) (vtrefny)
- Limit partition max size based on disklabel limits (#1623659) (vtrefny)
- Ignore pylint 'no-value-for-parameter' warning (vtrefny)
- Fix 'assignment-from-no-return' error discovered by pylint (vtrefny)
- Removed copyright year (code)
- Ignore pylint error for "preexec_fn" (vtrefny)
- Ignore pylint false positives for Gtk.ListStore (vtrefny)
- Set _supported_filesystems in BlivetGUIAnaconda init (awilliam)
- Sync spec with downstream (vtrefny)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.8-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.8-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Vojtech Trefny <vtrefny@redhat.com> - 2.1.8-2
- Set _supported_filesystems in BlivetGUIAnaconda init (awilliam)

* Mon Jan 15 2018 Vojtech Trefny <vtrefny@redhat.com> - 2.1.8-1
- Do not allow to format large devices to biosboot (#1532253) (vtrefny)
- Remove unused 'socket' module import (vtrefny)
- Don't pass 'hostname' kwarg to suggest_container_name (#1528103) (awilliam)
- Sync spec file with downstream (vtrefny)
- Use better message when blivet-gui is already running (vtrefny)
- Use constants instead of strings for init errors communication (vtrefny)
- Fix few pep8 violations found by pep8 on Debian (vtrefny)
- Try to locate pep8 executable in pep8 target (vtrefny)
- Do not use RPM to check if Zanata client is installed (vtrefny)
- Use ansible for test dependencies installation (vtrefny)
- Fix opening raw LUKS format (#1519049) (vtrefny)
- Get supported filesystems in the 'backend' process (vtrefny)
- Fix ignored pylint directory (vtrefny)
- Add pylint log files to .gitignore (vtrefny)
- Bump required version for blivet to 3.0 (vtrefny)
- Use new method for getting supported disklabels (vtrefny)
- Use new method to configure blivet (vtrefny)
- Use argparse module instead of deprecated optparse (vtrefny)
- Update information about running tests in CONTRIBUTING.md (vtrefny)
- Add targetcli to test dependencies (vtrefny)

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.7-5
- Remove obsolete scriptlets

* Tue Jan 02 2018 Vojtech Trefny <vtrefny@redhat.com> - 2.1.7-4
- Don't pass 'hostname' kwarg to suggest_container_name (#1528103)
- Remove unused 'socket' module import

* Tue Dec 19 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.7-3
- Fix python-setuptools dependency

* Mon Nov 27 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.7-2
- Allow running with new Blivet 3.0

* Tue Sep 19 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.7-1
- Allow changing partition table (disklabel) (vtrefny)
- Do not use Gtk.Label.set_align it is deprecated (vtrefny)
- Do not use Gtk.Widget.size_request() it is deprecated (vtrefny)
- Do not use positional argument with Gtk initializers (vtrefny)
- Do not use Gtk.Table it is deprecated (vtrefny)
- Do not specify title and buttons in Gtk.Dialog initializer (vtrefny)
- AddDialog: Fix displaying filesystem label entry (vtrefny)
- Makefile: Add a separate targets for gui and utils tests (vtrefny)
- Add a basic test suite for testing BlivetUtils class (vtrefny)
- Sync spec with downstream (vtrefny)
- Allow running BlivetUtils on only subset of disks (vtrefny)

* Fri Aug 18 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.6-1
- Add a basic "high level" log for BlivetUtils (vtrefny)
- Redirect stdout to stderr for blivet-gui-daemon (vtrefny)
- Do not try to teardown luks devices before removing (#1466940) (vtrefny)
- Fix displaying resize dialog for non-resizable devices (#1473350) (vtrefny)
- Fix getting parents for loop devices (#1474483) (vtrefny)
- Fix ABRT/libreport config for blivet-gui (vtrefny)
- Update the upstream git URL for blivet-gui and blivet (vtrefny)
- Split blivet-gui package into "blivet-gui" and "blivet-gui-runtime" (vtrefny)
- Require "PolicyKit-authentication-agent" instead of "polkit-gnome" (vtrefny)
- New version of help for blivet-gui (vtrefny)
- Add more information to the README and a new readme for contributors (vtrefny)
- Add make targets for building SRPM and RPM packages (vtrefny)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.5-2
- Split blivet-gui package into "blivet-gui" and "blivet-gui-runtime" (vtrefny)

* Tue Jun 20 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.5-1
- Fix reusing LUKS devices in Anaconda (#1462071) (vtrefny)
- Make the device toolbar look more "toolbarish" (#1456011) (vtrefny)
- Use "is_disk" to check if device is disk (#1457163) (vtrefny)
- Fix displaying encrypted logical partitions (vtrefny)
- Run "update_size_info" for luks devices (vtrefny)
- pylint: fix different keyword arguments for "connect" method (vtrefny)
- Ignore pylint error "not-context-manager" for locks (vtrefny)

* Tue May 30 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.4-2
- Run "update_size_info" for luks devices (vtrefny)
- Fix displaying encrypted logical partitions  (vtrefny)

* Fri May 05 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.4-1
- Do not try to set both size request and auto-expand for Gtk.Scale (vtrefny)
- Use Gtk.Menu.popup_at_pointer when showing context menu (vtrefny)
- Allow keyboard shortcuts configuration from Anaconda (#1439608) (vtrefny)
- Allow "refreshing" UI from Anaconda when spoke is visible (vtrefny)
- Hide 'protected' devices in installer mode (vtrefny)
- Update Zanata branch name (vtrefny)

* Thu Apr 27 2017 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.3-2
- Use python3-gobject not pygobject3

* Mon Apr 24 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.3-1
- Merge pull request #57 from vojtechtrefny/master_partition-ordering (vtrefny)
- Preserve ordering when adding partitions (#1439591) (vtrefny)
- Merge pull request #55 from vojtechtrefny/master_test-day-fixes-3 (vtrefny)
- Fix crash when there are no "real" actions to perform (vtrefny)
- Fix displaying of non-existing encrypted devices (#1439576) (vtrefny)
- Allow deleting parents when deleting VG/RAID/Btrfs volume (#1439661) (vtrefny)
- SizeChooser: Change default and available size units (#1440369) (vtrefny)
- Allow creating encrypted MD arrays (#1440392) (vtrefny)
- Allow setting mountpoint for all mountable filesystems (#1440372) (vtrefny)
- Allow creating encrypted LVs (#1439651) (vtrefny)

* Tue Apr 11 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.2-1
- Merge pull request #52 from vojtechtrefny/master_test-day-fixes-2 (vtrefny)
- Fix devices allowed to add to a PV on an mdarray (#1440804) (vtrefny)
- Do not allow setting mountpoint for extended partitions (vtrefny)
- Merge pull request #48 from vojtechtrefny/master_test-day-fixes (vtrefny)
- Show previously selected mountpoint when editting a device (#1439525) (vtrefny)
- Fix decorations of some dialogs in installer mode (vtrefny)
- Add 'prepboot' and 'biosboot' to supported filesystems (#1439538) (vtrefny)
- Add a config class for blivet-gui (#1439581) (vtrefny)
- Allow changing format for MD arrays (#1439592) (vtrefny)
- Do not use 'dim-label' style for labels in dialogs (#1439529) (vtrefny)
- Add tooltips for actions toolbar (#1439563) (vtrefny)
- Merge pull request #47 from vojtechtrefny/master_fix-reuse-luks (vtrefny)
- Do not try to check mountpoint for unmountable formats (#1439108) (vtrefny)
- Merge pull request #46 from offthewoll/master (vtrefny)
- Correct "proccessing" to "processing" (aviwoll)
- Corrected "proccessing" to "processing" (aviwoll)
- Merge pull request #44 from vojtechtrefny/master_installer-bugs (vtrefny)
- Do not allow to set mountpoint for nonexisting LVM snapshots (vtrefny)
- Fix error when creating LVM PV (vtrefny)

* Tue Mar 14 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.1-1
- Merge pull request #43 from vojtechtrefny/master_fix-lvmsnapshot-free (vtrefny)
- AddDialog: Use 'free_space' instead of 'free' for VGs free space (vtrefny)

* Mon Feb 27 2017 Vojtech Trefny <vtrefny@redhat.com> - 2.1.0-1
- Merge pull request #42 from vojtechtrefny/master_installer-mode4 (vtrefny)
- Allow setting same mountpoint when editting a device (vtrefny)
- Completely stop using PVs as parents when adding LVs (vtrefny)
- AddDialog: Do not show advanced options for LVs (vtrefny)
- Merge pull request #41 from vojtechtrefny/master_handle-user-change (vtrefny)
- Add a special method for handling changes made by user (vtrefny)
- Merge pull request #40 from vojtechtrefny/master_action-label-fix (vtrefny)
- Use Gtk.Button for showing number of scheduled actions (vtrefny)
- Merge pull request #39 from vojtechtrefny/master_raid-chooser (vtrefny)
- Hotfix for maximum size of LVs (vtrefny)
- Temporarily disable LVM RAID (vtrefny)
- AddDialog: Use BTRFS._min_size instead 256 MiB (vtrefny)
- Allow creating LVM/Btrfs only when selected free space is big enough (vtrefny)
- Temporarily remove support for cache area (vtrefny)
- Reworked SizeArea and size widgets for AddDialog (vtrefny)
- Do not display a special raid chooser for LVs (vtrefny)
- AddDialog: Create a standalone RaidChooser widget (vtrefny)
- Merge pull request #37 from vojtechtrefny/master_installer-mode3 (vtrefny)
- AddDialog: Change label for selecting parents (vtrefny)
- Allow setting label when changing format of device (vtrefny)
- AddDialog: add scrollbars if the dialog is too big (vtrefny)
- Add adwaita-icon-theme to dependencies (vtrefny)
- Fix some MagicMock related exceptions in tests (vtrefny)
- AddDialog: Allow setting filesystem label for mdraid (vtrefny)
- AddDialog: Remove separate option to put PV on an MD RAID (vtrefny)
- Fix creating format for new md arrays (vtrefny)
- AddDialog: Allow setting filesystem label for LVs (vtrefny)
- Do not allow creating snapshots of non-existing LVs (vtrefny)
- AddDialog: Change description for 'LVM Storage' to 'LVM VG' (vtrefny)
- Use 'better' icon for the edit menu (vtrefny)
- Use accelerators in custom dialogs (vtrefny)
- Allow running ShowActionsDialog without decoration in installer_mode (vtrefny)
- Do not show number of pending actions in installer mode (vtrefny)
- Allow 'reusing' actions in installer mode (vtrefny)
- Merge pull request #36 from vojtechtrefny/master_installer-mode2 (vtrefny)
- Allow running ShowActionsDialog without decoration in installer_mode (vtrefny)
- Do not show number of pending actions in installer mode (vtrefny)
- Allow 'reusing' actions in installer mode (vtrefny)
- Merge pull request #35 from vojtechtrefny/master_edit-mountpoint (vtrefny)
- Use Gtk.Window in AddDialogTest instead of Mock (vtrefny)
- Add dialog for setting mountpoint in installer mode (vtrefny)
- Allow setting mountpoint when formatting existing device (vtrefny)
- Merge pull request #34 from vojtechtrefny/master_installer-mode (vtrefny)
- Fix fs selection in AddDialog test (vtrefny)
- Allow to run ResizeDialog and FormatDialog without decoration (vtrefny)
- Prefix blivet-gui CSS styles to avoid name conflicts (vtrefny)
- Move CSS styling to BlivetGUI class (vtrefny)
- Allow to initialize blivet-gui during refresh in installer mode (vtrefny)
- Do not create list of devices and actions in constructor (vtrefny)
- Fix creating format with label and mountpoints (vtrefny)
- Get list of currently used mountpoints when adding new device (vtrefny)
- AddDialog: don't show decoration on message dialogs in installer mode (vtrefny)
- AddDialog: center and don't show decorations in installer mode (vtrefny)
- Add custom method to run dialogs (vtrefny)
- Run message dialogs with lightbox in installer mode (vtrefny)
- Allow showing message dialogs without decoration (vtrefny)
- Use show_dialog methods instead of creating dialogs manually (vtrefny)
- Change 'ActionsToolbar' to a standalone widget (vtrefny)
- Expand partitions list widget vertically (vtrefny)
- Add some basic classes for running blivet-gui in Anaconda (vtrefny)
- Stop predenting we need auth token for client-server communication (vtrefny)
- Do not create client instance in BlivetGUI class (vtrefny)
- Do not allow ignoring exceptions from BlivetGUIClient (vtrefny)
- Raise custom exception in BlivetGUIClient for connection errors (vtrefny)
- Remove kickstart mode from blivet-gui (vtrefny)
- Merge branch 'f25-branch' (vtrefny)
- Merge pull request #33 from vojtechtrefny/f25-branch_ui-fixes (vtrefny)
- Fix showing traceback in exception dialog (vtrefny)
- Add glade temp files to gitignore (vtrefny)
- Show scrollbars in visualization (vtrefny)
- Fix position of main menu (vtrefny)
- SizeChooser: Fix size of size SpinButton (vtrefny)
- Unmount devices from the GUI (vtrefny)
- Catch exceptions when calling methods on proxy objects (vtrefny)
- Allow calling methods on proxy objects from client (vtrefny)
- Merge branch 'f25-branch' into f26-branch (vtrefny)
- Bump zanata branch version (vtrefny)

* Mon Dec 12 2016 Vojtech Trefny <vtrefny@redhat.com> - 2.0.2-1
- Merge pull request #32 from vojtechtrefny/f25-branch_exception-handler (vtrefny)
- Add custom exception handler for blivet-gui (vtrefny)
- Merge pull request #31 from vojtechtrefny/f25-branch_thin-snapshots (vtrefny)
- fix typo (chris)
- Fix typo lvmlv device info (vtrefny)
- Fix visualisation of thin snapshots (vtrefny)
- Add support for creating lvm thinsnapshosts (vtrefny)
- Merge pull request #29 from vojtechtrefny/f25-branch_fix-xvfb (vtrefny)
- Fix floating point exception when running test using xvfb-run (vtrefny)
- Merge pull request #28 from vojtechtrefny/f25-branch_appdata-upgrade (vtrefny)
- Update appdata.xml to new version (vtrefny)
- New up-to-date screenshots for AppData (vtrefny)
- New zanata branch (vtrefny)

* Thu Aug 04 2016 Vojtech Trefny <vtrefny@redhat.com> - 2.0.1-1
- Merge pull request #27 from vojtechtrefny/f25-branch_meh-remove (vtrefny)
- Add config for abrt to attach blivet logs to reports (vtrefny)
- Simplify logging (vtrefny)
- Don't use python-meh (vtrefny)

* Mon Jul 18 2016 Vojtech Trefny <vtrefny@redhat.com> - 2.0.0-1
- Remove redundant version constants (vtrefny)
- Merge pull request #24 from vojtechtrefny/master_docs (vtrefny)
- Fix few typos in docstrings (vtrefny)
- Add autogenerated doc files to .gitignore (vtrefny)
- Add basic introduction to blivet-gui developer documentation (vtrefny)
- Remove unused .rst documentation files (vtrefny)
- Fix Makefile and configuration for documentation (vtrefny)
- Merge pull request #23 from vojtechtrefny/master_constants (vtrefny)
- Use blivet constants instead of "magic" numbers in AddDialog (vtrefny)
- Merge pull request #22 from vojtechtrefny/master-btrfs_in_vg2 (vtrefny)
- Return supported filesystems as objects not just types (vtrefny)
- Allow using btrfs as format for all devices (vtrefny)
- AddDialog: Remove special type for lvmpv, allow lvmpv format (vtrefny)

* Mon May 23 2016 Vojtech Trefny <vtrefny@redhat.com> - 1.3.1-1
- Merge pull request #21 from vojtechtrefny/master-split_edit (vtrefny)
- Merge pull request #19 from dashea/translation-canary (vtrefny)
- Add translation context for "Format" strings (vtrefny)
- Add LVMVG edit option to edit menu (vtrefny)
- Remove EditDialogTest (vtrefny)
- BlivetGUI: Use new resize and format dialogs instead of edit dialog (vtrefny)
- Add new submenus for "edit" option in toolbar and popup menu (vtrefny)
- Replace PartitionEditDialog by ResizeDialog and FormatDialog (vtrefny)
- BlivetUtils: Add new public methods for device resize and format (vtrefny)
- Merge pull request #20 from vojtechtrefny/master-reset_progress (vtrefny)
- Add progress dialog for storage reload (vtrefny)
- Remove markup from translatable strings where possible. (dshea)
- Use the translation-canary tests (dshea)
- Do not use intltool. (dshea)
- Add P_ to the xgettext keywords. (dshea)
- Always use setup.py to generate the source archive. (dshea)
- Merge commit 'e8a62de12f347962c7c9c71e4562f42a2618fce7' as 'translation-canary' (dshea)
- Squashed 'translation-canary/' content from commit edda4ea (dshea)
- Merge pull request #18 from vojtechtrefny/master-chunk_size (vtrefny)
- Add test for chunk size (vtrefny)
- Add chunk support for mdraid creation (vtrefny)
- Merge pull request #17 from vojtechtrefny/master-none_format (vtrefny)
- Allow "none" as format when adding/editting devices (vtrefny)
- Remove communication log (vtrefny)
- Allow ignoring disks with corrupted/unknown disklabels (vtrefny)
- New version 1.3.0 (vtrefny)

* Tue Apr 12 2016 Vojtech Trefny <vtrefny@redhat.com> - 1.3.0
- Fix visualization CSS styles (vtrefny@redhat.com)
- Fix visualization of group devices inside VG (#1326175) (vtrefny@redhat.com)
- Translations moved from translate.zanata.org to fedora.zanata.org (vtrefny@redhat.com)
- Remove gnome-icon-theme from requires (vtrefny@redhat.com)
- Fix adding a new device into an existing mdarray (vtrefny@redhat.com)
- Add make ci target and test dependencies (vtrefny@redhat.com)
- Fix methods for locating CSS and UI files (vtrefny@redhat.com)
- SizeChooserAreaTest: Libbytesize support related fixes (vtrefny@redhat.com)
- Use property instead of setter method for luks decrypt passphrase (vtrefny@redhat.com)
- CacheArea: Fix displaying parent name in pv chooser (vtrefny@redhat.com)
- Pylint/PEP8 fixes, fix AddDialog test cases (vtrefny@redhat.com)
- Skip ListPartitionsTest when X server is not available (vtrefny@redhat.com)
- Remove remaining user documentation related code (vtrefny@redhat.com)
- AddDialog: do not allow to set size when adding vg to pvs (vtrefny@redhat.com)
- Do not try to display (meta)data level for btrfs subvolumes (vtrefny@redhat.com)
- Fix adding lvm thinpools (vtrefny@redhat.com)
- Libbytesize support changes (vtrefny@redhat.com)
- Set communication socket to be owned by user not root (vtrefny@redhat.com)
- Remove obsolte/unused methods from BlivetUtils (vtrefny@redhat.com)
- Fix editting volume groups (vtrefny@redhat.com)
- Pylint and PEP8 fixes (vtrefny@redhat.com)
- Always remove format when removing device (vtrefny@redhat.com)
- Hide second raid chooser for non LVs (vtrefny@redhat.com)
- LVM RAID support -- utils part (vtrefny@redhat.com)
- SizeArea,AddDialog -- LVM RAID support, part 2 (vtrefny@redhat.com)
- Temporary disable device name validation (vtrefny@redhat.com)
- Move supported fs types to EditDialog (vtrefny@redhat.com)
- Add RAID chooser into ParentArea when adding new LV (vtrefny@redhat.com)
- Do not display parent size chooser for LVs (vtrefny@redhat.com)
- AddLabelDialog: Fix available disklabels (vtrefny@redhat.com)
- SizeArea -- RAID support, part 1 (vtrefny@redhat.com)
- Raise exception in client when accesing blivet attribute failed (vtrefny@redhat.com)
- AddDialog: Do not offer full PVs as possible parents for LVs (vtrefny@redhat.com)
- AddDialog: Switch to single SizeArea model (vtrefny@redhat.com)
- Fix ParentArea for non-LVM parents (vtrefny@redhat.com)
- AddDialog: Fix checking for lvmlv and lvmthinlv device types (vtrefny@redhat.com)
- AddDialog: Change _get_selected_device_type to property (vtrefny@redhat.com)
- Remove support for adding btrfs as a disklabel (vtrefny@redhat.com)
- Refactor add_partition method (vtrefny@redhat.com)
- Fix passing selected and free devices to AddDialog (vtrefny@redhat.com)
- Move supported types (fs, raid levels, disklabels) to AddDialog (vtrefny@redhat.com)
- SizeChooser: Update main size chooser when changing size for parents (vtrefny@redhat.com)
- SizeChooser: Add ParentArea for parents size selection (vtrefny@redhat.com)
- Merge branch 'master' of github.com:rhinstaller/blivet-gui (vtrefny@redhat.com)
- Merge pull request #14 from dashea/eintr (vtrefny@redhat.com)
- Remove the removal of the eintr checker, which has been removed (dshea@redhat.com)
- Use new_lv instead of LVM objects constructors (vtrefny@redhat.com)
- Fix adding devices on DASD and zFCP disks (#1305495) (vtrefny@redhat.com)
- Make LUKS encrypted partitions resizable (vtrefny@redhat.com)
- Use list of children for devices instead of get_children (vtrefny@redhat.com)
- Fix visualization of raw format LUKS devices (#1288943) (vtrefny@redhat.com)
- Size area refactoring (vtrefny@redhat.com)
- Fix updateSizeInfo on BIOSBoot partitions (#1286616) (vtrefny@redhat.com)
- Add cache info to device info dialog (vtrefny@redhat.com)
- Reimplement size area using Glade (vtrefny@redhat.com)
- LVM cache support -- utils part (vtrefny@redhat.com)
- LVM cache support -- UI part (vtrefny@redhat.com)
- Allow nested ProxyDataContainer in server-cleint communication (vtrefny@redhat.com)
- Add tests for recently found bugs (vtrefny@redhat.com)
- Fix allow creating lvm snapshots (vtrefny@redhat.com)
- AddDialog: Fix min size for vg children (vtrefny@redhat.com)
- AddDialog: Fix parent type when adding LMV LV (vtrefny@redhat.com)
- Don't allow adding btrfs volume to devices smaller than 256 MiB (vtrefny@redhat.com)
- Do not call get_children more than necessary (vtrefny@redhat.com)
- New version 1.2 (vtrefny@redhat.com)

* Wed Nov 18 2015 Vojtech Trefny <vtrefny@redhat.com> - 1.2-1
- Add PEP8 compliance check to 'make check' (vtrefny)
- Fix PEP8 violations. (vtrefny)
- Remove some obsolete/debug prints and imports (vtrefny)
- Catch blivet.errors.LUKSError instead of BlockDev.CryptoError (vtrefny)
- Add test for adding device to partitions list (vtrefny)
- EditDialog: add test for formatting extended partitions (vtrefny)
- Add test for communication.proxy_utils (vtrefny)
- Fix BlivetProxyObjectTest (vtrefny)
- Add tests for new FreeSpaceDevice features (vtrefny)
- Fix check for allowed max partitions count (vtrefny)
- AddDialog: fix displaying parents for MDArray PVs (vtrefny)
- Fix 'disk' attribute for FreeSpaceDevices (vtrefny)
- Visualization: add protected icon to protected devices (vtrefny)
- Do not allow deleting/editting protected devices (vtrefny)
- Remove pocketlint from BuildRequires (vtrefny)
- Remove 'check' from 'make release' target (vtrefny)
- Run mkfs.ntfs with '-f' option (fast formatting) (#1253013) (vtrefny)
- Add support for creating NTFS format (vtrefny)
- Fix visualisation of group devices with 0 size (#1275815) (vtrefny)
- Visualization: do not allocate remaing space when there is no space left (vtrefny)
- Fix device visualisation with high contrast theme (vtrefny)
- Properly catch and reraise exceptions from BlivetUtils initialization (vtrefny)
- Fix tests to work with localization (vtrefny)
- Add make coverage target (vtrefny)
- Add loading window when starting blivet-gui (vtrefny)
- Fix make po-pull/push target (vtrefny)
- Set translation domain for glade files (vtrefny)

* Wed Sep 23 2015 Vojtech Trefny <vtrefny@redhat.com> - 1.1-1
- Fix make bumpver to work with 1.x versions (vtrefny)
- Fix finished actions visualisation in processing window (vtrefny)
- Remove MANIFEST file from git (vtrefny)
- Fix visualization for non-existing encrypted partitions (vtrefny)
- Add "local" target to Makefile (vtrefny)
- Use zanata-python-client instead of zanata-cli (vtrefny)
- AddDialog: Always display at least one size area (vtrefny)
- Fix max size of KickstartSelectDevicesDialog (vtrefny)
- Fix dialogs with actions list height (vtrefny)
- Allow shrinking extended partitions (vtrefny)
- Fix bug description when reporting using python-meh (vtrefny)
- AddDialog: Add a second passphrase entry for verification (vtrefny)
- Remove obsolete test run mode from BlivetUtils (vtrefny)
- Allow deleting of active formats in kickstart mode (vtrefny)

* Wed Sep 02 2015 Vojtech Trefny <vtrefny@redhat.com> - 1.0-1
- Update man page (vtrefny)
- Add AppData validation to spec file (vtrefny)
- Add tags to desktop file (vtrefny)
- Add AppData for blivet-gui (vtrefny)
- Fix few typos and grammar in strings (vtrefny)
- Add first test for ListPartitions (vtrefny)
- Fix adding LVM Thin LVs (vtrefny)
- Remove help from package (vtrefny)
- ListParents: fix checking parents for logical partitions (vtrefny)
- Add icons to %%files in spec file (vtrefny)
- DeviceInfoDialog: add special info for mdarrays (vtrefny)
- Fix maximal size for thinpools (vtrefny)
- Add desktop icon for blivet-gui (vtrefny)
- Selection unit tests for AddDialog (vtrefny)
- More tests for AddDialog and PartitionEditDialog (vtrefny)
- Fix check_mountpoint method (vtrefny)
- Do not run unittests without X server (vtrefny)
- More unit tests for AddDialog (vtrefny)
- ProcessingWindow: Center on blivet-gui main window. (vtrefny)
- PhysicalView: Double click to select parent device (vtrefny)
- Fix logical and physical view for mdarrays with lvm (vtrefny)
- Fix adding lvmvg to MD raid (vtrefny)
- AddDialog: Fix minimal size when changing device type (vtrefny)
- AddDialog: Delete content of Gtk.Entry when hiding it (vtrefny)
- Fix physical view for devices with logical partitions as parents (vtrefny)
- Fix spelling in isUninitializedDisk method name (vtrefny)
- Add unittest for AddDialog (vtrefny)
- Add test for fslabel validity check (vtrefny)
- AddDialog, PartitionEditDialog: Add fslabel validity check (#1236112) (vtrefny)
- Do not allow to add lvmvg to lvmpv with insufficient size (vtrefny)
- Fix allowed pesizes for lvmvg in AddDialog (vtrefny)
- Allow resizing of extended partitions (vtrefny)
- Reimplement ActionsMenu using Glade (vtrefny)
- Add test for ListActions (vtrefny)
- Fix visualization for logical group devices (vtrefny)
- In kickstart mode show future mountpoints in partition list (vtrefny)
- EditDialog: Add mountpoint validity check (vtrefny)
- AddDialog: Fix mountpoint validation (vtrefny)
- Fix actions dialogs width (vtrefny)
- AddDialog: Update min size limit for encrypted devices (vtrefny)
- AddDialog: Update min size limit based on selected pesize (vtrefny)
- AddDialog: Add method to update size limits (vtrefny)
- AddDialog: allow empty device name (vtrefny)
- AddDialog: Do not offer PESize larger than free space available (vtrefny)
- Fix visualization for live usb deviceFix visualization for live usb devicess (vtrefny)
- Fix free space regions for unitialized disks (vtrefny)
- Do not refresh views after cancelling delete action (vtrefny)
- Fix displaying number of pending actions after applying them (vtrefny)
- Quit 'nicely' on Ctrl-C (vtrefny)
- Add test for fslabel in PartitionEditDialog (vtrefny)
- PartitionEditDialog: allow setting fslabel when changing format (vtrefny)
- Add test for FreeSpaceDevice (vtrefny)
- Add name validation for devices in AddDialog (vtrefny)
- Fix displaying device info icons (vtrefny)
- Add ID and format to FreeSpaceDevice and RawFormatDevice (vtrefny)
- Preselect filesystem type for add/edit dialog (vtrefny)
- Visualization size corresponding with device size (vtrefny)
- Don't allow to add more than 4 partitions on msdos disklabels (vtrefny)
- Call blivet.partitioning.getFreeRegions with align=True (vtrefny)
- Move i18n definitions to one file (vtrefny)
- Display number of pending actions in statusbar (vtrefny)
- Add information icons to devices in logical view (vtrefny)
- Switch to device logical view by double-clicking on it (vtrefny)
- First unittest for blivet_utils (vtrefny)
- Remove python.six, python3 only support now (vtrefny)
- Fix visualization update after resizing device (vtrefny)
- Add device size to visualization (vtrefny)
- Hide physical view for disks (vtrefny)
- Use python3-pid for pidfile creation (vtrefny)
- New version 0.3.6 (vtrefny)

* Thu Aug 06 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.3.6-1
- Fix visualisation for extended partitions with single child (vtrefny)
- Fix parent visualization for encrypted LVMs (vtrefny)
- Allow adding new VG to an empty LVMPV (vtrefny)
- Remove obsolete definiton of locate_ui_file method (vtrefny)
- Do not allow displaying device info for raw format devices (vtrefny)
- Remove old visualization files (vtrefny)
- Display context menu for logical view visualization (vtrefny)
- New UI, part 4: Physical View -- parents visualization (vtrefny)
- Fix visualization for raw format devices (vtrefny)
- Tweak device visualisation in logical view using CSS (vtrefny)
- Move various GUI helper functions into one file (vtrefny)
- New UI, part 3: New device visualisation for logical view (vtrefny)
- BlivetUtilsServer: quit when recieve empty message (vtrefny)
- Renaming few files and folders (vtrefny)

* Wed Jul 29 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.3.5-1
- Fix displaying btrfs as a disklabel (vtrefny)
- Fix adding btrfs as a disklabel (vtrefny)
- Small UI fixes (vtrefny)
- Few stylistic fixes (vtrefny)
- New UI, part 2: listing of device children in logical view (vtrefny)
- Catch AttirbuteErrors during remote utils calls (vtrefny)
- PartitionEditDialog: Do not offer formats that are not supported (vtrefny)
- Fix context menu for partitions list (vtrefny)
- Add test for PartitionEditDialog (vtrefny)
- Fix AddDialog tests (vtrefny)
- AddDialog: Do not offer formats that are not supported (vtrefny)
- Display MDarrays and Btrfs Volumes in device list (vtrefny)
- Remove custom method to detect extended partition on disk (vtrefny)
- Allow displaying disks withou disklabel in AddDialog (vtrefny)
- Fix creating extended partitions (vtrefny)
- Remove unused import (vtrefny)
- Fix pocketlint settings (vtrefny)
- Do not allow adding snapshot when there is not enough free space (vtrefny)
- Fix converting ProxyDataContainer to IDs (vtrefny)
- Move all tests to one folder (vtrefny)
- Add tests to test server-client functions (vtrefny)
- Fix catching exceptions in client-server communication (vtrefny)
- BlivetGUIClient: fix sending ProxyDataContainer (vtrefny)
- New version 0.3.4 (vtrefny)

* Thu Jul 16 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.3.4-1
- Pylint fixes (vtrefny)
- Use pocketlint for blivet-gui (vtrefny)
- Recreate list of actions using Glade (vtrefny)
- Completely separate toolbar for blivet actions and for device actions (vtrefny)
- Add device information button to DeviceToolbar (vtrefny)
- Separate ActionsToolbar and DeviceToolbar (vtrefny)
- New UI, part 1 (vtrefny)
- Use gi.require_version when importing from gi.repository (vtrefny)
- Few pylint overrides and fixes (vtrefny)
- Reimplement AddDisklabelDialog using Glade (vtrefny)
- Add unittest to test AdvancedOptions from AddDialog (vtrefny)
- Add "test" rule to Makefile (vtrefny)
- Add unittest to test SizeChooserArea from AddDialog (vtrefny)
- Move SizeChooserArea to own module (vtrefny)
- Fix name suggestion for thinlvs (vtrefny)
- Fix progress bar fraction during applying changes (vtrefny)
- Do not allow editing of non-existing LVM VGs (vtrefny)
- EditDialog: Do not allow select "None" as format (vtrefny)
- Fix removing parents for encrypted devices and btrfs volumes (vtrefny)
- Delete existing partition table when adding btrfs as a disklabel (vtrefny)
- Align target size before resizing partitions (#1207798) (vtrefny)
- Fix device visualisation selection after window resize (vtrefny)
- Allow adding encrypted logical partitions (vtrefny)
- DeviceInfoDialog: auto-ellipsize long labels (vtrefny)
- Do not display disks without disklabel in AddDialog (vtrefny)
- Move exception catching to add_device method (vtrefny)
- Do not allow adding new LV to an incomplete VG (vtrefny)
- Do not allow to create an extended partition on GPT disks (vtrefny)

* Thu May 21 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.3.3-1
- Require newest blivet (python-blivet 1.4) (vtrefny)
- Allow using of free space inside extended partitions for LVM (vtrefny)
- Use sys.exit instead of blivetgui.quit in certain situations (vtrefny)
- AddDialog: fix size selection for btrfs disks (vtrefny)
- Remove obsolete option to embedd blivet-gui to another app (vtrefny)
- Remove some obsolete/unused BlivetUtils methods (vtrefny)

* Thu May 14 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.3.2-1
- Devel branch for l10n on Zanata (vtrefny)
- Use currentSize instead of partedDevice.length for empty disks (vtrefny)
- add_device method refactoring (vtrefny)
- Display progress in ProcessingWindow dialog (vtrefny)
- BlivetGUI: Call the blivet_do_it method with progress report support (vtrefny)
- Add progress callback support in BlivetUtils.blivet_do_it (vtrefny)
- Fix Makefile and spec for python3 (vtrefny)
- Add thinlv support to DeviceInformationDialog (vtrefny)
- Do not try to display information about unknown devices (vtrefny)
- Added support for creating LVM thinpools and thinlvs (vtrefny)
- Pylint fixes (vtrefny)
- Fix displaying parents in device information dialog (vtrefny)
- Add version information to the AboutDialog (vtrefny)
- Fix adding encrypted partitions (vtrefny)
- Fix displaying future mountpoint in kickstart mode (vtrefny)
- Pylint fixes (vtrefny)
- Fix 'None' as disk.model in kickstart dialogs (vtrefny)
- New option to show device information (vtrefny)
- Do not (de)activate non-existing options in menus/toolbars (vtrefny)
- Do not allow to resize lvs with snapshots (vtrefny)
- AddDialog refactoring (vtrefny)
- Add support for creating LVM snapshots (vtrefny)
- Python 3 compatible localisation support (vtrefny)

* Mon Apr 27 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.3.1-1
- Fix catching exception when trying to decrypt LUKS device (vtrefny)
- Fix python-meh requirement to Python 3 version (vtrefny)
- Remove obsolete methon convert_to_size (vtrefny)
- Fix None disk.model in description (vtrefny)
- Use format.systemMountpoint instead of format.mountpoint (vtrefny)
- New version 0.3.0 (vtrefny)

* Wed Apr 22 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.3.0-1
- Add translator credits to AboutDialog (vtrefny)
- Merge branch 'separate-processes' into devel (vtrefny)
- Advanced logging and python-meh support (vtrefny)
- Check if the server starts in blivet-gui main() (vtrefny)
- Fix returning of BlivetProxyObject and id to it (vtrefny)
- Pylint checks and docstrings (vtrefny)
- Logging server communication (vtrefny)
- Add message verification with a secret "key" (vtrefny)
- Remove temp directories atexit of server (vtrefny)
- Do not use Gio.Settings to obtaion default system font (vtrefny)
- Store blivet logs on server site (vtrefny)
- Delete udisks_loop.py file (no longer used) (vtrefny)
- Use blivet's ParentList for FreeSpaceDevice parents (vtrefny)
- Autorun server part, PID file for server (vtrefny)
- Update setup.py with new package_data (vtrefny)
- Use ProxyDataContainer instead of ReturnList (vtrefny)
- Use ProxyDataContainer for old_mountpoints (vtrefny)
- Fix EditDialog using non-existing UserSelection class (vtrefny)
- More detailed information for proxy objects AttributeError (vtrefny)
- Create instance of BlivetUtils upon client request (vtrefny)
- Use ProxyDataContainer instead of ResizeInfo namedtuple (vtrefny)
- Catch exception raised during BlivetUtils calls (vtrefny)
- Send message length in messages and use it in recv (vtrefny)
- Do not forward LUKS decrypt exceptions to client (vtrefny)
- Use GLib.timeout_add instead of GObject.timeout_add (vtrefny)
- Delete socket file using atexit (vtrefny)
- Catch GLib.GError instead of blivet.errors.CryptoError (vtrefny)
- Pickle only whitelisted objects (vtrefny)
- Mutex-protected server calls (vtrefny)
- Proper catching and reraising exception during doIt() (vtrefny)
- Use UnixStreamServer instead of TCPServer (vtrefny)
- Close server on client exit (vtrefny)
- Fix blivetgui.reload() function (vtrefny)
- Use GLib.idle_add instead of GObject.idle_add (vtrefny)
- New way of re-raising exceptions from BlivetUtils (vtrefny)
- Remove unused functions; mark some functions as private (vtrefny)
- Replace BlivetUtils calls with BlivetGUIClient calls (vtrefny)
- Replace UserSelection with ProxyDataContainer (vtrefny)
-"Binary" file for server/daemon part (vtrefny)
- blivet-gui process separation (vtrefny)
- Do not check root privilegies for blivet-gui (client part) (vtrefny)

* Mon Apr 13 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.4-1
- Auto-ellipsize longer strings in ListPartitions (vtrefny)
- Fix widget spacing in AddLabelDialog (vtrefny)
- Better handling of raw device formats (#1207743) (vtrefny)
- Fix blivetgui.reload() function (vtrefny)
- Python3 compatibility for device visualisation (vtrefny)
- Python3 compatible re-raising exceptions (vtrefny)
- Do not allow resizing of non-existing devices. (vtrefny)
- Catch GLib.GError instead of blivet.errors.CryptoError (vtrefny)
- Fix device visualisation with russian locale (#1202955) (vtrefny)
- EditDialog: Set the value of size SpinButton to device size (vtrefny)
- Do not display current size in EditDialog (#1201706) (vtrefny)

* Fri Mar 13 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.3-1
- Fix resizing LVs (#1201745) (vtrefny)
- Start KickstartSelectDevicesDialog with MainWindow as parent (vtrefny)
- Simplyfication of MainMenu, ActionsMenu and ActionsToolbar classes (vtrefny)
- Do not call updateSizeInfo() multiple times (vtrefny)
- Removed last dependency on blivet from BlivetGUI (vtrefny)
- EditDialog: Inform about corrupted filesystems (#1198239) (vtrefny)
- Fix python-meh handler.install (vtrefny)
- Fix returning success when editting LVM VGs (vtrefny)
- Do not refresh views when there are actions scheduled (vtrefny)
- DeviceCanvas: do not select invalid path (vtrefny)
- Re-raise exception from BlivetUtils with original traceback (vtrefny)
- Move logging from BlivetUtisl to BlivetGUI (vtrefny)
- Move thread creation and calling doIt() from ProcessingWindow (vtrefny)
- Move handling errors from BlivetUtils to BlivetGUI, part 2 (vtrefny)
- Move handling errors from BlivetUtils to BlivetGUI (vtrefny)
- ListPartitions cleanup (vtrefny)
- Fix blivet required version (>= 1.0) (vtrefny)
- Merge branch 'new_class_model' (vtrefny)
- Simplification of ListAction and undo history (vtrefny)
- New class model - preparation for root/non-root separation (vtrefny)
- New version 0.2.2 (vtrefny)
- New version 0.2.2 (vtrefny)

* Mon Feb 23 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.2-1
- Store blivet program log too (vtrefny)
- Fix Size calling (vtrefny)
- Replace filter with regexp (vtrefny)
- blivet.size is now module (vtrefny)
- Fix covertTo to use blivet.size.parseUnits function (vtrefny)
- New version 0.2.1 (vtrefny)

* Wed Feb 18 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.1-1
- Fix python-meh for processing window (vtrefny)
- python-meh support (vtrefny)
- Base default container name on distribution name (vtrefny)
- Removed some ununsed functions (vtrefny)
- Enable blivet logging, preparations for blivet-gui internal logging (vtrefny)
- Detect minimal device (partition and LV) size during BlivetUtils initialization (vtrefny)
- Swap is not resizable (vtrefny)
- Catch exceptions when checnking minSize on device with broken fs (vtrefny)
- Fix luks passphrase dialog spacing (vtrefny)
- Added root_check_window.ui file (vtrefny)
- 'Root privilegies required' dialog changed to window (vtrefny)
- MainMenu: partition_menu renamed to device_menu (vtrefny)
- pylint removed unallowed spaces (vtrefny)

* Thu Jan 22 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.0-6
- GitHub release as source for spec file (vtrefny)

* Thu Jan 22 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.0-5
- Fixed macro-in-changelog rpmlint warning (vtrefny)

* Thu Jan 22 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.0-4
- New build 0.2.0-4
- Fedora review: updated specfile, licence added to package (vtrefny)
- %%clean section removed from spec file (vtrefny)

* Tue Jan 20 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.0-3
- Licence file added (GPLv2) (vtrefny)
- New source location (vtrefny)

* Tue Jan 20 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.2.0-2
- Version bumped to 0.2 (vtrefny)
- EditDialog: typo (vtrefny)
- Fixed generating spec file changelog (vtrefny)

* Mon Jan 19 2015 Vojtech Trefny <vtrefny@redhat.com> - 0.1.11-1
- New version 0.1.11 (vtrefny)
- bumpver target for makefile (vtrefny)
- Merge branch 'master' of github.com:vojtechtrefny/blivet-gui (vtrefny)
- Specific binary file for desktop file (vtrefny)
- User help update (vtrefny)
- Fix python-blivet required version (vtrefny)
- Fix long device names (vtrefny)
- Suppress broad-except pylint errors. (amulhern)
- Change relative to absolute imports. (amulhern)
- Omit or hide unused variables and computations. (amulhern)
- main.py moved to blivet-gui file (vtrefny)
- Omit needless imports. (amulhern)
- Move % operator outside translation. (amulhern)
- Do not use wildcard import. (amulhern)
- Do not use builtin name format as parameter name. (amulhern)
- Fix bad indentation. (amulhern)
- Initial pylint setup. (amulhern)
- Support lvm inside extended partitions (vtrefny)
- pylint (vtrefny)
- AddDialog: Move btrfs type chooser above parents view (vtrefny)
- Do not clear actions after apply in ks mode (vtrefny)
- blivet-gui man page (vtrefny)
- Fix embedded function and example (vtrefny)
- fedora-review fixes for spec and desktop file (vtrefny)
- Python binary file (vtrefny)
- Check if file exists while saving ks (vtrefny)
- Mountpoint support for btrfs in ks mode (vtrefny)
- Don't allow editing mdmember partitions (vtrefny)
- Version 0.1.10 (vtrefny)
- Do not sort child devices on disks with raw device (vtrefny)
- Fix unicode converting bug (vtrefny)

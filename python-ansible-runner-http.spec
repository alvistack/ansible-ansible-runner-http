# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-ansible-runner-http
Epoch: 100
Version: 1.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Ansible Runner HTTP Event Emitter
License: Apache-2.0
URL: https://pypi.org/project/ansible-runner-http/#history
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This project is a plugin for Ansible Runner that allows emitting Ansible
status and events to HTTP services in the form of POST events. This can
allow Runner to notify other systems as Ansible jobs are run and to
deliver key events to that system if it's interested.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ansible-runner-http
Summary: Ansible Runner HTTP Event Emitter
Requires: python3
Requires: python3-requests
Requires: python3-requests-unixsocket
Provides: python3-ansible-runner-http = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-runner-http) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-runner-http = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-runner-http) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-runner-http = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-runner-http) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ansible-runner-http
This project is a plugin for Ansible Runner that allows emitting Ansible
status and events to HTTP services in the form of POST events. This can
allow Runner to notify other systems as Ansible jobs are run and to
deliver key events to that system if it's interested.

%files -n python%{python3_version_nodots}-ansible-runner-http
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-ansible-runner-http
Summary: Ansible Runner HTTP Event Emitter
Requires: python3
Requires: python3-requests
Requires: python3-requests-unixsocket
Provides: python3-ansible-runner-http = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-runner-http) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-runner-http = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-runner-http) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-runner-http = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-runner-http) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-runner-http
This project is a plugin for Ansible Runner that allows emitting Ansible
status and events to HTTP services in the form of POST events. This can
allow Runner to notify other systems as Ansible jobs are run and to
deliver key events to that system if it's interested.

%files -n python3-ansible-runner-http
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog

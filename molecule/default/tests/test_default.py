import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_windows_feature_exists(host):
    f = host.ansible("win_feature", "name='dhcp'")
    assert f["changed"] is False


def test_dhcp_empty_scope(host):
    f = host.ansible("win_shell", "Get-DhcpServerv4Scope", check=False)
    print(f)
    assert len(f['stdout_lines']) is 0

# SPDX-License-Identifier: GPL-3.0-only

import pytest

import xmipp4

def test_returns_device_manager(__setup_interface_catalog):
  assert xmipp4.compute.get_device_manager(
    __setup_interface_catalog
  ) is not None

def test_always_returns_same_device_manager(__setup_interface_catalog):
  dm1 = xmipp4.compute.get_device_manager(__setup_interface_catalog)
  dm2 = xmipp4.compute.get_device_manager(__setup_interface_catalog)
  assert dm1 is dm2

def test_returns_default_backends(__setup_interface_catalog):
  dm = xmipp4.compute.get_device_manager(
    __setup_interface_catalog
  )
  assert dm.backends == ['cpu']

def test_returns_default_devices(__setup_interface_catalog):
  dm = xmipp4.compute.get_device_manager(
    __setup_interface_catalog
  )
  assert dm.devices == [xmipp4.compute.DeviceIndex('cpu', 0)]

@pytest.fixture
def __setup_interface_catalog():
  return xmipp4.InterfaceCatalog()

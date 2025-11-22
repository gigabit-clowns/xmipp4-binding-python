# SPDX-License-Identifier: GPL-3.0-only

import unittest
from unittest.mock import patch

import pytest

import xmipp4

def test_should_allow_inheriting_from_device(__setup_device):
	assert isinstance(__setup_device, xmipp4.hardware.Device)

def test_whatever(__setup_device):
	assert __setup_device.create_device_queue() == 0

@pytest.fixture
def __setup_device():
	class DeviceMock(xmipp4.hardware.Device):
		pass
	
	mymock = DeviceMock()
	mymock.create_device_queue = unittest.mock.MagicMock(return_value=42)

	return xmipp4.hardware.launder(mymock)

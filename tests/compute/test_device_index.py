#***************************************************************************
# Authors:     Oier Lauzirika Zarrabeitia (oierlauzi@bizkaia.eu)
#              Martín Salinas Antón (ssalinasmartin@gmail.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# 02111-1307  USA
#
#  All comments concerning this program package may be sent to the
#  e-mail address 'xmipp@cnb.csic.es'
# ***************************************************************************
import pytest

import xmipp4

def test_constructor_from_params():
  xmipp4.compute.DeviceIndex('host', 0) is not None

def test_constructor_from_string():
  xmipp4.compute.DeviceIndex('cuda:0') is not None

def test_returns_expected_properties():
  device_index = xmipp4.compute.DeviceIndex('cuda', 1)
  assert (
    (
      device_index.backend, device_index.id
    ) == ('cuda', 1)
  )

@pytest.mark.parametrize(
  "backend, id, are_equals",
  [
    pytest.param("host", 0, False, id="With different backend"),
    pytest.param("cuda", 0, False, id="With different id"),
    pytest.param("cuda", 1, True, id="Equals")
  ]
)
def test_are_equals(backend, id, are_equals):
  d1 = xmipp4.compute.DeviceIndex(backend, id)
  d2 = xmipp4.compute.DeviceIndex('cuda', 1)
  assert (d1 == d2) == are_equals

@pytest.mark.parametrize(
  "backend, id, are_not_equals",
  [
    pytest.param("host", 0, True, id="With different id"),
    pytest.param("cuda", 0, True, id="With different backend"),
    pytest.param("host", 1, False, id="Equals")
  ]
)
def test_are_not_equals(backend, id, are_not_equals):
  d1 = xmipp4.compute.DeviceIndex(backend, id)
  d2 = xmipp4.compute.DeviceIndex('host', 1)
  assert (d1 != d2) == are_not_equals

@pytest.mark.parametrize(
  "backend, id, is_less",
  [
    pytest.param("host", 0, True, id="With smaller id"),
    pytest.param("cuda", 0, True, id="With \"smaller\" backend & smaller id"),
    pytest.param("cuda", 1, True, id="With \"smaller\" backend"),
    pytest.param("cuda", 2, True, id="With \"smaller\" backend & bigger id"),
    pytest.param("host", 1, False, id="Equals"),
    pytest.param("host", 2, False, id="With bigger id"),
    pytest.param("metal", 1, False, id="With \"bigger\" backend"),
    pytest.param("metal", 0, False, id="With \"bigger\" backend & smaller id"),
    pytest.param("metal", 2, False, id="With \"bigger\" backend & bigger id")
  ]
)
def test_is_less(backend, id, is_less):
  d1 = xmipp4.compute.DeviceIndex(backend, id)
  d2 = xmipp4.compute.DeviceIndex("host", 1)
  assert (d1 < d2) == is_less

@pytest.mark.parametrize(
  "backend, id",
  [
    pytest.param("host", 0, id="With host backend"),
    pytest.param("host", 1, id="Equals"),
    pytest.param("cuda", 0, id="With CUDA backend")
  ]
)
def test_is_less_with_same_(backend, id):
  d1 = xmipp4.compute.DeviceIndex(backend, id)
  d2 = xmipp4.compute.DeviceIndex("host", 1)
  assert d1 <= d2

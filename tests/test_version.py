#***************************************************************************
# Authors:     Oier Lauzirika Zarrabeitia (oierlauzi@bizkaia.eu)
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
import pickle

import xmipp4

def test_version_constructor():
  v = xmipp4.Version(1234, 567, 890)
  assert (
    (
      v.major, v.minor, v.patch
    ) == (1234, 567, 890)
  )

def test_versions_are_equal():
  v1 = xmipp4.Version(1234, 567, 890)
  v2 = xmipp4.Version(1234, 567, 890)
  assert v1 == v2

def test_versions_are_not_equal():
  v1 = xmipp4.Version(1234, 567, 890)
  v2 = xmipp4.Version(1234, 567, 891)
  assert v1 != v2

def test_version_is_less():
  v1 = xmipp4.Version(1234, 567, 890)
  v2 = xmipp4.Version(1234, 567, 891)
  assert v1 < v2

def test_version_is_less_or_equal():
  v1 = xmipp4.Version(1234, 567, 890)
  v2 = xmipp4.Version(1234, 567, 890)
  assert v1 <= v2

def test_version_is_greater():
  v1 = xmipp4.Version(1234, 567, 890)
  v2 = xmipp4.Version(1234, 567, 891)
  assert v2 > v1

def test_version_is_greater_or_equal():
  v1 = xmipp4.Version(1234, 567, 890)
  v2 = xmipp4.Version(1234, 567, 890)
  assert v1 >= v2

def test_version_to_string():
  v = xmipp4.Version(1234, 567, 890)
  assert str(v) == "1234.567.890"

def test_version_pickle():
  v = xmipp4.Version(1234, 567, 890)
  pickled = pickle.dumps(v)
  unpickled = pickle.loads(pickled)
  assert v == unpickled

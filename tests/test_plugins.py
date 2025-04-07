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
import xmipp4

def test_plugin_manager_constructor():
  assert xmipp4.PluginManager() is not None

def test_plugin_manager_discovers_plugins_without_plugins():
  pm = xmipp4.PluginManager()
  pm.discover_plugins()
  assert pm.plugins == []

def test_interface_registry_constructor():
  assert xmipp4.InterfaceRegistry() is not None

def test_interface_registry_registers_plugins_without_plugins():
  ir = xmipp4.InterfaceRegistry()
  pm = xmipp4.PluginManager()
  n_plugins = ir.register_plugins(pm)
  assert n_plugins == 0

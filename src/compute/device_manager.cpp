/***************************************************************************
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
 * 02111-1307  USA
 *
 *  All comments concerning this program package may be sent to the
 *  e-mail address 'xmipp@cnb.csic.es'
 ***************************************************************************/

#include "device_manager.hpp"

#include <xmipp4/core/compute/device_manager.hpp>
#include <xmipp4/core/compute/device_create_parameters.hpp>
#include <xmipp4/core/compute/device.hpp>
#include <xmipp4/core/compute/host/host_device_backend.hpp> // TODO remove

#include <pybind11/stl.h> // Required for std::vector binding

namespace xmipp4
{
namespace compute
{

namespace py = pybind11;

void register_device_manager(pybind11::module_ &m)
{
    py::class_<device_manager>(m, "device_manager")
        .def(py::init<>())
        .def(
            "enumerate_backends", 
            [](device_manager &self) -> std::vector<std::string> {
                std::vector<std::string> backends;
                self.enumerate_backends(backends);
                return backends;
            }
        )
        .def(
            "enumerate_devices", 
            [](device_manager &self) -> std::vector<device_index> {
                std::vector<device_index> indices;
                self.enumerate_devices(indices);
                return indices;
            }
        )
        .def(
            "get_device_properties", 
            [](device_manager &self, const device_index &index) -> device_properties {
                device_properties desc;
                if(!self.get_device_properties(index, desc)) {
                    throw std::invalid_argument("Requested device does not exist.");
                }
                return desc;
            }
        )
        .def("create_device", &device_manager::create_device);
        // TODO get backend 

    m.def("register_host_backend", &host_device_backend::register_at); // TODO remove

}

} // namespace compute
} // namespace xmipp4

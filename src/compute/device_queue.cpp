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

#include "device_queue.hpp"

#include <xmipp4/core/compute/device_queue.hpp>

#include <sstream>

namespace xmipp4
{
namespace compute
{

namespace py = pybind11;

void bind_device_queue(pybind11::module_ &m)
{
    py::class_<device_queue>(m, "DeviceQueue")
        .def_property_readonly("is_idle", &device_queue::is_idle)
        .def("wait_util_completed", &device_queue::wait_until_completed);
}

} // namespace compute
} // namespace xmipp4

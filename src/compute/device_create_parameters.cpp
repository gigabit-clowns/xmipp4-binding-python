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

#include "device_create_parameters.hpp"

#include <xmipp4/core/compute/device_create_parameters.hpp>

namespace xmipp4
{
namespace compute
{

namespace py = pybind11;

void register_device_create_parameters(pybind11::module_ &m)
{
    py::class_<device_create_parameters>(m, "device_create_parameters")
        .def(py::init<>())
        .def_property(
            "desired_queue_count", 
            &device_create_parameters::get_desired_queue_count, 
            &device_create_parameters::set_desired_queue_count
        )
        .def(py::pickle(
            [](const device_create_parameters &l) -> pybind11::tuple // __getstate__
            {
                return py::make_tuple(
                    l.get_desired_queue_count()
                );
            },
            [](py::tuple t) -> device_create_parameters  // __setstate__
            {
                device_create_parameters result;
                result.set_desired_queue_count(t[0].cast<std::size_t>());
                return result;
            }
        ));

}

} // namespace compute
} // namespace xmipp4

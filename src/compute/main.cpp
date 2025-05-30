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

#include "main.hpp"

#include "device.hpp"
#include "device_event.hpp"
#include "device_index.hpp"
#include "device_manager.hpp"
#include "device_properties.hpp"
#include "device_queue.hpp"
#include "device_queue_pool.hpp"
#include "device_to_host_event.hpp"
#include "device_type.hpp"

namespace xmipp4
{
namespace compute
{

namespace py = pybind11;

void bind_compute(pybind11::module_ &m)
{
    bind_device(m);
    bind_device_event(m);
    bind_device_index(m);
    bind_device_manager(m);
    bind_device_properties(m);
    bind_device_queue(m);
    bind_device_queue_pool(m);
    bind_device_to_host_event(m);
    bind_device_type(m);
}

} // namespace compute
} // namespace xmipp4

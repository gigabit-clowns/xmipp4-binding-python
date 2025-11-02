// SPDX-License-Identifier: GPL-3.0-only

#include "device.hpp"

#include <xmipp4/core/hardware/device.hpp>
#include <xmipp4/core/hardware/device_memory_allocator.hpp>
#include <xmipp4/core/hardware/host_memory_allocator.hpp>
#include <xmipp4/core/hardware/host_to_device_transfer.hpp>
#include <xmipp4/core/hardware/device_to_host_transfer.hpp>
#include <xmipp4/core/hardware/device_copy.hpp>
#include <xmipp4/core/hardware/device_event.hpp>
#include <xmipp4/core/hardware/device_to_host_event.hpp>

namespace xmipp4
{
namespace hardware
{

namespace py = pybind11;

void bind_device(pybind11::module_ &m)
{
    py::class_<device, std::shared_ptr<device>>(m, "Device")
        .def(
            "create_device_memory_allocator", 
            &device::create_device_memory_allocator,
            py::keep_alive<0, 1>()
        )
        .def(
            "create_host_memory_allocator", 
            &device::create_host_memory_allocator,
            py::keep_alive<0, 1>()
        )
        .def("create_host_to_device_transfer", 
            &device::create_host_to_device_transfer,
            py::keep_alive<0, 1>()
        )
        .def(
            "create_device_to_host_transfer", 
            &device::create_device_to_host_transfer,
            py::keep_alive<0, 1>()
        )
        .def(
            "create_device_copy", 
            &device::create_device_copy,
            py::keep_alive<0, 1>()
        )
        .def(
            "create_device_event", 
            &device::create_device_event,
            py::keep_alive<0, 1>()
        )
        .def(
            "create_device_to_host_event", 
            &device::create_device_to_host_event,
            py::keep_alive<0, 1>()
        );

}

} // namespace hardware
} // namespace xmipp4

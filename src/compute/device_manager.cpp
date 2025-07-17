// SPDX-License-Identifier: GPL-3.0-only

#include "device_manager.hpp"

#include <xmipp4/core/compute/device_manager.hpp>

#include <xmipp4/core/interface_catalog.hpp>
#include <xmipp4/core/compute/device_create_parameters.hpp>
#include <xmipp4/core/compute/device.hpp>

#include <pybind11/stl.h> // Required for std::vector binding

namespace xmipp4
{
namespace compute
{

static device_manager& get_device_manager(interface_catalog &catalog)
{
    return catalog.get_backend_manager<device_manager>();
}



namespace py = pybind11;

void bind_device_manager(pybind11::module_ &m)
{
    py::class_<device_manager>(m, "DeviceManager")
        .def_property_readonly(
            "backends",
            [](device_manager &self) -> std::vector<std::string>
            {
                std::vector<std::string> backends;
                self.enumerate_backends(backends);
                return backends;
            }
        )
        .def_property_readonly(
            "devices",
            [](device_manager &self) -> std::vector<device_index>
            {
                std::vector<device_index> indices;
                self.enumerate_devices(indices);
                return indices;
            }
        )
        .def(
            "get_device_properties",
            [](device_manager &self, const device_index &index) -> device_properties
            {
                device_properties desc;
                if(!self.get_device_properties(index, desc)) {
                    throw std::invalid_argument("Requested device does not exist.");
                }
                return desc;
            }
        )
        .def(
            "create_device",
            [] (device_manager &self,
                const device_index& index,
                const py::kwargs &kwargs ) -> std::shared_ptr<device>
            {
                std::shared_ptr<device> result;
                device_create_parameters params;
                if(kwargs.contains("desired_queue_count")) {
                    params.set_desired_queue_count(kwargs["desired_queue_count"].cast<std::size_t>());
                }

                if(!(result = self.create_device(index, params))) {
                    throw std::invalid_argument("Requested device does not exist.");
                }

                return result;
            },
            py::keep_alive<0, 1>()
        );

    m.def(
        "get_device_manager",
        &get_device_manager,
        py::return_value_policy::reference,
        py::keep_alive<0, 1>()
    );

}

} // namespace compute
} // namespace xmipp4

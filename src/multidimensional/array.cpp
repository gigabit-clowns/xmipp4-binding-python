// SPDX-License-Identifier: GPL-3.0-only

#include "array.hpp"

#include <xmipp4/core/multidimensional/array.hpp>

namespace xmipp4
{
namespace multidimensional
{

namespace py = pybind11;

void bind_array(pybind11::module_ &m)
{
	py::class_<array>(m, "Array")
		.def(py::init<>()) // Keep?
		.def_property_readonly("dtype", &array::get_data_type)
		.def_property_readonly("ndim", &array::get_rank)
		.def_property_readonly("shape", &array::get_extents)
		// array apply_subscripts(span<const dynamic_subscript> subscripts) --> __getitem__(*args)
		.def("__getitem__", &array::apply_subscripts, py::arg("subscripts"))
		.def_property_readonly("T", &array::transpose)
		.def("transpose", &array::transpose)
		.def_property_readonly("mT", [](array &a) { return a.matrix_transpose(-2, -1); })
		.def("matrix_transpose", &array::matrix_transpose, py::arg("axis1") = -2, py::arg("axis2") = -1)
		.def("matrix_diagonal", &array::matrix_diagonal, py::arg("axis1") = -2, py::arg("axis2") = -1)
		.def("squeeze", &array::squeeze)
		.def("broadcast_to", &array::broadcast_to, py::arg("extents"));
}

} // namespace multidimensional
} // namespace xmipp4

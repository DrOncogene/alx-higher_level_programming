#define PY_SSIZE_T_CLEAN
#include <Python.h>

void
print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyObject *item;

	if (PyList_CheckExact(p)){
		printf("[*] Size of the python list = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", PyObject_Size(p));
		for (i = 0; i < PyList_Size(p); i++){
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
